"""
Travel Tools - Weather Service
Simple mock weather service for travel planning.
"""

from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class WeatherInfo:
    """Weather information data structure."""

    location: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    forecast_days: List[Dict[str, Any]]


def get_weather_info(location: str, days: int = 3) -> WeatherInfo:
    """
    Get weather information for a location.
    This is a mock service - in real implementation, use OpenWeatherMap API.
    """
    try:
        # Mock weather forecast data
        mock_forecast = [
            {
                "date": "2025-08-24",
                "high": 22,
                "low": 15,
                "condition": "Sunny",
                "rain_chance": 10,
            },
            {
                "date": "2025-08-25",
                "high": 18,
                "low": 12,
                "condition": "Cloudy",
                "rain_chance": 30,
            },
            {
                "date": "2025-08-26",
                "high": 20,
                "low": 14,
                "condition": "Light Rain",
                "rain_chance": 70,
            },
            {
                "date": "2025-08-27",
                "high": 25,
                "low": 16,
                "condition": "Partly Cloudy",
                "rain_chance": 20,
            },
            {
                "date": "2025-08-28",
                "high": 23,
                "low": 17,
                "condition": "Sunny",
                "rain_chance": 5,
            },
        ]

        return WeatherInfo(
            location=location,
            temperature=20.5,
            description="Partly cloudy with occasional showers",
            humidity=65,
            wind_speed=12.5,
            forecast_days=mock_forecast[:days],
        )

    except Exception as e:
        print(f"Weather service error: {e}")
        return WeatherInfo(
            location=location,
            temperature=20,
            description="Weather data unavailable",
            humidity=50,
            wind_speed=10,
            forecast_days=[],
        )
