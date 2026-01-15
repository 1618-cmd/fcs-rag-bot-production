"""
Health check endpoints.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from ...utils.config import settings
from ...services.cache import get_cache_stats

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


def _warmup_logic():
    """
    Shared logic for warm-up endpoint (used by both GET and HEAD).
    Initializes the RAG pipeline and returns status.
    """
    try:
        from ...core.rag import get_rag_pipeline
        
        # Force pipeline initialization
        pipeline = get_rag_pipeline()
        
        # Verify pipeline is actually ready by checking vector store
        pipeline_ready = pipeline.vector_store is not None
        
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


@router.get("/health/warmup")
async def warmup_check_get():
    """
    Warm-up endpoint that initializes the RAG pipeline (GET method).
    
    Call this endpoint after deployment to pre-initialize the pipeline
    and eliminate cold start delays for the first user query.
    """
    return _warmup_logic()


@router.head("/health/warmup")
async def warmup_check_head():
    """
    Warm-up endpoint that initializes the RAG pipeline (HEAD method).
    
    Supports HEAD requests for monitoring services that use HEAD method.
    Pipeline initialization still happens even with HEAD requests.
    """
    # HEAD requests should still initialize the pipeline
    _warmup_logic()
    # Return empty response for HEAD (status 200 to indicate success)
    from fastapi import Response
    return Response(status_code=200)


@router.get("/health/cache")
async def cache_stats():
    """
    Get cache statistics.
    
    Returns information about Redis cache status and usage.
    """
    stats = get_cache_stats()
    return stats