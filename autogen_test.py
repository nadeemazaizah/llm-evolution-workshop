import os
import asyncio
from typing import Annotated
from autogen_core.models import UserMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import (
    MaxMessageTermination,
    TextMentionTermination,
)
from autogen_agentchat.ui import Console

from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()


def add_numbers(
    a: Annotated[int, "First number"], b: Annotated[int, "Second number"]
) -> int:
    """Add two numbers together."""
    return a + b


def multiply_numbers(
    a: Annotated[int, "First number"], b: Annotated[int, "Second number"]
) -> int:
    """Multiply two numbers together."""
    return a * b


def divide_numbers(
    a: Annotated[float, "First number"], b: Annotated[float, "Second number"]
) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


async def main():
    # Check if required environment variables are set
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_LLM_DEPLOYMENT",
        "AZURE_OPENAI_LLM_API_VERSION",
    ]

    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set up your .env file or environment variables.")
        print("See README.md for setup instructions.")
        return

    model_client = AzureOpenAIChatCompletionClient(
        azure_deployment=os.getenv("AZURE_OPENAI_LLM_DEPLOYMENT"),
        model=os.getenv("AZURE_OPENAI_LLM_DEPLOYMENT"),
        api_version=os.getenv("AZURE_OPENAI_LLM_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    )

    print("=" * 60)
    print("LLM EVOLUTION DEMO - FROM SIMPLE TO ADVANCED")
    print("=" * 60)

    # STAGE 1: Direct LLM Model Call (No tools, no agents)
    print("\n🔹 STAGE 1: Direct LLM Model Call")
    print("-" * 40)

    simple_question = "What is the capital of France?"
    print(f"Question: {simple_question}")

    direct_result = await model_client.create(
        [UserMessage(content=simple_question, source="user")]
    )
    print(f"Answer: {direct_result.content}")

    # STAGE 2: LLM with Tools (Single Agent)
    print("\n🔹 STAGE 2: LLM with Tools (Single Agent)")
    print("-" * 40)

    agent_with_tools = AssistantAgent(
        name="calculator_agent",
        model_client=model_client,
        tools=[add_numbers, multiply_numbers, divide_numbers],
        system_message=(
            "You are a mathematical assistant. Use the provided tools "
            "for calculations. Show your work step by step."
        ),
    )

    math_question = "Calculate 15 + 25, then multiply the result by 3"
    print(f"Task: {math_question}")

    response = await agent_with_tools.run(task=math_question)
    print("Conversation flow:")
    for i, message in enumerate(response.messages):
        if hasattr(message, "source"):
            print(f"  {i+1}. {message.source}: {message.content}")
        else:
            print(f"  {i+1}. {type(message).__name__}: {message.content}")

    # STAGE 3: Team-based Multi-agent System
    print("\n🔹 STAGE 3: Team-based Multi-agent System")
    print("-" * 40)

    # Create specialized agents
    calculator_agent = AssistantAgent(
        name="calculator",
        model_client=model_client,
        tools=[add_numbers, multiply_numbers, divide_numbers],
        system_message=(
            "You are a calculator specialist. Perform mathematical "
            "calculations using the provided tools. Be precise and "
            "show each calculation step. Once you complete the "
            "calculations requested, pass the results to the analyst."
        ),
    )

    analyst_agent = AssistantAgent(
        name="analyst",
        model_client=model_client,
        system_message=(
            "You are a data analyst. You interpret mathematical results "
            "and provide insights. When you receive calculation results, "
            "provide analysis and conclude with 'ANALYSIS COMPLETE' to "
            "signal task completion."
        ),
    )

    # Create team with multiple termination conditions
    termination_condition = MaxMessageTermination(
        max_messages=8
    ) | TextMentionTermination("ANALYSIS COMPLETE")
    team = RoundRobinGroupChat(
        [calculator_agent, analyst_agent],
        termination_condition=termination_condition,
    )

    complex_task = (
        "I have 3 groups of students. Group A has 15 students, "
        "Group B has 25 students, and Group C has 20 students. "
        "Calculate the total number of students, then find the "
        "average class size if I want to divide them into 4 equal classes. "
        "Provide analysis of the results."
    )
    print(f"Complex Task: {complex_task}")
    print("\nTeam conversation:")

    # Run the team task
    await Console(team.run_stream(task=complex_task))


if __name__ == "__main__":
    asyncio.run(main())
