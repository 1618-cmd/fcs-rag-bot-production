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

from ...utils.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer(auto_error=False)

# JWT secret key (use environment variable or default)
JWT_SECRET_KEY = getattr(settings, 'jwt_secret_key', 'your-secret-key-change-in-production')
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# Admin credentials from environment (simple auth, no database)
ADMIN_EMAIL = getattr(settings, 'admin_email', 'admin@example.com')
ADMIN_PASSWORD = getattr(settings, 'admin_password', 'admin')


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


def create_jwt_token(email: str) -> str:
    """Create JWT token for authenticated user."""
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def verify_jwt_token(token: str) -> Optional[str]:
    """Verify JWT token and return email if valid."""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload.get('email')
    except jwt.ExpiredSignatureError:
        logger.warning("JWT token expired")
        return None
    except jwt.InvalidTokenError:
        logger.warning("Invalid JWT token")
        return None


async def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[str]:
    """Get current authenticated user from JWT token."""
    if not credentials:
        return None
    
    token = credentials.credentials
    return verify_jwt_token(token)


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Login endpoint for admin users.
    
    Validates credentials and returns JWT token.
    """
    # Validate credentials (simple check against environment variables)
    if request.email == ADMIN_EMAIL and request.password == ADMIN_PASSWORD:
        token = create_jwt_token(request.email)
        logger.info(f"User logged in: {request.email}")
        return LoginResponse(
            success=True,
            token=token,
            message="Login successful"
        )
    else:
        logger.warning(f"Failed login attempt for email: {request.email}")
        raise HTTPException(status_code=401, detail="Invalid email or password")


@router.get("/status", response_model=AuthStatus)
async def auth_status(current_user: Optional[str] = Depends(get_current_user)):
    """
    Check authentication status.
    
    Returns whether user is authenticated and their email.
    """
    return AuthStatus(
        authenticated=current_user is not None,
        email=current_user
    )


@router.post("/logout")
async def logout():
    """
    Logout endpoint (client-side token removal).
    
    Note: JWT tokens are stateless, so logout is handled client-side by removing the token.
    """
    return {"success": True, "message": "Logout successful. Please remove token client-side."}
