"""
Authentication endpoints for admin login.
"""

import logging
import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from ...utils.config import settings
from ...services.database import get_db
from ...models.database import User
from ...services.rate_limiter import limit_login

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer(auto_error=False)

# JWT secret key (use environment variable or default)
JWT_SECRET_KEY = getattr(settings, 'jwt_secret_key', 'your-secret-key-change-in-production')
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# Fallback admin credentials from environment (for initial setup)
ADMIN_EMAIL = getattr(settings, 'admin_email', 'admin@example.com')
ADMIN_PASSWORD = getattr(settings, 'admin_password', 'admin')
ALLOW_FALLBACK_ADMIN_LOGIN = getattr(settings, 'allow_fallback_admin_login', False)


class LoginRequest(BaseModel):
    """Login request model."""
    email: str
    password: str


class LoginResponse(BaseModel):
    """Login response model."""
    success: bool
    token: str
    message: str


class AuthStatus(BaseModel):
    """Authentication status model."""
    authenticated: bool
    email: Optional[str] = None
    role: Optional[str] = None
    user_id: Optional[str] = None


def create_jwt_token(user_id: str, email: str, tenant_id: str, role: str) -> str:
    """Create JWT token for authenticated user."""
    payload = {
        'user_id': user_id,
        'email': email,
        'tenant_id': tenant_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def verify_jwt_token(token: str) -> Optional[dict]:
    """Verify JWT token and return user info if valid."""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return {
            'user_id': payload.get('user_id'),
            'email': payload.get('email'),
            'tenant_id': payload.get('tenant_id'),
            'role': payload.get('role')
        }
    except jwt.ExpiredSignatureError:
        logger.warning("JWT token expired")
        return None
    except jwt.InvalidTokenError:
        logger.warning("Invalid JWT token")
        return None


async def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[str]:
    """Get current authenticated user ID from JWT token.

    Note: Kept for backwards compatibility with existing routes that only need the user_id.
    Prefer get_current_user_info for role-aware authorization.
    """
    if not credentials:
        return None
    
    token = credentials.credentials
    token_data = verify_jwt_token(token)
    return token_data.get('user_id') if token_data else None


async def get_current_user_info(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Optional[dict]:
    """Get current authenticated user info (user_id/email/tenant_id/role) from JWT token."""
    if not credentials:
        return None
    token = credentials.credentials
    return verify_jwt_token(token)


@router.post("/login", response_model=LoginResponse)
@limit_login()
async def login(http_request: Request, request: LoginRequest):
    """
    Login endpoint for users.
    
    Validates credentials against database (or fallback to env vars for initial setup).
    """
    # Try database first (if available)
    try:
        from ...services.database import get_db_context
        with get_db_context() as db:
            user = db.query(User).filter(User.email == request.email).first()
            
            if user:
                # Database user - verify password
                if not user.is_active:
                    raise HTTPException(status_code=403, detail="User account is inactive")
                
                # Check password
                from .users import verify_password
                if user.password_hash and verify_password(request.password, user.password_hash):
                    token = create_jwt_token(user.id, user.email, user.tenant_id, user.role)
                    logger.info(f"User logged in: {request.email} (role: {user.role})")
                    return LoginResponse(
                        success=True,
                        token=token,
                        message="Login successful"
                    )
                else:
                    logger.warning(f"Failed login attempt for email: {request.email} (invalid password)")
                    raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        # Database not available or error - fall through to fallback
        logger.debug(f"Database check failed (using fallback): {e}")
        pass
    
    # Fallback to environment variables (for initial setup before database is populated)
    # Best practice: keep this disabled in production unless explicitly enabled.
    if ALLOW_FALLBACK_ADMIN_LOGIN and request.email == ADMIN_EMAIL and request.password == ADMIN_PASSWORD:
        # Create a temporary token (user_id will be email for fallback)
        token = create_jwt_token(ADMIN_EMAIL, ADMIN_EMAIL, "default", "admin")
        logger.info(f"Fallback login (env vars): {request.email}")
        return LoginResponse(
            success=True,
            token=token,
            message="Login successful (using fallback credentials)"
        )
    
    logger.warning(f"Failed login attempt for email: {request.email}")
    raise HTTPException(status_code=401, detail="Invalid email or password")


@router.get("/status", response_model=AuthStatus)
async def auth_status(user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Check authentication status.
    
    Returns whether user is authenticated and their email.
    """
    return AuthStatus(
        authenticated=user_info is not None,
        email=(user_info.get("email") if user_info else None),
        role=(user_info.get("role") if user_info else None),
        user_id=(user_info.get("user_id") if user_info else None),
    )


@router.post("/logout")
async def logout():
    """
    Logout endpoint (client-side token removal).
    
    Note: JWT tokens are stateless, so logout is handled client-side by removing the token.
    """
    return {"success": True, "message": "Logout successful. Please remove token client-side."}
