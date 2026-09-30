"""Integration test: real Temporal/Kubernetes, deterministic diagnosis fixture (NO Claude call)."""
import asyncio
from collections import Counter
import json
import os
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE / ".runtime/kubehealer"))
from temporalio import activity
from temporalio.client import Client
from temporalio.worker import Worker
from activities.k8s_activities import get_pod_details
from lab_activities import scan_cluster, execute_fix
from workflows.healer_workflow import HealerWorkflow
from models import Diagnosis, HealerInput

@activity.defn(name="diagnose_pod")
async def fixture_diagnosis(details: str) -> Diagnosis:
    name = details.splitlines()[0].removeprefix("Pod: ")
    # A delay creates a reproducible crash window between completed activities.
    await asyncio.sleep(5)
    if name.startswith("web-app-"):
        action, fix = "fix_image", {"image": "nginx:alpine"}
    elif name.startswith("memory-app-"):
        action, fix = "patch_resources", {"memory": "256Mi"}
    elif name.startswith("config-app-"):
        action, fix = "skip", {}
    else:
        raise ValueError("Unexpected pod outside fixtures")
    with (BASE / ".runtime/offline-diagnoses.txt").open("a") as log:
        log.write(name + "\n")
    return Diagnosis(name, "Deterministic test fixture", "medium", action,
                     "Fixture only; not an AI diagnosis", fix, "days89-lab")

async def worker():
    client = await Client.connect("localhost:7233")
    async with Worker(client, task_queue="day89-offline-test",
                      workflows=[HealerWorkflow],
                      activities=[scan_cluster, get_pod_details, execute_fix, fixture_diagnosis]):
        await asyncio.Future()

async def wait_state(handle, predicate):
    deadline = time.monotonic() + 180
    while time.monotonic() < deadline:
        state = await handle.query(HealerWorkflow.get_state)
        if predicate(state):
            return state
        await asyncio.sleep(1)
    raise TimeoutError("Workflow did not reach expected state")

async def test():
    (BASE / ".runtime/offline-diagnoses.txt").write_text("")
    client = await Client.connect("localhost:7233")
    children = []
    def launch():
        log = (BASE / ".runtime/offline-worker.log").open("a")
        child = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                 stdout=log, stderr=log)
        children.append(child)
        log.close()
        return child
    try:
        child = launch()
        handle = await client.start_workflow(HealerWorkflow.run,
            HealerInput(namespace="days89-lab", auto_approve=False),
            id="day89-offline-" + str(int(time.time())), task_queue="day89-offline-test")
        state = await wait_state(handle, lambda s: s["phase"] == "diagnosing" and len(s["diagnoses"]) >= 1)
        completed_name = state["diagnoses"][0]["pod_name"]
        child.kill()
        child.wait(timeout=10)
        print("Worker killed during diagnosis after one completed activity")
        launch()
        state = await wait_state(handle, lambda s: s["phase"] == "awaiting_approval")
        assert len(state["diagnoses"]) == 3, state
        assert state["results"] == [], "Fix ran before approval"
        counts = Counter((BASE / ".runtime/offline-diagnoses.txt").read_text().splitlines())
        assert counts[completed_name] == 1, "Completed diagnosis was re-executed"
        print("Replay reused completed diagnosis; awaiting approval; no fixes applied")
        for diagnosis in state["diagnoses"]:
            signal = HealerWorkflow.reject_pod if diagnosis["action"] == "skip" else HealerWorkflow.approve_pod
            await handle.signal(signal, diagnosis["pod_name"])
        print(await asyncio.wait_for(handle.result(), timeout=90))
        history = await handle.fetch_history()
        (BASE / ".runtime/offline-history.json").write_text(history.to_json())
        print("Real Temporal history saved privately; Claude was replaced by a deterministic fixture")
    finally:
        for child in children:
            if child.poll() is None:
                child.terminate()
                child.wait(timeout=10)

if __name__ == "__main__":
    asyncio.run(worker() if "--worker" in sys.argv else test())
