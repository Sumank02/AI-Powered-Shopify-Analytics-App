class LLMClient:
    """
    Wrapper around Large Language Models.
    Currently mocked for demo and safety.
    """

    def __init__(self, provider: str = "mock"):
        self.provider = provider

    def complete(self, prompt: str) -> str:
        """
        Generate a completion from an LLM.
        """

        # -----------------------------
        # MOCK RESPONSE
        # -----------------------------
        return (
            "Intent: inventory\n"
            "Metrics: available_quantity, daily_sales_rate\n"
            "Time window: last 30 days"
        )

        # -----------------------------
        # REAL IMPLEMENTATION (Future)
        # -----------------------------
        """
        if self.provider == "openai":
            response = openai.ChatCompletion.create(...)
            return response.choices[0].message.content
        """
