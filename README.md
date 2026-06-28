# code-review-automation - MCP Server

MCP server for automated code review using AI agents. Analyze code diffs for bugs, security issues, and style violations, or run static analysis on file paths.

## Tools

### `review_code`
Analyze a code diff or file content for bugs, security issues, and style violations.
- **`diff`** (string, required): The code diff or file content to review

### `check_quality`
Run static analysis checks on a file path.
- **`path`** (string, required): File path to analyze

## Quick Start (local)

```bash
pip install -r requirements.txt
export MCP_BILLING_API=https://mcp-billing-api.onrender.com
uvicorn server:starlette_app --host 0.0.0.0 --port 8000
```

## Usage with Claude Desktop / MCP clients

```json
{
  "mcpServers": {
    "code-review-automation": {
      "url": "https://mcp-code-review.onrender.com/"
    }
  }
}
```

## Deployed endpoint

`https://mcp-code-review.onrender.com/` — Streamable HTTP transport at root path. Health check at `/health`.

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `MCP_BILLING_API` | Yes | Billing API endpoint |
| `MCP_LICENSE_KEY` | Yes | License key for billing |
| `AGENTICMARKET_SECRET` | No | Secret for AgenticMarket authentication |

## License

MIT
