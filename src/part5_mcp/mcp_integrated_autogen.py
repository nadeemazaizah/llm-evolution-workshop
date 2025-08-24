"""
Simple Tool-Enabled Travel Agent using AutoGen > 0.4 and GitHub Models
Demonstrates how external tools enhance agent capabilities.
"""

import os
from dotenv import load_dotenv

# AutoGen imports
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools


# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Create OpenAI client for GitHub Models
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=GITHUB_TOKEN,
    base_url="https://models.inference.ai.azure.com",
)


# Run the agent and stream the messages to the console.
async def main(query):
    # Get the absolute path to the MCP server script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_script = os.path.join(current_dir, "mcp_server.py")
    print("Server script path:", server_script)

    server_params = StdioServerParams(command="python", args=[server_script])
    mcp_tools = await mcp_server_tools(server_params)

    # Create agent with tools
    travel_agent = AssistantAgent(
        name="TravelAgent",
        model_client=model_client,
        tools=mcp_tools,
        system_message="""You are a helpful travel planning assistant. 
        You have access to: Flight search - use to find flights between cities
        Use these tools to provide comprehensive, practical travel advice.
        Always be specific with dates, amounts, and locations when using tools.""",
        reflect_on_tool_use=True,
        model_client_stream=True,
    )

    await Console(travel_agent.run_stream(task=query))
    # Close the connection to the model client.
    await model_client.close()


if __name__ == "__main__":
    import asyncio

    query = "find flights from New York City (NYC) to Tokyo on 2025-09-15"
    asyncio.run(main(query))
