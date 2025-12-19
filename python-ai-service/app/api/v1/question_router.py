from fastapi import APIRouter, HTTPException
from app.agent.agent import AnalyticsAgent
from app.models.request import QuestionRequest
from app.models.response import QuestionResponse

router = APIRouter()

# Initialize agent once (can be enhanced with dependency injection)
agent = AnalyticsAgent()


@router.post(
    "/questions",
    response_model=QuestionResponse,
    summary="Ask analytics questions in natural language"
)
async def ask_question(payload: QuestionRequest):
    """
    Receives a natural language question from Rails API,
    runs it through the AI agent, and returns insights.
    """
    try:
        result = agent.handle_question(
            store_id=payload.store_id,
            question=payload.question,
            access_token=payload.access_token
        )

        return QuestionResponse(
            answer=result["answer"],
            confidence=result.get("confidence", "medium"),
            metadata=result.get("metadata", {})
        )

    except ValueError as ve:
        # Used for validation / ambiguity errors
        raise HTTPException(
            status_code=400,
            detail=str(ve)
        )

    except Exception as e:
        # Catch unexpected agent failures
        raise HTTPException(
            status_code=500,
            detail="Failed to process analytics question"
        )
