from typing import List, Dict, Any


class ResultExplainer:
    """
    Converts raw Shopify data into business-friendly explanations.
    """

    def explain(
        self,
        intent: str,
        question: str,
        raw_data: List[Dict[str, Any]],
        plan: dict
    ) -> str:

        if not raw_data:
            return "There is not enough data available to answer this question."

        if intent == "inventory":
            return self._explain_inventory(raw_data)

        if intent == "sales":
            return self._explain_sales(raw_data)

        if intent == "customers":
            return self._explain_customers(raw_data)

        return "Unable to generate explanation for this question."

    # --------------------------------------------------
    # INVENTORY EXPLANATION
    # --------------------------------------------------
    def _explain_inventory(self, data: List[Dict[str, Any]]) -> str:
        explanations = []

        for item in data:
            available = item.get("available_quantity", 0)
            daily_rate = item.get("daily_sales_rate", 0)

            if daily_rate == 0:
                continue

            days_left = available // daily_rate

            if days_left <= 7:
                explanations.append(
                    f"{item['product_title']} may go out of stock in about {days_left} days. "
                    f"Consider reordering soon."
                )

        if not explanations:
            return "All products have sufficient inventory for the near future."

        return " ".join(explanations)

    # --------------------------------------------------
    # SALES EXPLANATION
    # --------------------------------------------------
    def _explain_sales(self, data: List[Dict[str, Any]]) -> str:
        top_products = []

        for item in data:
            top_products.append(
                f"{item['product_title']} ({item['total_quantity']} units sold)"
            )

        return (
            "Your top selling products are: "
            + ", ".join(top_products)
            + "."
        )

    # --------------------------------------------------
    # CUSTOMER EXPLANATION
    # --------------------------------------------------
    def _explain_customers(self, data: List[Dict[str, Any]]) -> str:
        count = len(data)

        return (
            f"You had {count} repeat customers during this period, "
            "indicating healthy customer retention."
        )
