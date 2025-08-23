"""
Travel Tools - Flight Search Service
Simple mock flight search for travel planning.
"""

from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta


@dataclass
class FlightInfo:
    """Flight information data structure."""

    origin: str
    destination: str
    departure_date: str
    price: float
    airline: str
    duration: str
    stops: int


def search_flights(
    origin: str, destination: str, departure_date: str
) -> List[FlightInfo]:
    """
    Search for flights between origin and destination.
    This is a mock service - in real implementation, use Amadeus or Skyscanner API.
    """
    try:
        # Mock flight data with some variation based on destination
        base_price = 800 if "Tokyo" in destination else 600

        mock_flights = [
            FlightInfo(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
                price=base_price + 99.99,
                airline="Air France",
                duration="8h 30m",
                stops=0,
            ),
            FlightInfo(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
                price=base_price + 299.99,
                airline="Lufthansa",
                duration="10h 15m",
                stops=1,
            ),
            FlightInfo(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
                price=base_price - 100.00,
                airline="Budget Airways",
                duration="12h 45m",
                stops=2,
            ),
        ]

        return mock_flights

    except Exception as e:
        print(f"Flight search error: {e}")
        return []


def format_flight_results(flights: List[FlightInfo]) -> str:
    """Format flight search results for display."""
    if not flights:
        return "No flights found."

    result = f"Found {len(flights)} flights:\n\n"
    for i, flight in enumerate(flights, 1):
        result += f"{i}. {flight.airline}\n"
        result += f"   {flight.origin} → {flight.destination}\n"
        result += f"   Date: {flight.departure_date}\n"
        result += f"   Duration: {flight.duration}, Stops: {flight.stops}\n"
        result += f"   Price: ${flight.price:.2f}\n\n"

    return result
