"""Use the reference workflow with explicit human approval instead of its auto starter."""
import argparse
import asyncio
import json
from pathlib import Path
import sys

REFERENCE = Path(__file__).parent / ".runtime/kubehealer"
sys.path.insert(0, str(REFERENCE))
from temporalio.client import Client
from models import HealerInput
from workflows.healer_workflow import HealerWorkflow

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "status", "approve", "reject"])
    parser.add_argument("--pod")
    args = parser.parse_args()
    # The reference SDK loads only the dedicated kubeconfig supplied by the caller.
    from kubernetes import config
    _, active = config.list_kube_config_contexts()
    if active["name"] != "kind-days81-90-lab":
        raise RuntimeError("Select the disposable lab kubeconfig first")
    client = await Client.connect("localhost:7233")
    workflow_id = "day89-human-approval"
    if args.action == "start":
        await client.start_workflow(HealerWorkflow.run,
            HealerInput(namespace="days89-lab", auto_approve=False),
            id=workflow_id, task_queue="kubehealer")
        print("Started with auto_approve=False")
    else:
        handle = client.get_workflow_handle(workflow_id)
        if args.action == "status":
            print(json.dumps(await handle.query(HealerWorkflow.get_state), indent=2))
        else:
            if not args.pod:
                parser.error("--pod is required for a decision")
            state = await handle.query(HealerWorkflow.get_state)
            if state["phase"] != "awaiting_approval" or args.pod not in {
                    diagnosis["pod_name"] for diagnosis in state["diagnoses"]}:
                raise ValueError("Pod must have a pending diagnosis")
            signal = HealerWorkflow.approve_pod if args.action == "approve" else HealerWorkflow.reject_pod
            await handle.signal(signal, args.pod)
            print("Decision recorded")

if __name__ == "__main__":
    asyncio.run(main())
