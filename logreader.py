from typing import Any
from mcp.server.fastmcp import FastMCP
from loguru import logger
import json

# Initialize FastMCP server
mcp = FastMCP(name="logreader")

@mcp.tool(name="get_important_logs", description="get contents of all important logs")
def get_key_logs():
    logs = ["file.log", "file2.log"]
    returned_lines = []
    for log in logs:
        with open(file=log, mode="r") as log_file:
            lines = log_file.readlines()
            for line in lines:
                if "error" in line.lower():
                    returned_lines.append(line)

@mcp.tool(name="get_important_events", description="get important CICD events from a log file")
def get_important_events():
    logs = ["file.log", "file2.log"]
    returned_lines = []

    for log in logs:
        with open(file=log, mode="r") as log_file:
            lines = log_file.readlines()
            for line in lines:
                if "deployment" in line.lower():
                    returned_lines.append(line)
            
            return returned_lines

@mcp.tool(name="get_cicd_logs", description="retrieve all pipeline related events and logs")
def get_cicd_events():
    with open(file="pipeline.json") as pipeline_file:
        content = json.load(pipeline_file)
        return content


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
