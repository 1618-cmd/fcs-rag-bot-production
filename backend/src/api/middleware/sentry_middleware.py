"""
Sentry middleware to add user context to error tracking.
"""

import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger(__name__)


class SentryUserContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add user context to Sentry for error tracking.
    
    Extracts user information from request.state (set by AuthMiddleware)
    and adds it to Sentry scope for better error tracking.
    """
    
    async def dispatch(self, request: Request, call_next):
        # Try to get user info from request.state (set by AuthMiddleware)
        user_id = getattr(request.state, 'user_id', None)
        tenant_id = getattr(request.state, 'tenant_id', None)
        role = getattr(request.state, 'role', None)
        
        # Add user context to Sentry if available
        if user_id:
            try:
                import sentry_sdk
                
                # Set user context in Sentry
                sentry_sdk.set_user({
                    "id": user_id,  # Use user_id, not email (privacy)
                    "tenant_id": tenant_id,
                    "role": role,
                    # Explicitly don't include email (privacy concern)
                })
                
                # Add tags for filtering
                if tenant_id:
                    sentry_sdk.set_tag("tenant_id", tenant_id)
                if role:
                    sentry_sdk.set_tag("user_role", role)
                
                logger.debug(f"Set Sentry user context: user_id={user_id}, tenant_id={tenant_id}")
            except ImportError:
                # Sentry not installed or not initialized
                pass
            except Exception as e:
                # Don't break request if Sentry fails
                logger.debug(f"Failed to set Sentry user context: {e}")
        
        response = await call_next(request)
        return response
