from pydantic import BaseModel
from typing import Dict, Any


class QuestionResponse(BaseModel):
    """
    Response model returned to Rails API
    """

    answer: str
    confidence: str = "medium"
    metadata: Dict[str, Any] = {}
