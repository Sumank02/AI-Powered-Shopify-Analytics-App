from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.question_router import router as question_router

app = FastAPI(
    title="AI Powered Shopify Analytics Service",
    description="LLM-powered agent that converts natural language questions into ShopifyQL insights",
    version="1.0.0"
)

# -------------------------------------------------
# Middleware
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Routes
# -------------------------------------------------
app.include_router(
    question_router,
    prefix="/api/v1",
    tags=["Questions"]
)

# -------------------------------------------------
# Health Check
# -------------------------------------------------
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "python-ai-service",
        "message": "AI service is running"
    }

# -------------------------------------------------
# Global Exception Handler
# -------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Catch-all exception handler to avoid leaking internal errors
    """
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc)
        }
    )
