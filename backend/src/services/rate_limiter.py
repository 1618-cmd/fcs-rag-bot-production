"""
Rate limiting service using slowapi with Redis backend.

Provides distributed rate limiting that works across multiple instances.
"""

import logging
from typing import Optional, Callable
from fastapi import Request, HTTPException, status
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from ..utils.config import settings
from ..services.cache import get_redis_client

logger = logging.getLogger(__name__)

# Create limiter instance
# Use Redis if available, otherwise fallback to in-memory (not recommended for production)
_limiter = None


def get_limiter_key(request: Request) -> str:
    """
    Get rate limit key based on user authentication or IP address.
    
    Priority:
    1. Authenticated user: use user_id from JWT token
    2. Fallback: use IP address
    
    Args:
        request: FastAPI request object
        
    Returns:
        String key for rate limiting
    """
    # Try to get user_id from JWT token (if authenticated)
    try:
        # Check if user info is in request state (set by auth middleware)
        if hasattr(request.state, 'user_id') and request.state.user_id:
            user_id = request.state.user_id
            logger.debug(f"Rate limiting by user_id: {user_id}")
            return f"user:{user_id}"
    except Exception as e:
        logger.debug(f"Could not get user_id from request state: {e}")
    
    # Fallback to IP address
    ip_address = get_remote_address(request)
    logger.debug(f"Rate limiting by IP: {ip_address}")
    return f"ip:{ip_address}"


def get_limiter() -> Limiter:
    """
    Get or create rate limiter instance.
    Uses Redis if available, otherwise in-memory (not recommended for production).
    
    Returns:
        Limiter instance
    """
    global _limiter
    
    if _limiter is not None:
        return _limiter
    
    # Get Redis client for distributed rate limiting
    redis_client = get_redis_client()
    
    if redis_client and settings.rate_limit_enabled:
        # Use Redis for distributed rate limiting (recommended for production)
        try:
            _limiter = Limiter(
                key_func=get_limiter_key,
                storage_uri=settings.redis_url,
                default_limits=[]  # No default limits - apply per endpoint
            )
            logger.info("Rate limiter initialized with Redis backend")
        except Exception as e:
            logger.warning(f"Failed to initialize Redis-backed rate limiter: {e}. Using in-memory fallback.")
            _limiter = Limiter(
                key_func=get_limiter_key,
                default_limits=[]  # No default limits - apply per endpoint
            )
    else:
        if not settings.rate_limit_enabled:
            logger.info("Rate limiting is disabled in configuration")
            # Return a no-op limiter
            _limiter = Limiter(
                key_func=get_limiter_key,
                default_limits=[],
                storage_uri="memory://"  # In-memory storage
            )
        else:
            logger.warning("Redis not available - using in-memory rate limiter (not recommended for production)")
            # Fallback to in-memory (works but not distributed)
            _limiter = Limiter(
                key_func=get_limiter_key,
                default_limits=[]  # No default limits - apply per endpoint
            )
    
    return _limiter


def create_rate_limit_decorator(limit: str, per: str = "minute") -> Callable:
    """
    Create a rate limit decorator with specified limit.
    
    Args:
        limit: Number of requests allowed
        per: Time period (minute, hour, day)
        
    Returns:
        Decorator function
    """
    limiter = get_limiter()
    
    if not settings.rate_limit_enabled:
        # Return no-op decorator if rate limiting is disabled
        def noop_decorator(func):
            return func
        return noop_decorator
    
    # Create rate limit string (e.g., "20/minute", "5/hour")
    rate_limit_str = f"{limit}/{per}"
    
    return limiter.limit(rate_limit_str)


# Convenience decorators for common rate limits
def limit_query() -> Callable:
    """Rate limit decorator for query endpoints (20/minute)."""
    return create_rate_limit_decorator(
        str(settings.rate_limit_query_per_minute),
        "minute"
    )


def limit_login() -> Callable:
    """Rate limit decorator for login endpoints (5/minute)."""
    return create_rate_limit_decorator(
        str(settings.rate_limit_login_per_minute),
        "minute"
    )


def limit_user_management() -> Callable:
    """Rate limit decorator for user management endpoints (10/minute)."""
    return create_rate_limit_decorator(
        str(settings.rate_limit_user_management_per_minute),
        "minute"
    )


def limit_admin() -> Callable:
    """Rate limit decorator for admin endpoints (30/minute)."""
    return create_rate_limit_decorator("30", "minute")


# Custom exception handler for rate limit errors
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    """
    Custom handler for rate limit exceeded errors.
    Returns proper HTTP 429 response with retry-after header.
    """
    from fastapi.responses import JSONResponse
    
    # Extract limit information from exception detail
    # exc.detail format is usually like "20 per 1 minute" or "5 per 1 minute"
    limit_detail = str(exc.detail) if exc.detail else "rate limit"
    
    # Calculate retry after in seconds (default to 60 if not provided)
    retry_after_seconds = exc.retry_after if exc.retry_after else 60
    
    # Format user-friendly message
    message = (
        f"Rate limit exceeded. You have made too many requests ({limit_detail}). "
        f"Please wait {retry_after_seconds} seconds before trying again."
    )
    
    response = JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "error": "Rate limit exceeded",
            "message": message,
            "detail": limit_detail,
            "retry_after": retry_after_seconds
        },
        headers={"Retry-After": str(retry_after_seconds)}
    )
    return response
