from typing import List, Dict, Any


def calculate_confidence(
    raw_data: List[Dict[str, Any]],
    intent: str
) -> str:
    """
    Calculates confidence level for the generated answer.
    """

    if not raw_data:
        return "low"

    data_points = len(raw_data)

    # Inventory answers depend heavily on accurate stock data
    if intent == "inventory":
        if data_points >= 2:
            return "high"
        return "medium"

    # Sales trends are generally more reliable
    if intent == "sales":
        if data_points >= 3:
            return "high"
        return "medium"

    # Customer analytics often has partial data
    if intent == "customers":
        if data_points >= 5:
            return "high"
        return "medium"

    return "medium"
