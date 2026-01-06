"""
Pydantic schemas for API requests and responses.

These models define the structure of data sent to and received from the API.
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


# Query schemas (also defined in routes, but kept here for reference)
class QueryRequest(BaseModel):
    """Request model for RAG query."""
    question: str = Field(..., description="The question to ask", min_length=1, max_length=1000)
    top_k: Optional[int] = Field(None, description="Number of documents to retrieve", ge=1, le=10)


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


# Analytics schemas (for future use)
class QueryLog(BaseModel):
    """Query log entry model."""
    id: Optional[int] = None
    question: str
    answer: str
    sources: List[str]
    latency_ms: float
    timestamp: datetime
    user_id: Optional[str] = None


class AnalyticsResponse(BaseModel):
    """Analytics response model."""
    total_queries: int
    average_latency_ms: float
    top_questions: List[str]

