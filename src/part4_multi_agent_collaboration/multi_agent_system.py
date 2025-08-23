"""
Multi-Agent Travel Planning System
Specialized agents collaborating for comprehensive travel planning.
"""

import os
from dotenv import load_dotenv

# AutoGen imports
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
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

# Flight Specialist Agent
flight_specialist = AssistantAgent(
    name="FlightSpecialist",
    model_client=model_client,
    tools=[search_flights],
    system_message="""You are a Flight Booking Specialist. Your expertise:
    - Find best flight options (price, duration, stops)
    - Airline recommendations and comparisons
    - Travel routes and timing optimization
    Focus ONLY on flight-related queries and recommendations.""",
)

# Weather Specialist Agent
weather_specialist = AssistantAgent(
    name="WeatherSpecialist",
    model_client=model_client,
    tools=[get_weather_info],
    system_message="""You are a Weather and Climate Specialist. Your expertise:
    - Weather forecasts and seasonal patterns
    - Climate recommendations for destinations
    - Weather-appropriate activity suggestions
    Focus ONLY on weather and climate information.""",
)

# Budget Specialist Agent
budget_specialist = AssistantAgent(
    name="BudgetSpecialist",
    model_client=model_client,
    tools=[convert_currency],
    system_message="""You are a Travel Budget Specialist. Your expertise:
    - Budget planning and cost optimization
    - Currency conversion and financial planning
    - Cost-effective travel recommendations
    Focus ONLY on budget and financial aspects of travel.""",
)

# Travel Coordinator (orchestrates the team)
travel_coordinator = AssistantAgent(
    name="TravelCoordinator",
    model_client=model_client,
    system_message="""You are the Travel Planning Coordinator. Your role:
    - Orchestrate the travel planning process
    - Synthesize recommendations from all specialists
    - Ensure plan coherence and feasibility
    - Present final comprehensive travel plan
    
    Work with the team to create complete travel recommendations.""",
)

# Create the multi-agent team
agents = [
    travel_coordinator,
    flight_specialist,
    weather_specialist,
    budget_specialist,
]
team = RoundRobinGroupChat(agents)


async def main(query):
    """Run the multi-agent travel planning system."""
    await Console(team.run_stream(task=query))
    await model_client.close()


if __name__ == "__main__":
    import asyncio

    # Example query - change this to test different scenarios
    query = (
        "Plan a trip from New York to Tokyo departing September 15th "
        "with a $2500 USD budget. Need weather info and flight options."
    )

    asyncio.run(main(query))
