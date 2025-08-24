# mcp_server.py - FastMCP Server

import sys
import os
from mcp.server.fastmcp import FastMCP

# Add the project root to the path so we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.part3_single_agent.tools.flight_tool import search_flights

# Create an MCP server
mcp = FastMCP("Search flights MCP Server")


@mcp.tool()
def mcp_search_flights(origin: str, destination: str, departure_date: str):
    """Search for flights between two cities on a specific date."""
    return search_flights(origin, destination, departure_date)


if __name__ == "__main__":
    # Run the server using stdio for AutoGen integration
    mcp.run(transport="stdio")
