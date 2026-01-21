"""
Kill switch service for quickly disabling/enabling the system.

Uses Redis for fast state checks, with database fallback for persistence.
"""

import logging
from typing import Optional
from datetime import datetime

try:
    import redis
    from redis.exceptions import RedisError, ConnectionError as RedisConnectionError
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False
    redis = None

from ..utils.config import settings
from .cache import get_redis_client

logger = logging.getLogger(__name__)

# Redis key for kill switch state
KILL_SWITCH_KEY = "system:kill_switch:enabled"
KILL_SWITCH_MESSAGE_KEY = "system:kill_switch:message"


def is_kill_switch_enabled() -> bool:
    """
    Check if kill switch is enabled (system disabled).
    
    Returns:
        True if system is disabled, False if enabled
    """
    # Try Redis first (fastest)
    client = get_redis_client()
    if client:
        try:
            enabled = client.get(KILL_SWITCH_KEY)
            if enabled is not None:
                return enabled.lower() == "true"
        except (RedisError, Exception) as e:
            logger.warning(f"Error reading kill switch from Redis: {e}. Checking database.")
    
    # Fallback to database
    try:
        from ..services.database import get_db_context
        from sqlalchemy import text
        
        with get_db_context() as db:
            # Check if kill_switch_settings table exists
            result = db.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'kill_switch_settings'
                )
            """))
            table_exists = result.scalar()
            
            if table_exists:
                result = db.execute(text("""
                    SELECT enabled FROM kill_switch_settings 
                    ORDER BY updated_at DESC 
                    LIMIT 1
                """))
                enabled = result.scalar()
                if enabled is not None:
                    return bool(enabled)
    except Exception as e:
        logger.warning(f"Error reading kill switch from database: {e}")
    
    # Default: system is enabled (kill switch is off)
    return False


def get_kill_switch_message() -> Optional[str]:
    """
    Get custom message for kill switch (if system is disabled).
    
    Returns:
        Custom message or None
    """
    # Try Redis first
    client = get_redis_client()
    if client:
        try:
            message = client.get(KILL_SWITCH_MESSAGE_KEY)
            if message:
                return message
        except (RedisError, Exception) as e:
            logger.warning(f"Error reading kill switch message from Redis: {e}")
    
    # Fallback to database
    try:
        from ..services.database import get_db_context
        from sqlalchemy import text
        
        with get_db_context() as db:
            result = db.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'kill_switch_settings'
                )
            """))
            table_exists = result.scalar()
            
            if table_exists:
                result = db.execute(text("""
                    SELECT message FROM kill_switch_settings 
                    ORDER BY updated_at DESC 
                    LIMIT 1
                """))
                message = result.scalar()
                if message:
                    return message
    except Exception as e:
        logger.warning(f"Error reading kill switch message from database: {e}")
    
    return None


def set_kill_switch(enabled: bool, message: Optional[str] = None, user_id: Optional[str] = None) -> bool:
    """
    Set kill switch state.
    
    Args:
        enabled: True to disable system, False to enable
        message: Optional custom message to show when disabled
        user_id: Optional user ID who triggered the change
        
    Returns:
        True if successful, False otherwise
    """
    success = False
    
    # Update Redis (fastest)
    client = get_redis_client()
    if client:
        try:
            client.set(KILL_SWITCH_KEY, str(enabled).lower())
            if message:
                client.set(KILL_SWITCH_MESSAGE_KEY, message)
            else:
                client.delete(KILL_SWITCH_MESSAGE_KEY)
            success = True
            logger.info(f"Kill switch updated in Redis: enabled={enabled}")
        except (RedisError, Exception) as e:
            logger.warning(f"Error updating kill switch in Redis: {e}")
    
    # Update database (persistence)
    try:
        from ..services.database import get_db_context
        from sqlalchemy import text
        
        with get_db_context() as db:
            # Create table if it doesn't exist
            db.execute(text("""
                CREATE TABLE IF NOT EXISTS kill_switch_settings (
                    id SERIAL PRIMARY KEY,
                    enabled BOOLEAN NOT NULL DEFAULT FALSE,
                    message TEXT,
                    updated_by VARCHAR(255),
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            
            # Insert new setting
            db.execute(text("""
                INSERT INTO kill_switch_settings (enabled, message, updated_by, updated_at)
                VALUES (:enabled, :message, :updated_by, CURRENT_TIMESTAMP)
            """), {
                "enabled": enabled,
                "message": message,
                "updated_by": user_id
            })
            
            success = True
            logger.info(f"Kill switch updated in database: enabled={enabled}")
    except Exception as e:
        logger.error(f"Error accessing database for kill switch: {e}")
    
    return success


def get_kill_switch_status() -> dict:
    """
    Get current kill switch status.
    
    Returns:
        Dict with status information
    """
    enabled = is_kill_switch_enabled()
    message = get_kill_switch_message()
    
    return {
        "enabled": enabled,
        "system_disabled": enabled,
        "message": message or "System is currently disabled for maintenance. Please try again later.",
        "timestamp": datetime.utcnow().isoformat()
    }
