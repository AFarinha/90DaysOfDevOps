"""Analyze GitHub Actions using bounded read-only tools."""
import os
from pathlib import Path
import sys
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from devops_tools import run, identifier

REPOSITORY = os.getenv("CI_REPOSITORY", "AFarinha/90DaysOfDevOps")

@tool
def list_workflow_runs(status: str = "failure") -> str:
    """List the five most recent failed GitHub Actions runs in the configured repository."""
    if status not in {"failure", "success", "completed", "in_progress", "queued"}:
        raise ValueError("Invalid run status")
    return run(["gh", "run", "list", "--repo", REPOSITORY, "--status", status,
                "--limit", "5", "--json", "databaseId,name,conclusion"])

@tool
def get_failed_logs(run_id: str) -> str:
    """Read failed step logs for a numeric GitHub Actions run ID, limited to 5000 characters."""
    if not run_id.isdigit():
        raise ValueError("Run ID must be numeric")
    return run(["gh", "run", "view", run_id, "--repo", REPOSITORY, "--log-failed"])

@tool
def get_workflow_file(workflow_name: str) -> str:
    """Read a workflow file from the current repository, rejecting path traversal."""
    identifier(workflow_name)
    root = (Path.cwd() / ".github/workflows").resolve()
    path = (root / workflow_name).resolve()
    if path.parent != root:
        raise ValueError("Workflow must be inside .github/workflows")
    return path.read_text()[:5000] if path.is_file() else "Workflow file not found"

if __name__ == "__main__":
    agent = create_agent(ChatOllama(model=os.getenv("OLLAMA_MODEL", "gemma4"),
                                   temperature=0, num_ctx=4096, num_predict=256, reasoning=False),
                         [list_workflow_runs, get_failed_logs, get_workflow_file])
    result = agent.invoke({"messages": [("user", " ".join(sys.argv[1:]) or "What failed in my last CI run?")]},
                          {"recursion_limit": 16})
    print(result["messages"][-1].content)
