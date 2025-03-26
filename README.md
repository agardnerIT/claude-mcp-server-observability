# Claude MCP Server for Observability Demo

Companion repo to this video: [Claude MCP Server for Observability](https://youtu.be/lWO9M9SpGAg)

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
                "/full/path/claude-mcp-server-observability",
                "run",
                "logreader.py"
            ]
    }
  }
}
```

## Step 3: Launch Claude

You should see the little "connector" icon. Click that and it should show one installed server called logreader.

## Step 4: Ask Claude for Help!

Start a new chat and ask something like: `I noticed errors in the logs on the 22nd March. Help me investigate`

Claude should figure out that it should use your MCP server (and the three tools it offers) to help answer your query. Claude may request permission to run the tools. Accept the permissions.

Sooner or later (may need additional hints / prompts) you should get the answer and suggested remediation:

- Pipeline C and the release was most likely responsible for the errors
- You should contact Susan


