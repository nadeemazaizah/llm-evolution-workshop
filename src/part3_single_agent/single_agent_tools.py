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

# Import our custom tools
from tools.weather_tool import get_weather_info
from tools.flight_tool import search_flights
from tools.currency_tool import convert_currency

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


# Create OpenAI client for GitHub Models
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=GITHUB_TOKEN,
    base_url="https://models.inference.ai.azure.com",
)


# Create agent with tools
travel_agent = AssistantAgent(
    name="TravelAgent",
    model_client=model_client,
    tools=[get_weather_info, search_flights, convert_currency],
    system_message="""You are a helpful travel planning assistant. You have access to:
    1. Weather information - use to check weather conditions for destinations
    2. Flight search - use to find flights between cities
    3. Currency converter - use to help with budget planning
    Use these tools to provide comprehensive, practical travel advice.
    Always be specific with dates, amounts, and locations when using tools.""",
    reflect_on_tool_use=True,
    model_client_stream=True,
)


# Run the agent and stream the messages to the console.
async def main(query):
    await Console(travel_agent.run_stream(task=query))
    # Close the connection to the model client.
    await model_client.close()


if __name__ == "__main__":
    import asyncio

    # query = "what is the weather like in Tokyo in end of August?"
    # query = "find flights from New York City (NYC) to Tokyo on 2025-09-15"
    # query = "how much is 100 USD in JPY?"
    query = "find flights from New York City (NYC) to Tokyo on 2025-09-15, provide the expected weather in Tokyo around that date, and convert 100 USD to JPY."
    asyncio.run(main(query))
