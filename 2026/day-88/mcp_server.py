"""Expose the lab Kubernetes tools over MCP stdio."""
from fastmcp import FastMCP
from kubernetes_tools import TOOLS

mcp = FastMCP("Lab Kubernetes Tools")
for tool in TOOLS:
    mcp.tool(tool.func)

if __name__ == "__main__":
    mcp.run()
