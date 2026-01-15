"""
FastAPI application for Vena RAG Bot Production.

Main entry point for the API server.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..utils.config import settings, validate_settings
from ..utils.logging_config import setup_logging
from .routes import query, health

# Set up logging
setup_logging(log_level=settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown."""
    # Startup
    logger.info("Starting FCS RAG Bot API...")
    
    # Validate configuration
    if not validate_settings():
        logger.error("Configuration validation failed! Check your .env file.")
        raise ValueError("Invalid configuration")
    
    logger.info("Configuration validated successfully")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Qdrant URL: {settings.qdrant_url}")
    
    # Pre-initialize RAG pipeline to eliminate cold start delay
    # This ensures the first user doesn't wait 10-25 seconds for initialization
    # Wrapped in try/except to ensure API starts even if initialization fails
    # Qdrant client has a 30s timeout, so worst case is 30s delay on startup
    logger.info("Pre-initializing RAG pipeline (this may take a few seconds)...")
    try:
        from ..core.rag import get_rag_pipeline
        import time
        
        start_time = time.time()
        
        # Initialize pipeline synchronously (better than first user waiting)
        # Qdrant client already has 30s timeout configured, so this won't hang forever
        pipeline = get_rag_pipeline()
        
        init_time = time.time() - start_time
        logger.info(f"✅ RAG pipeline pre-initialized successfully in {init_time:.2f}s")
        
    except Exception as e:
        # If initialization fails, API still starts - pipeline will init on first query
        logger.warning(f"⚠️  RAG pipeline pre-initialization failed (will initialize on first query): {e}")
        logger.info("This is not critical - the API will still start and initialize on first query")
        # Don't re-raise - we want the API to start even if pipeline init fails
    
    yield
    
    # Shutdown
    logger.info("Shutting down FCS RAG Bot API...")


# Create FastAPI app
app = FastAPI(
    title="FCS RAG Bot API",
    description="RAG-based technical support system for Vena platform",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware (allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(query.router, prefix="/api", tags=["Query"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "FCS RAG Bot API",
        "version": "1.0.0",
        "docs": "/api/docs",
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )

