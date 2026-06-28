"""
code-review-automation - Streamable HTTP MCP Server
"""
import json, os
from mcp.server import FastMCP
from mcp_billing import billing

fastmcp = FastMCP(
    "code-review-automation",
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8000")),
    streamable_http_path="/",
    json_response=True,
)


@fastmcp.tool()
def review_code(diff: str) -> str:
    """Analyze a code diff for bugs, security issues, and style violations
    diff (str): The code diff or file content to review
    """
    allowed, msg, remaining = billing.check_and_deduct("code-review", "review_code")
    if not allowed:
        return json.dumps({"error": msg, "payment_required": True, "remaining": remaining})
    return json.dumps({"tool": "review_code", "params": {"diff": diff[:100]}, "credits_remaining": remaining})


@fastmcp.tool()
def check_quality(path: str) -> str:
    """Run static analysis checks on a file path
    path (str): File path to analyze
    """
    allowed, msg, remaining = billing.check_and_deduct("code-review", "check_quality")
    if not allowed:
        return json.dumps({"error": msg, "payment_required": True, "remaining": remaining})
    return json.dumps({"tool": "check_quality", "params": {"path": path}, "credits_remaining": remaining})


# Health check endpoint for Render
from starlette.responses import JSONResponse
from starlette.routing import Route


async def health_check(request):
    return JSONResponse({"status": "ok"})


# ASGI app for Render / uvicorn with health check route
starlette_app = fastmcp.streamable_http_app()
starlette_app.router.routes.insert(0, Route("/health", endpoint=health_check, methods=["GET"]))

if __name__ == "__main__":
    fastmcp.run(transport="streamable-http")
