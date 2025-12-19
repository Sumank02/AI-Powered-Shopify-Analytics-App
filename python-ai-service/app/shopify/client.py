import requests
from typing import List, Dict, Any, Optional


class ShopifyClient:
    """
    Executes ShopifyQL queries against Shopify Admin GraphQL API.
    
    Uses the correct Shopify API approach:
    - POST to GraphQL endpoint: /admin/api/{version}/graphql.json
    - Headers: X-Shopify-Access-Token
    - GraphQL mutation for ShopifyQL execution
    """

    def __init__(self):
        # Use latest stable API version
        self.api_version = "2024-01"

    def execute_shopifyql(
        self, 
        store_id: str, 
        query: str, 
        access_token: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Executes a ShopifyQL query via Shopify Admin GraphQL API.
        
        Args:
            store_id: Shopify store domain (e.g., "example-store.myshopify.com")
            query: ShopifyQL query string
            access_token: Shopify access token (shpat_xxxxx)
                        If None, uses demo mode with mocked data
        
        Returns:
            List of data records from ShopifyQL query
        """

        # -----------------------------
        # DEMO MODE (No token provided)
        # -----------------------------
        if not access_token:
            return self._get_mock_data(query)

        # -----------------------------
        # REAL IMPLEMENTATION
        # ShopifyQL via GraphQL Admin API
        # -----------------------------
        graphql_url = f"https://{store_id}/admin/api/{self.api_version}/graphql.json"
        
        headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json"
        }

        # ShopifyQL queries are executed via GraphQL mutation
        graphql_mutation = {
            "query": """
                mutation runShopifyQL($query: String!) {
                    shopifyqlQuery(query: $query) {
                        data
                        errors {
                            message
                        }
                    }
                }
            """,
            "variables": {
                "query": query.strip()
            }
        }

        try:
            response = requests.post(
                graphql_url,
                json=graphql_mutation,
                headers=headers,
                timeout=30
            )

            if response.status_code != 200:
                raise Exception(f"Shopify API error: {response.status_code} - {response.text}")

            result = response.json()
            
            # Handle GraphQL errors
            if "errors" in result:
                error_messages = [err.get("message", "Unknown error") for err in result["errors"]]
                raise Exception(f"Shopify GraphQL errors: {', '.join(error_messages)}")

            # Extract data from GraphQL response
            shopifyql_result = result.get("data", {}).get("shopifyqlQuery", {})
            
            if "errors" in shopifyql_result and shopifyql_result["errors"]:
                error_messages = [err.get("message", "Unknown error") for err in shopifyql_result["errors"]]
                raise Exception(f"ShopifyQL errors: {', '.join(error_messages)}")

            data = shopifyql_result.get("data", [])
            
            # Parse JSON string if data is returned as string
            if isinstance(data, str):
                import json
                data = json.loads(data)

            return data if isinstance(data, list) else []

        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to connect to Shopify API: {str(e)}")

    def _get_mock_data(self, query: str) -> List[Dict[str, Any]]:
        """
        Returns mocked data for demo purposes when no access token is provided.
        """
        if "inventory_levels" in query.lower():
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

        if "from orders" in query.lower():
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
