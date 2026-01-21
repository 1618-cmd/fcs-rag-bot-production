"""
Query logging service for analytics and GDPR compliance.

Logs queries to database in a non-blocking, safe manner.
Never blocks or breaks queries if logging fails.
"""

import logging
from typing import Optional, List
from datetime import datetime
from fastapi import Request

from ..models.database import QueryLog
from ..services.database import get_db_context
from ..utils.config import settings

logger = logging.getLogger(__name__)


def log_query_async(
    request: Request,
    question: str,
    answer: str,
    sources: List[str],
    latency_ms: float,
    was_cached: bool = False,
    was_refusal: bool = False,
    refusal_reason: Optional[str] = None,
    calc_script: Optional[str] = None
) -> None:
    """
    Log query to database in background (non-blocking).
    
    This function is designed to be fire-and-forget. It never raises exceptions
    and never blocks the main request flow.
    
    Args:
        request: FastAPI Request object (contains user info in request.state)
        question: User's question
        answer: Bot's response
        sources: List of source document names
        latency_ms: Response time in milliseconds
        was_cached: Whether response came from cache
        was_refusal: Whether bot refused to answer
        refusal_reason: Reason for refusal (if applicable)
        calc_script: Optional calc script that was analyzed
    """
    # Only log if database is configured
    if not settings.database_url:
        return
    
    # Extract user info from request.state (set by AuthMiddleware)
    user_id = getattr(request.state, 'user_id', None)
    tenant_id = getattr(request.state, 'tenant_id', None)
    user_email = None
    
    # If no tenant_id from JWT, use default
    if not tenant_id:
        tenant_id = "default"
    
    # Try to get user email if available (optional)
    try:
        # Could query database for email, but that's another DB call
        # For now, just use None - can be populated later if needed
        pass
    except Exception:
        pass
    
    # Build full question text (include calc script if provided)
    full_question = question
    if calc_script:
        full_question = f"Calc Script Analysis:\n{calc_script}\n\nQuestion: {question}"
    
    # Truncate answer preview (first 200 chars)
    answer_preview = answer[:200] if answer else None
    
    # Prepare sources list (JSON array)
    sources_list = sources if sources else []
    sources_count = len(sources_list)
    
    # Log in background (fire-and-forget)
    try:
        with get_db_context() as db:
            query_log = QueryLog(
                tenant_id=tenant_id,
                user_id=user_id,
                user_email=user_email,
                question=full_question,
                answer_preview=answer_preview,
                answer_full=answer,  # Store full answer for search
                sources_count=sources_count,
                sources_list=sources_list,
                latency_ms=latency_ms,
                was_cached=was_cached,
                was_refusal=was_refusal,
                refusal_reason=refusal_reason,
                created_at=datetime.utcnow()
            )
            db.add(query_log)
            db.commit()
            logger.debug(f"Query logged successfully: user_id={user_id}, tenant_id={tenant_id}")
    except Exception as e:
        # Never raise - logging failures should never break queries
        logger.warning(f"Query logging failed (non-critical): {e}")
        # Could optionally log to Sentry here, but don't raise
