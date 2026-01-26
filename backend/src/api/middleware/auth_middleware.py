"""
Middleware to extract user info from JWT token and set in request.state for rate limiting.
"""

import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from ...api.routes.auth import verify_jwt_token
from fastapi.security import HTTPBearer

logger = logging.getLogger(__name__)
security = HTTPBearer(auto_error=False)


class AuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware to extract user_id from JWT token and set in request.state.
    This allows rate limiting to use user_id instead of IP when authenticated.
    """
    
    async def dispatch(self, request: Request, call_next):
        # Extract JWT token from Authorization header
        authorization = request.headers.get("Authorization")
        
        if authorization and authorization.startswith("Bearer "):
            token = authorization.split(" ")[1]
            user_info = verify_jwt_token(token)
            
            if user_info and user_info.get('user_id'):
                # Set user info in request.state for rate limiting and Sentry
                request.state.user_id = user_info.get('user_id')
                request.state.tenant_id = user_info.get('tenant_id')
                request.state.role = user_info.get('role')
                logger.debug(f"Set user info in request.state: user_id={user_info.get('user_id')}")
        
        response = await call_next(request)
        return response
