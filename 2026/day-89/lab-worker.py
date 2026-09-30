"""Run the upstream healer with namespace limits and the explicit approval starter."""
import asyncio
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / ".runtime/kubehealer"))
from kubernetes import config
_, active = config.list_kube_config_contexts()
if active["name"] != "kind-days81-90-lab":
    raise RuntimeError("Use the dedicated lab kubeconfig")
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise RuntimeError("ANTHROPIC_API_KEY is not configured locally")
from temporalio.client import Client
from temporalio.worker import Worker
from activities.k8s_activities import get_pod_details
from activities.llm_activities import diagnose_pod
from lab_activities import scan_cluster, execute_fix
from workflows.healer_workflow import HealerWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    async with Worker(client, task_queue="kubehealer", workflows=[HealerWorkflow],
                      activities=[scan_cluster, get_pod_details, diagnose_pod, execute_fix]):
        print("Lab worker ready; start-with-approval.py is required")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
