import requests
from typing import List, Dict, Any


class ShopifyClient:
    """
    Executes ShopifyQL queries against Shopify Analytics API.
    """

    def __init__(self):
        # In production, tokens come securely from Rails
        self.api_version = "2023-10"

    def execute_shopifyql(self, store_id: str, query: str) -> List[Dict[str, Any]]:
        """
        Executes a ShopifyQL query and returns raw data.

        NOTE:
        - This is mocked for demo purposes
        - Structure matches Shopify Analytics response
        """

        # -----------------------------
        # MOCK RESPONSE (Demo / Interview)
        # -----------------------------
        if "inventory_levels" in query:
            return [
                {
                    "product_title": "Product A",
                    "available_quantity": 50,
                    "daily_sales_rate": 10
                },
                {
                    "product_title": "Product B",
                    "available_quantity": 20,
                    "daily_sales_rate": 8
                }
            ]

        if "FROM orders" in query:
            return [
                {
                    "product_title": "Product A",
                    "total_quantity": 300,
                    "total_sales": 45000
                },
                {
                    "product_title": "Product B",
                    "total_quantity": 220,
                    "total_sales": 33000
                }
            ]

        return []

        # -----------------------------
        # REAL IMPLEMENTATION (Future)
        # -----------------------------
        """
        url = f"https://{store_id}/admin/api/{self.api_version}/shopifyql.json"

        headers = {
            "X-Shopify-Access-Token": "<TOKEN>",
            "Content-Type": "application/json"
        }

        payload = {
            "query": query
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception("Shopify API error")

        return response.json().get("data", [])
        """
