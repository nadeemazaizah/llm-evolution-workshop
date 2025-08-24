import os
from openai import OpenAI
from dotenv import load_dotenv
from rag.rag_retrieval import (
    load_travel_data,
    find_relevant_destinations,
    format_destination_info,
)

# Load environment variables from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize OpenAI client with GitHub Models endpoint
# GitHub Models provides free access to popular LLMs including GPT-4o-mini
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)


def get_rag_enhanced_advice(user_query):
    """Get travel advice enhanced with RAG (retrieved information)."""
    # Step 1: Load travel data from JSON file
    destinations = load_travel_data()

    # Step 2: Find relevant destinations using TF-IDF similarity matching
    relevant_destinations = find_relevant_destinations(
        user_query,
        destinations,
    )

    # Step 3: Format retrieved information as context
    context = ""
    if relevant_destinations:
        context = "Here is relevant travel information:\n\n"
        for dest in relevant_destinations:
            context += format_destination_info(dest) + "\n"
    else:
        context = "No specific destination information found in the database."

    # Step 4: Create system prompt to use only provided context
    system_prompt = """
        You are a helpful travel assistant. 
        You must ONLY use the travel information provided in the user's message as your source of knowledge. 
        Do not use any external knowledge about destinations.

        Key instructions:
        - Base your recommendations EXCLUSIVELY on the provided travel information
        - If the provided information is insufficient to answer the question, clearly state what information is missing
        - Include specific details from the context such as attractions, cuisine, budget ranges, and cultural tips
        - If no relevant information is provided, politely explain that you don't have that information in your database
        - Be helpful and detailed, but stay within the bounds of the provided context
    """

    # Step 5: Create user prompt with context and query
    user_prompt = f"""
        Travel Information Database:
        {context}

        User Question: 
        {user_query}

        Please provide travel advice based ONLY on the information provided above.
        """

    # Step 6: Call GitHub Models API with RAG-enhanced prompt
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Free model via GitHub Models
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,  # Balance between creativity and consistency
        max_tokens=500,  # Limit response length for workshop demo
    )

    return response.choices[0].message.content


def main():
    """
    Main function demonstrating RAG-enhanced travel advice.

    This example shows the difference between basic LLM prompting and RAG:
    - Without RAG: Generic travel advice based on LLM training data
    - With RAG: Specific advice based on retrieved travel database information
    """

    # Example query - modify this to test different scenarios
    query = "Plan a trip to Tokyo"
    print(f"\n🔍 User Query: {query}")

    # Get RAG-enhanced advice with retrieved context
    advice = get_rag_enhanced_advice(query)
    print("\n💡 RAG-Enhanced Travel Advice:" f"\n{advice}")


if __name__ == "__main__":
    main()
