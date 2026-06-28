# code-review-automation - MCP Server

MCP server for automated code review using AI agents

## Installation

### pip
```bash
pip install code-review-automation
```

### uvx (recommended)
```bash
uvx code-review-automation
```

## Usage

Add to your Claude Desktop config:
```json
{"mcpServers": {"code-review-automation": {"command": "uvx", "args": ["code-review-automation"]}}}
```

## Available Tools
- **example_tool**: Example

## License
MIT

[![PyPI](https://img.shields.io/pypi/v/code-review-automation)](https://pypi.org/project/code-review-automation/) [![GitHub](https://img.shields.io/github/stars/KennyWayn3/code-review-automation)](https://github.com/KennyWayn3/code-review-automation)
