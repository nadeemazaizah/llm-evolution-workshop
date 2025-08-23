"""
Simple RAG Retrieval System using TF-IDF
This module handles the retrieval of relevant travel information.
TF-IDF can be easily replaced with advanced embedding models.
"""

import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_travel_data(file_path=None):
    """Load travel data from JSON file."""
    if file_path is None:
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "travel_data.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["destinations"]


def create_document_texts(destinations):
    """Create searchable text from destination data."""
    documents = []
    for dest in destinations:
        # Combine all text fields for better search
        text = f"{dest['destination']} {dest['description']} "
        text += f"{' '.join(dest['top_attractions'])} "
        text += f"{' '.join(dest['local_cuisine'])} "
        text += f"{dest['cultural_tips']} {dest['weather_info']}"
        documents.append(text)
    return documents


def find_relevant_destinations(query, destinations, top_k=2):
    """
    Find most relevant destinations based on user query using TF-IDF.
    This can be replaced with advanced embedding models like OpenAI embeddings.
    """
    # Create document texts for search
    documents = create_document_texts(destinations)

    # Initialize TF-IDF vectorizer (can be replaced with embedding models)
    vectorizer = TfidfVectorizer(stop_words="english")

    # Fit and transform documents
    doc_vectors = vectorizer.fit_transform(documents)

    # Transform query
    query_vector = vectorizer.transform([query])

    # Calculate similarity scores
    similarities = cosine_similarity(query_vector, doc_vectors)[0]

    # Get top k most similar destinations
    top_indices = similarities.argsort()[-top_k:][::-1]

    relevant_destinations = []
    for idx in top_indices:
        if similarities[idx] > 0:  # Only include if there's some similarity
            relevant_destinations.append(destinations[idx])

    return relevant_destinations


def format_destination_info(destination):
    """Format destination information for the prompt."""
    info = f"Destination: {destination['destination']}\n"
    info += f"Best Season: {destination['best_season']}\n"
    info += f"Budget Range: {destination['budget_range']}\n"
    info += f"Top Attractions: {', '.join(destination['top_attractions'])}\n"
    info += f"Local Cuisine: {', '.join(destination['local_cuisine'])}\n"
    info += f"Transportation: {destination['transportation']}\n"
    info += f"Cultural Tips: {destination['cultural_tips']}\n"
    info += f"Weather: {destination['weather_info']}\n"
    return info
