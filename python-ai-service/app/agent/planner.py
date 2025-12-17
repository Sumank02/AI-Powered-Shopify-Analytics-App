from datetime import datetime, timedelta


class QueryPlanner:
    """
    Converts intent into a structured data plan.
    """

    def create_plan(self, intent: str, question: str) -> dict:
        """
        Create a query plan based on intent.
        """

        if intent == "sales":
            return self._sales_plan(question)

        if intent == "inventory":
            return self._inventory_plan(question)

        if intent == "customers":
            return self._customer_plan(question)

        raise ValueError("Unsupported intent type")

    # --------------------------------------------------
    # SALES PLAN
    # --------------------------------------------------
    def _sales_plan(self, question: str) -> dict:
        return {
            "resource": "orders",
            "metrics": ["total_quantity", "total_sales"],
            "group_by": "product",
            "time_window": self._extract_time_window(question),
            "limit": 5
        }

    # --------------------------------------------------
    # INVENTORY PLAN
    # --------------------------------------------------
    def _inventory_plan(self, question: str) -> dict:
        return {
            "resource": "inventory",
            "metrics": ["available_quantity", "daily_sales_rate"],
            "group_by": "product",
            "time_window": self._extract_time_window(question),
            "projection": True
        }

    # --------------------------------------------------
    # CUSTOMER PLAN
    # --------------------------------------------------
    def _customer_plan(self, question: str) -> dict:
        return {
            "resource": "customers",
            "metrics": ["order_count"],
            "filters": ["repeat_customers"],
            "time_window": self._extract_time_window(question)
        }

    # --------------------------------------------------
    # TIME WINDOW EXTRACTION
    # --------------------------------------------------
    def _extract_time_window(self, question: str) -> dict:
        """
        Converts natural language time into date ranges.
        Defaults to last 30 days.
        """
        today = datetime.utcnow()

        q = question.lower()

        if "7 days" in q or "last week" in q:
            start = today - timedelta(days=7)

        elif "90" in q or "quarter" in q:
            start = today - timedelta(days=90)

        elif "next week" in q:
            start = today - timedelta(days=7)

        elif "next month" in q:
            start = today - timedelta(days=30)

        else:
            start = today - timedelta(days=30)

        return {
            "start_date": start.date().isoformat(),
            "end_date": today.date().isoformat()
        }
