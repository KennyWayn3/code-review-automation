"""
code-review-automation - MCP Server
"""
import json
from mcp.server import FastMCP

app = FastMCP("code-review-automation")


@app.tool()
def example_tool(input: str) -> str:
    """Example
    input (str): Input
    """
    return json.dumps({"tool": "example_tool", "params": {"input": input}})

if __name__ == "__main__":
    app.run(transport="stdio")
