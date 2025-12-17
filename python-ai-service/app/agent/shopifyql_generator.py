class ShopifyQLGenerator:
    """
    Generates ShopifyQL queries from a structured query plan.
    """

    def generate(self, intent: str, plan: dict) -> str:
        if intent == "sales":
            return self._sales_query(plan)

        if intent == "inventory":
            return self._inventory_query(plan)

        if intent == "customers":
            return self._customer_query(plan)

        raise ValueError("Unsupported intent for ShopifyQL generation")

    # --------------------------------------------------
    # SALES QUERY
    # --------------------------------------------------
    def _sales_query(self, plan: dict) -> str:
        time = plan["time_window"]

        return f"""
        FROM orders
        SHOW
            sum(line_items.quantity) AS total_quantity,
            sum(total_price) AS total_sales
        GROUP BY line_items.product_title
        SINCE {time["start_date"]}
        UNTIL {time["end_date"]}
        ORDER BY total_quantity DESC
        LIMIT {plan.get("limit", 5)}
        """

    # --------------------------------------------------
    # INVENTORY QUERY
    # --------------------------------------------------
    def _inventory_query(self, plan: dict) -> str:
        return """
        FROM inventory_levels
        SHOW
            sum(available) AS available_quantity
        GROUP BY product_title
        """

    # --------------------------------------------------
    # CUSTOMER QUERY
    # --------------------------------------------------
    def _customer_query(self, plan: dict) -> str:
        time = plan["time_window"]

        return f"""
        FROM orders
        SHOW
            count(order_id) AS order_count
        GROUP BY customer_id
        SINCE {time["start_date"]}
        UNTIL {time["end_date"]}
        HAVING order_count > 1
        """
