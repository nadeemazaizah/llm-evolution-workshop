"""
Simple RAG-Enhanced Travel Assistant using GitHub Models
This shows how external data enhances LLM responses with specific information.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from rag.rag_retrieval import (
    load_travel_data,
    find_relevant_destinations,
    format_destination_info,
)

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize OpenAI client with GitHub Models
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)


def get_rag_enhanced_advice(user_query):
    """Get travel advice enhanced with RAG (retrieved information)."""
    # Step 1: Load travel data from JSON file
    destinations = load_travel_data()

    # Step 2: Find relevant destinations using TF-IDF
    relevant_destinations = find_relevant_destinations(
        user_query,
        destinations,
    )

    # Step 3: Format retrieved information
    context = ""
    if relevant_destinations:
        context = "Here is relevant travel information:\n\n"
        for dest in relevant_destinations:
            context += format_destination_info(dest) + "\n"

    # Step 4: Create enhanced prompt with context
    system_prompt = (
        "You are a helpful travel assistant. Use the provided travel "
        "information to give specific, detailed advice. Include practical "
        "details like attractions, food, budget estimates, and cultural "
        "tips when available."
    )

    user_prompt = f"{context}\nUser Question: {user_query}"

    # Step 5: Get response from GitHub Models
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content


def main():
    """Main function demonstrating RAG-enhanced travel advice."""
    # User query - change this to test different questions
    query = "Plan a 5-day trip to Tokyo for first-time visitors"
    print(f"\nQuery: {query}")

    # Get RAG-enhanced advice
    advice = get_rag_enhanced_advice(query)
    print(f"💡 Enhanced Travel Advice:\n{advice}")


if __name__ == "__main__":
    main()
