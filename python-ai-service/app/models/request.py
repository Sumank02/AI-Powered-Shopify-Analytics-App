from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    """
    Request model received from Rails API
    """

    store_id: str = Field(
        ...,
        example="example-store.myshopify.com",
        description="Shopify store domain"
    )

    question: str = Field(
        ...,
        example="How much inventory should I reorder for next week?",
        description="Natural language analytics question"
    )
