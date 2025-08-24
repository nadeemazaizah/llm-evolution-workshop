"""
Multi-Agent Travel Planning System
Specialized agents collaborating for comprehensive travel planning.
"""

import os
from dotenv import load_dotenv

# AutoGen imports
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

# Import our custom tools
from src.part3_single_agent.tools.weather_tool import get_weather_info
from src.part3_single_agent.tools.flight_tool import search_flights
from src.part3_single_agent.tools.currency_tool import convert_currency

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Create OpenAI client for GitHub Models
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=GITHUB_TOKEN,
    base_url="https://models.inference.ai.azure.com",
)

# Flight Agent
flight_agent = AssistantAgent(
    name="FlightAgent",
    description="An agent for searching flight information",
    model_client=model_client,
    tools=[search_flights],
    system_message="""
    You are a flight search agent.
    Your only tool is search_flights - use it to find information.
    You make only one search call at a time.
    Once you have the results, you never do calculations based on them.
    """,
    reflect_on_tool_use=True,
    model_client_stream=True,
)

# Weather Agent
weather_agent = AssistantAgent(
    name="WeatherAgent",
    description="An agent for searching weather information",
    model_client=model_client,
    tools=[get_weather_info],
    system_message="""
    You are a weather search agent.
    Your only tool is get_weather_info - use it to find information.
    You make only one search call at a time.
    Once you have the results, you never do calculations based on them.
    """,
    reflect_on_tool_use=True,
    model_client_stream=True,
)

# Budget Agent
budget_agent = AssistantAgent(
    name="BudgetAgent",
    description="An agent for searching budget information.",
    model_client=model_client,
    tools=[convert_currency],
    system_message="""
    You are a travel budget agent.
    Your job is to find the best currency conversion rates and budget options for travel.
    Your only tool is convert_currency - use it for currency conversion tasks.
    To check if the budget is sufficient for the trip, do the evaluation by your self with numbers compare
    This means you need to look at the flight prices and the budget in the same currency.
    You make only one search call at a time.
    Once you have the results, you never do calculations based on them.
    """,
    reflect_on_tool_use=True,
    model_client_stream=True,
)

# Planning Agent
planning_agent = AssistantAgent(
    name="PlanningAgent",
    description="An agent for planning tasks, this agent should be the first to engage when given a new task.",
    model_client=model_client,
    system_message="""
    You are a planning agent.
    Your job is to break down complex tasks into smaller, manageable subtasks.
    Your team members are:
    - FlightAgent
    - WeatherAgent
    - BudgetAgent 

    You only plan and delegate tasks - you do not execute them yourself.
    If there is no clear ask to specific agent don't assign the task to this agent

    When assigning tasks, use this format:
    1. <agent> : <task>

    You can assign tasks to multiple agents if needed.
    You can assign repetitive tasks to the same agent.

    Only after all tasks are complete, and the answer is summarized, and sufficient information is provided to the user query, end with "FINISHED".
    """,
    reflect_on_tool_use=True,
    model_client_stream=True,
)

# Define a termination condition that stops the task if the critic approves.
text_termination = TextMentionTermination("FINISHED")

# Create the multi-agent team
agents = [
    planning_agent,
    flight_agent,
    weather_agent,
    budget_agent,
]

selector_prompt = """
    Select an agent to perform task.

    {roles}

    Current conversation context:
    {history}

    Read the above conversation, then select an agent from {participants} to perform the next task.
    Make sure the PlanningAgent has assigned tasks before other agents start working.
    Only select one agent.
    """

team = SelectorGroupChat(
    agents,
    model_client=model_client,
    termination_condition=text_termination,
    selector_prompt=selector_prompt,
    allow_repeated_speaker=True,
)


async def main(query):
    """Run the multi-agent travel planning system."""
    await Console(team.run_stream(task=query))
    await model_client.close()


if __name__ == "__main__":
    import asyncio

    # Example query - change this to test different scenarios
    query = "find flights from New York City (NYC) to Tokyo on 2025-09-15, provide the expected weather in Tokyo around that date, and convert 100 USD to JPY."
    # query = "I have a budget of 100000 JPY, and I want to find flights to Tokyo on 2025-09-15."

    asyncio.run(main(query))
