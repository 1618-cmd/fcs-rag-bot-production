"""
Redis caching service for query responses.
"""

import json
import hashlib
import re
import logging
from typing import Optional, Dict, Any
from datetime import datetime, timedelta

try:
    import redis
    from redis.exceptions import RedisError, ConnectionError as RedisConnectionError
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False
    redis = None

from ..utils.config import settings

logger = logging.getLogger(__name__)

# Global Redis client (singleton)
_redis_client = None


def get_redis_client():
    """Get or create Redis client (singleton)."""
    global _redis_client
    
    if not REDIS_AVAILABLE:
        logger.warning("Redis not available - caching disabled")
        return None
    
    if _redis_client is None:
        if not settings.redis_url:
            logger.warning("REDIS_URL not configured - caching disabled")
            return None
        
        try:
            _redis_client = redis.from_url(
                settings.redis_url,
                decode_responses=True,  # Automatically decode responses to strings
                socket_connect_timeout=5,  # 5 second connection timeout
                socket_timeout=5,  # 5 second socket timeout
                retry_on_timeout=True,
                health_check_interval=30,  # Check connection health every 30 seconds
            )
            # Test connection
            _redis_client.ping()
            logger.info("Redis client connected successfully")
        except (RedisConnectionError, RedisError) as e:
            logger.warning(f"Failed to connect to Redis: {e}. Caching disabled.")
            _redis_client = None
    
    return _redis_client


def normalize_question(question: str) -> str:
    """
    Normalize question for consistent cache key generation.
    Handles spacing variations, punctuation, and case differences.
    
    Args:
        question: User question string
        
    Returns:
        Normalized question string
    """
    # Convert to lowercase
    normalized = question.lower()
    
    # Normalize whitespace: multiple spaces/tabs/newlines → single space
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Remove leading/trailing whitespace
    normalized = normalized.strip()
    
    return normalized


def get_prompt_version() -> str:
    """
    Get current prompt version hash.
    This changes when SYSTEM_PROMPT or USER_PROMPT changes,
    automatically invalidating old cache entries.
    
    Returns:
        Short hash of current prompts (first 8 chars of MD5)
    """
    try:
        from ..core.rag import SYSTEM_PROMPT, USER_PROMPT
        # Combine both prompts and hash them
        prompt_content = f"{SYSTEM_PROMPT}{USER_PROMPT}"
        prompt_hash = hashlib.md5(prompt_content.encode('utf-8')).hexdigest()
        # Return first 8 characters for shorter cache keys
        return prompt_hash[:8]
    except Exception as e:
        logger.warning(f"Could not get prompt version: {e}. Using default.")
        return "default"


def get_cache_key(question: str, include_version: bool = True) -> str:
    """
    Generate cache key from question with optional versioning.
    
    Args:
        question: User question string
        include_version: Whether to include prompt version in cache key (default: True)
        
    Returns:
        Cache key string
    """
    # Normalize question (handles spacing, case, punctuation variations)
    normalized = normalize_question(question)
    
    # Generate MD5 hash of normalized question
    hash_value = hashlib.md5(normalized.encode('utf-8')).hexdigest()
    
    # Include prompt version to auto-invalidate on prompt changes
    if include_version:
        version = get_prompt_version()
        return f"rag:query:v{version}:{hash_value}"
    else:
        return f"rag:query:{hash_value}"


def get_cached_response(question: str) -> Optional[Dict[str, Any]]:
    """
    Get cached response if exists.
    
    Args:
        question: User question string
        
    Returns:
        Cached response dict or None if not found/expired
    """
    client = get_redis_client()
    if not client:
        return None
    
    try:
        cache_key = get_cache_key(question)
        cached_data = client.get(cache_key)
        
        if cached_data:
            try:
                response = json.loads(cached_data)
                logger.info(f"Cache hit for query: {question[:50]}...")
                return response
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to decode cached response: {e}")
                # Delete corrupted cache entry
                client.delete(cache_key)
                return None
        else:
            logger.info(f"Cache miss for query: {question[:50]}...")
            return None
            
    except (RedisError, Exception) as e:
        logger.warning(f"Error reading from cache: {e}. Continuing without cache.")
        return None


def cache_response(question: str, response: Dict[str, Any], ttl_seconds: Optional[int] = None):
    """
    Cache response.
    
    Args:
        question: User question string
        response: Response dict to cache
        ttl_seconds: Time to live in seconds (defaults to settings.cache_ttl)
    """
    client = get_redis_client()
    if not client:
        return
    
    try:
        cache_key = get_cache_key(question)
        ttl = ttl_seconds or settings.cache_ttl
        
        # Serialize response to JSON
        cached_data = json.dumps(response)
        
        # Store with TTL
        client.setex(cache_key, ttl, cached_data)
        logger.info(f"Cached response for query: {question[:50]}... (TTL: {ttl}s)")
        
    except (RedisError, Exception) as e:
        logger.warning(f"Error writing to cache: {e}. Continuing without cache.")


def clear_cache(pattern: str = "rag:query:*"):
    """
    Clear cache entries matching pattern.
    
    Args:
        pattern: Redis key pattern (default: all query caches)
    """
    client = get_redis_client()
    if not client:
        logger.warning("Cannot clear cache - Redis not available")
        return
    
    try:
        keys = client.keys(pattern)
        if keys:
            deleted = client.delete(*keys)
            logger.info(f"Cleared {deleted} cache entries matching pattern: {pattern}")
        else:
            logger.info(f"No cache entries found matching pattern: {pattern}")
    except (RedisError, Exception) as e:
        logger.error(f"Error clearing cache: {e}")


def get_cache_stats() -> Dict[str, Any]:
    """
    Get cache statistics.
    
    Returns:
        Dict with cache stats
    """
    client = get_redis_client()
    if not client:
        return {
            "enabled": False,
            "message": "Redis not available"
        }
    
    try:
        # Count cache keys (matches both old format and new versioned format)
        cache_keys = client.keys("rag:query:*")
        key_count = len(cache_keys)
        
        # Get Redis info
        info = client.info("memory")
        memory_used = info.get("used_memory_human", "unknown")
        
        return {
            "enabled": True,
            "cached_queries": key_count,
            "memory_used": memory_used,
            "ttl_seconds": settings.cache_ttl,
        }
    except (RedisError, Exception) as e:
        logger.error(f"Error getting cache stats: {e}")
        return {
            "enabled": True,
            "error": str(e)
        }
