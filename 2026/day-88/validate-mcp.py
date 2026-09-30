"""Exercise real MCP discovery and read-only calls without requiring an LLM."""
import asyncio
import os
from pathlib import Path
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({"kubernetes": {"transport": "stdio",
        "command": sys.executable, "args": [str(Path(__file__).with_name("mcp_server.py"))],
        "env": {"KUBECONFIG": os.environ["KUBECONFIG"]}}})
    tools = {t.name: t for t in await client.get_tools()}
    assert set(tools) == {"list_pods", "describe_pod", "get_events", "search_logs"}
    print("Discovered:", ", ".join(sorted(tools)))
    print(await tools["list_pods"].ainvoke({}))
    description = str(await tools["describe_pod"].ainvoke({"pod_name": "broken-pod"}))
    assert "CrashLoopBackOff" in description or "Error" in description, description
    print("describe_pod returned crash evidence")
    print(await tools["search_logs"].ainvoke({"keyword": "app starting"}))

if __name__ == "__main__":
    asyncio.run(main())
