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

logger = logging.getLogger(__name__)
router = APIRouter()


class QueryRequest(BaseModel):
    """Request model for RAG query."""
    question: str = Field(..., description="The question to ask", min_length=1, max_length=1000)
    top_k: Optional[int] = Field(None, description="Number of documents to retrieve (default: 5)", ge=1, le=10)


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
        # Get RAG pipeline
        pipeline = get_rag_pipeline()
        
        # Query the pipeline
        logger.info(f"Processing query: {request.question[:100]}...")
        response, documents = pipeline.query(request.question)
        
        # Extract sources
        source_names = pipeline.get_sources(documents)
        sources = [Source(name=name) for name in source_names]
        
        # Calculate latency
        latency_ms = (time.time() - start_time) * 1000
        
        logger.info(f"Query completed in {latency_ms:.2f}ms")
        
        return QueryResponse(
            answer=response,
            sources=sources,
            latency_ms=round(latency_ms, 2),
            model=settings.openai_model,
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing query: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

