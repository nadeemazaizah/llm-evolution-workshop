import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_travel_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "travel_data.json")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["destinations"]


def create_document_texts(destinations):
    documents = []
    for dest in destinations:
        # Combine all relevant text fields for comprehensive search
        # Order matters: destination name first for relevance weighting
        text = f"{dest['destination']} {dest['description']} "
        text += f"{' '.join(dest['top_attractions'])} "
        text += f"{' '.join(dest['local_cuisine'])} "
        text += f"{dest['cultural_tips']} {dest['weather_info']}"
        documents.append(text)
    return documents


def find_relevant_destinations(query, destinations, top_k=2):
    # Convert structured data to searchable text documents
    documents = create_document_texts(destinations)

    # Initialize TF-IDF vectorizer
    # TF-IDF: Term Frequency × Inverse Document Frequency
    # Prioritizes unique words that appear frequently in specific documents
    vectorizer = TfidfVectorizer(
        stop_words="english",  # Remove common words (the, and, is, etc.)
    )

    try:
        # Transform documents into TF-IDF vectors
        doc_vectors = vectorizer.fit_transform(documents)

        # Transform user query into TF-IDF vector (same space)
        query_vector = vectorizer.transform([query])

        # Calculate cosine similarity between query and all documents
        # Cosine similarity measures vector angles (0=different, 1=same)
        similarities = cosine_similarity(query_vector, doc_vectors)[0]

        # Get top-k most similar destinations
        # argsort() returns indices sorted by similarity (ascending)
        # [-top_k:][::-1] gets last top_k indices and reverses (descending)
        top_indices = similarities.argsort()[-top_k:][::-1]

        # Filter results with actual similarity (> 0)
        relevant_destinations = []
        for idx in top_indices:
            # Only include if there's some similarity
            if similarities[idx] > 0:
                relevant_destinations.append(destinations[idx])
                print(
                    f"📍 Found: {destinations[idx]['destination']} "
                    f"(similarity: {similarities[idx]:.3f})"
                )

        if not relevant_destinations:
            print("🔍 No relevant destinations found for query:", query)

        return relevant_destinations

    except Exception as e:
        print(f"❌ Error during similarity search: {e}")
        return []


def format_destination_info(destination):
    # Format information in a structured, LLM-friendly way
    info = f"**{destination['destination']}**\n"
    info += f"• Best Season: {destination['best_season']}\n"
    info += f"• Budget Range: {destination['budget_range']}\n"
    info += f"• Top Attractions: {', '.join(destination['top_attractions'])}\n"
    info += f"• Local Cuisine: {', '.join(destination['local_cuisine'])}\n"
    info += f"• Transportation: {destination['transportation']}\n"
    info += f"• Cultural Tips: {destination['cultural_tips']}\n"
    info += f"• Weather: {destination['weather_info']}\n"
    return info
