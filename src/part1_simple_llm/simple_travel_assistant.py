"""
Simple Travel Planner using OpenAI SDK with GitHub Models
A basic script for travel planning assistance without classes.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize OpenAI client with GitHub Models
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)


def get_travel_advice(user_query):
    """Get travel advice from the LLM."""
    system_prompt = """You are a helpful travel planner. 
                        Provide practical travel advice including:
                            - Destination recommendations
                            - Itinerary suggestions
                            - Budget estimates
                            - Best time to visit
                            - Local attractions and activities
                            - Transportation tips           
                        Keep your responses concise and helpful.
                    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to run the travel planner."""
    # User query - change this to any travel question you want
    query = "Plan a trip to Tokyo"
    print(f"\n🔍 User Query: {query}")

    # Get travel advice
    advice = get_travel_advice(query)
    print(f"💡 Travel Advice:\n{advice}")


if __name__ == "__main__":
    main()
