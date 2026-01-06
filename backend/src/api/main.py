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

