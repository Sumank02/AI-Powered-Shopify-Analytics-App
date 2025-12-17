from app.agent.intent_classifier import IntentClassifier
from app.agent.planner import QueryPlanner
from app.agent.shopifyql_generator import ShopifyQLGenerator
from app.agent.validator import QueryValidator
from app.agent.explainer import ResultExplainer

from app.shopify.client import ShopifyClient
from app.utils.confidence_score import calculate_confidence


class AnalyticsAgent:
    """
    Central orchestrator for the agentic workflow.
    """

    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.planner = QueryPlanner()
        self.query_generator = ShopifyQLGenerator()
        self.validator = QueryValidator()
        self.explainer = ResultExplainer()
        self.shopify_client = ShopifyClient()

    def handle_question(self, store_id: str, question: str) -> dict:
        """
        Main entry point for handling a natural language question.
        """

        if not question or len(question.strip()) < 5:
            raise ValueError("Question is too short or unclear")

        # 1️⃣ Understand intent
        intent_result = self.intent_classifier.classify(question)

        # 2️⃣ Plan data requirements
        plan = self.planner.create_plan(
            intent=intent_result["intent"],
            question=question
        )

        # 3️⃣ Generate ShopifyQL
        shopifyql = self.query_generator.generate(
            intent=intent_result["intent"],
            plan=plan
        )

        # 4️⃣ Validate query
        self.validator.validate(shopifyql)

        # 5️⃣ Execute query against Shopify
        raw_data = self.shopify_client.execute_shopifyql(
            store_id=store_id,
            query=shopifyql
        )

        # 6️⃣ Explain results in business language
        explanation = self.explainer.explain(
            intent=intent_result["intent"],
            question=question,
            raw_data=raw_data,
            plan=plan
        )

        # 7️⃣ Confidence scoring
        confidence = calculate_confidence(
            raw_data=raw_data,
            intent=intent_result["intent"]
        )

        return {
            "answer": explanation,
            "confidence": confidence,
            "metadata": {
                "intent": intent_result["intent"],
                "plan": plan,
                "shopifyql": shopifyql
            }
        }
