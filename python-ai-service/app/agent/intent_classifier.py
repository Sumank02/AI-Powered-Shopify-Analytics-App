import re


class IntentClassifier:
    """
    Classifies user intent from a natural language question.
    """

    INVENTORY_KEYWORDS = [
        "inventory", "stock", "out of stock", "reorder",
        "units", "available", "run out"
    ]

    SALES_KEYWORDS = [
        "sales", "selling", "sold", "revenue",
        "top selling", "orders", "trend"
    ]

    CUSTOMER_KEYWORDS = [
        "customer", "customers", "repeat", "loyal",
        "returning", "buyers"
    ]

    TIME_PATTERNS = {
        "7_days": r"(7 days|last week|past week)",
        "30_days": r"(30 days|last month|past month)",
        "90_days": r"(90 days|last 90|quarter)",
        "next_week": r"(next week)",
        "next_month": r"(next month)"
    }

    def classify(self, question: str) -> dict:
        """
        Classify intent and extract signals.
        """
        q = question.lower()

        intent = self._detect_intent(q)
        time_window = self._detect_time_window(q)

        if not intent:
            raise ValueError(
                "Unable to determine intent. Please clarify your question."
            )

        return {
            "intent": intent,
            "time_window": time_window or "30_days"
        }

    def _detect_intent(self, question: str) -> str:
        for word in self.INVENTORY_KEYWORDS:
            if word in question:
                return "inventory"

        for word in self.SALES_KEYWORDS:
            if word in question:
                return "sales"

        for word in self.CUSTOMER_KEYWORDS:
            if word in question:
                return "customers"

        return ""

    def _detect_time_window(self, question: str) -> str:
        for label, pattern in self.TIME_PATTERNS.items():
            if re.search(pattern, question):
                return label
        return ""
