"""
Query endpoints for RAG queries.
"""

import time
import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ...core.rag import get_rag_pipeline
from ...utils.config import settings
from ...services.cache import get_cached_response, cache_response

logger = logging.getLogger(__name__)
router = APIRouter()


class QueryRequest(BaseModel):
    """Request model for RAG query."""
    question: str = Field(..., description="The question to ask", min_length=1, max_length=10000)  # Increased to support long code snippets
    top_k: Optional[int] = Field(None, description="Number of documents to retrieve (default: 5)", ge=1, le=10)
    skip_cache: bool = Field(default=False, description="Skip cache and force fresh response")


class Source(BaseModel):
    """Source document model."""
    name: str
    content: Optional[str] = None


class QueryResponse(BaseModel):
    """Response model for RAG query."""
    answer: str
    sources: List[Source]
    latency_ms: float
    model: str


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Query the RAG system.
    
    Takes a question and returns an answer with source citations.
    """
    start_time = time.time()
    
    try:
        # Check cache first (unless skip_cache is True)
        if not request.skip_cache:
            cached_response = get_cached_response(request.question)
            if cached_response:
                # Return cached response (much faster!)
                logger.info(f"Returning cached response (saved {cached_response.get('latency_ms', 0)}ms)")
                return QueryResponse(**cached_response)
        else:
            logger.info("Skipping cache (skip_cache=True)")
        
        # Cache miss - process query
        # Get RAG pipeline
        pipeline = get_rag_pipeline()
        
        # Query the pipeline (async version for better performance)
        # Falls back to sync if async fails
        logger.info(f"Processing query: {request.question[:100]}...")
        try:
            response, documents = await pipeline.query_async(request.question)
        except Exception as async_error:
            logger.warning(f"Async query failed, falling back to sync: {async_error}")
            # Fallback to synchronous version if async fails
            response, documents = pipeline.query(request.question)
        
        # Check if the response indicates a refusal (missing information)
        # If the LLM refused to answer, don't include sources
        refusal_indicators = [
            "do not contain sufficient information",
            "context documents do not contain",
            "does not contain information",
            "would need documentation",
            "insufficient information to answer"
        ]
        
        is_refusal = any(indicator.lower() in response.lower() for indicator in refusal_indicators)
        
        # Extract sources only if not a refusal
        if is_refusal:
            logger.info("Response indicates refusal - excluding sources")
            sources = []
        else:
            source_names = pipeline.get_sources(documents)
            sources = [Source(name=name) for name in source_names]
        
        # Calculate latency
        latency_ms = (time.time() - start_time) * 1000
        
        logger.info(f"Query completed in {latency_ms:.2f}ms")
        
        # Build response
        query_response = QueryResponse(
            answer=response,
            sources=sources,
            latency_ms=round(latency_ms, 2),
            model=settings.openai_model,
        )
        
        # Cache the response for future queries
        cache_response(request.question, query_response.dict())
        
        return query_response
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing query: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

