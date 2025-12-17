class QueryValidator:
    """
    Validates ShopifyQL queries before execution.
    """

    ALLOWED_TABLES = [
        "orders",
        "inventory_levels"
    ]

    FORBIDDEN_KEYWORDS = [
        "DELETE",
        "UPDATE",
        "DROP",
        "INSERT"
    ]

    def validate(self, query: str):
        if not query or len(query.strip()) == 0:
            raise ValueError("Generated ShopifyQL query is empty")

        upper_query = query.upper()

        # Block destructive keywords
        for keyword in self.FORBIDDEN_KEYWORDS:
            if keyword in upper_query:
                raise ValueError("Unsafe operation detected in query")

        # Validate table usage
        if not self._contains_allowed_table(query):
            raise ValueError("Query uses unsupported Shopify resource")

    def _contains_allowed_table(self, query: str) -> bool:
        q = query.lower()
        for table in self.ALLOWED_TABLES:
            if f"from {table}" in q:
                return True
        return False
