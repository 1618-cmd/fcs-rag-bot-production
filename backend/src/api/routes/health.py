"""
Health check endpoints.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from ...utils.config import settings

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    environment: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    
    Returns the current status of the API.
    """
    return HealthResponse(
        status="healthy",
        environment=settings.environment,
        version="1.0.0",
    )


@router.get("/health/ready")
async def readiness_check():
    """
    Readiness check endpoint.
    
    Verifies that the service is ready to accept requests.
    Checks critical dependencies.
    """
    checks = {
        "api": "ok",
        "openai": "ok" if settings.openai_api_key else "missing",
        "qdrant": "ok" if settings.qdrant_url and settings.qdrant_api_key else "missing",
    }
    
    is_ready = all(status == "ok" for status in checks.values())
    
    return {
        "status": "ready" if is_ready else "not_ready",
        "checks": checks,
    }


@router.get("/health/warmup")
@router.head("/health/warmup")  # Also support HEAD requests for monitoring services
async def warmup_check():
    """
    Warm-up endpoint that initializes the RAG pipeline.
    
    Call this endpoint after deployment to pre-initialize the pipeline
    and eliminate cold start delays for the first user query.
    
    Supports both GET and HEAD requests for compatibility with monitoring services.
    
    This endpoint can be called by:
    - Render health checks
    - Cron jobs
    - External monitoring services (including those using HEAD method)
    """
    try:
        from ...core.rag import get_rag_pipeline
        
        # Force pipeline initialization
        pipeline = get_rag_pipeline()
        
        # Verify pipeline is actually ready by checking vector store
        pipeline_ready = pipeline.vector_store is not None
        
        # FastAPI automatically handles HEAD requests (returns empty body)
        # But pipeline initialization still happens, which is what we want for warm-up
        return {
            "status": "warmed_up" if pipeline_ready else "warming",
            "pipeline_initialized": pipeline_ready,
            "message": "RAG pipeline is ready" if pipeline_ready else "Pipeline initialization in progress",
        }
    except Exception as e:
        return {
            "status": "error",
            "pipeline_initialized": False,
            "error": str(e),
        }