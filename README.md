# Claude MCP Server for Observability Demo

Companion repo to this video: [Claude MCP Server for Observability](https://example.com)

## Prerequisites

You'll need Claude Desktop for this (a free account is OK)

## Step 1: Start MCP Server

- Clone this repo
- Install dependencies `pip install -r requirements.txt`
- Start the server with `python logreader.py`

## Step 2: Install MCP Servers in Claude Desktop

Open Claude Desktop. Go to `Claude > Settings > Developer` and click `Edit config`.

This will open a folder and highlight a particular JSON file. Open that file and set the content to what's below.

This step makes Claude Desktop aware of your MCP server.

```
{
  "mcpServers": {
    "logreader": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/adamgardner/claude/mcp_test",
                "run",
                "logreader.py"
            ]
    }
  }
}
```
