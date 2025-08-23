"""
Travel Tools - Currency Conversion Service
Simple currency converter for travel budgeting.
"""

from typing import Dict


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Get exchange rate between two currencies.
    This is a mock service - in real implementation, use ExchangeRate-API.
    """
    # Mock exchange rates (USD as base)
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "CAD": 1.25,
        "AUD": 1.35,
        "CHF": 0.92,
        "CNY": 6.45,
    }

    try:
        if from_currency == to_currency:
            return 1.0

        # Convert through USD if needed
        usd_rate_from = exchange_rates.get(from_currency, 1.0)
        usd_rate_to = exchange_rates.get(to_currency, 1.0)

        # Calculate rate: from_currency -> USD -> to_currency
        rate = usd_rate_to / usd_rate_from
        return round(rate, 4)

    except Exception as e:
        print(f"Currency conversion error: {e}")
        return 1.0


def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> Dict:
    """Convert amount from one currency to another."""
    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate

    return {
        "original_amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "exchange_rate": rate,
        "converted_amount": round(converted_amount, 2),
    }


def format_currency_conversion(conversion: Dict) -> str:
    """Format currency conversion for display."""
    result = "Currency Conversion:\n"
    result += f"{conversion['original_amount']} {conversion['from_currency']} = "
    result += f"{conversion['converted_amount']} {conversion['to_currency']}\n"
    result += f"Exchange Rate: 1 {conversion['from_currency']} = "
    result += f"{conversion['exchange_rate']} {conversion['to_currency']}"

    return result
