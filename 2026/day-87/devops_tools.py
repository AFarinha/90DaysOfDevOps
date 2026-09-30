"""Bounded, read-only Docker tools; no shell commands or secret-bearing inspect output."""
import re
import subprocess
from langchain_core.tools import tool

def identifier(value):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", value):
        raise ValueError("Invalid resource name")
    return value

def run(args):
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=20)
        output = result.stdout + result.stderr
        return f"exit_code={result.returncode}\n" + output[:5000]
    except subprocess.TimeoutExpired:
        return "Command timed out after 20 seconds"
    except OSError as exc:
        return f"Command unavailable: {exc}"

@tool
def list_containers() -> str:
    """List Docker containers and status to find stopped or restarting workloads."""
    return run(["docker", "ps", "-a", "--format", "{{.Names}} {{.Image}} {{.Status}}"])

@tool
def get_logs(container_name: str) -> str:
    """Read the last 50 log lines of a named Docker container to diagnose failures."""
    return run(["docker", "logs", "--tail", "50", identifier(container_name)])

@tool
def inspect_container(container_name: str) -> str:
    """Inspect a container's state, image and entry command without exposing environment variables."""
    return run(["docker", "inspect", "--format",
                "{{json .State}} {{json .Config.Image}} {{json .Config.Cmd}}",
                identifier(container_name)])

@tool
def list_images() -> str:
    """List local Docker images and their sizes to investigate disk usage."""
    return run(["docker", "images", "--format", "{{.Repository}}:{{.Tag}} {{.Size}}"])

TOOLS = [list_containers, get_logs, inspect_container, list_images]
