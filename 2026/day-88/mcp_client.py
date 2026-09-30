"""Discover MCP tools and ask a local LLM to use them."""
import asyncio
import os
from pathlib import Path
import sys
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({"kubernetes": {
        "transport": "stdio", "command": sys.executable,
        "args": [str(Path(__file__).with_name("mcp_server.py"))],
        "env": {"KUBECONFIG": os.environ["KUBECONFIG"]}}})
    tools = await client.get_tools()
    agent = create_agent(ChatOllama(model=os.getenv("OLLAMA_MODEL", "gemma4"),
                                   temperature=0, num_ctx=4096, num_predict=256, reasoning=False), tools)
    result = await agent.ainvoke({"messages": [("user", " ".join(sys.argv[1:]) or "Why is broken-pod crashing?")]},
                                {"recursion_limit": 16})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
