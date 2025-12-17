INTENT_CLASSIFICATION_PROMPT = """
You are an analytics assistant for a Shopify store.

Classify the user's question into one of:
- inventory
- sales
- customers

Extract:
- intent
- time range
- metrics needed

Question:
{question}
"""

SHOPIFYQL_GENERATION_PROMPT = """
You are an expert ShopifyQL analyst.

Based on the plan below, generate a valid ShopifyQL query.

Plan:
{plan}
"""
