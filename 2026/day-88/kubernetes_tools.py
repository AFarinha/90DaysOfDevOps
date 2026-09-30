"""Read-only Kubernetes tools constrained to a disposable lab context/namespace."""
import os
from langchain_core.tools import tool
from devops_tools import run, identifier

NAMESPACE = os.getenv("LAB_NAMESPACE", "days88-lab")
CONTEXT = "kind-days81-90-lab"

def kubectl(*args):
    return run(["kubectl", "--context", CONTEXT, "-n", NAMESPACE, *args])

@tool
def list_pods() -> str:
    """List pod status in the allowed lab namespace to find unhealthy workloads."""
    return kubectl("get", "pods")

@tool
def describe_pod(pod_name: str) -> str:
    """Describe a lab pod, its conditions and events to diagnose scheduling or startup failures."""
    return kubectl("describe", "pod", identifier(pod_name))

@tool
def get_events() -> str:
    """Read recent events in the lab namespace, ordered by timestamp."""
    return kubectl("get", "events", "--sort-by=.lastTimestamp")

@tool
def search_logs(keyword: str) -> str:
    """Search the last 100 log lines per lab pod for a literal keyword."""
    import json
    import subprocess
    result = subprocess.run(["kubectl", "--context", CONTEXT, "-n", NAMESPACE,
                             "get", "pods", "-o", "json"], capture_output=True,
                             text=True, timeout=20)
    if result.returncode:
        return result.stderr[:5000]
    found = []
    for pod in json.loads(result.stdout)["items"][:20]:
        name = pod["metadata"]["name"]
        logs = kubectl("logs", name, "--tail=100")
        if keyword.lower() in logs.lower():
            found.append(name + ": keyword found")
    return "\n".join(found) or "No matches in the sampled logs"

TOOLS = [list_pods, describe_pod, get_events, search_logs]
