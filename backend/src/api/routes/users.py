"""
User management endpoints for creating, updating, and managing users with roles.
"""

import logging
import uuid
import bcrypt
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from ...models.database import User, Tenant
from ...services.database import get_db
from .auth import get_current_user
from ...services.rate_limiter import limit_user_management

logger = logging.getLogger(__name__)
router = APIRouter()


# Role definitions
ROLES = {
    'admin': {
        'permissions': ['*'],  # All permissions
        'description': 'Full system access, can manage users, approve documents, run ingestion'
    },
    'modeler': {
        'permissions': ['query', 'upload', 'view_queries', 'view_analytics', 'approve_documents'],
        'description': 'Can upload documents, approve/reject, view queries and analytics'
    },
    'contributor': {
        'permissions': ['query', 'upload', 'view_own_queries'],
        'description': 'Can query bot and upload documents, view own query history'
    },
    'viewer': {
        'permissions': ['query', 'view_own_queries'],
        'description': 'Read-only access, can query bot and view own history'
    }
}


def has_permission(user_role: str, permission: str) -> bool:
    """Check if role has permission."""
    role_config = ROLES.get(user_role, {})
    role_perms = role_config.get('permissions', [])
    return '*' in role_perms or permission in role_perms


def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """Verify password against hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
    """Get user by ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get user by email."""
    return db.query(User).filter(User.email == email).first()


def get_user_role(db: Session, user_id: str) -> Optional[str]:
    """Get user's role."""
    user = get_user_by_id(db, user_id)
    return user.role if user else None


def is_admin(db: Session, user_id: str) -> bool:
    """Check if user is admin."""
    return get_user_role(db, user_id) == 'admin'


# Request/Response Models
class CreateUserRequest(BaseModel):
    """Request model for creating a user."""
    email: EmailStr
    password: Optional[str] = None  # Optional if using external auth
    full_name: Optional[str] = None
    role: str = 'viewer'  # Default role
    tenant_id: Optional[str] = None  # If not provided, uses current user's tenant


class UpdateUserRequest(BaseModel):
    """Request model for updating a user."""
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None


class AssignRoleRequest(BaseModel):
    """Request model for assigning a role."""
    role: str


class UserResponse(BaseModel):
    """User response model."""
    id: str
    email: str
    tenant_id: str
    role: str
    full_name: Optional[str]
    is_active: bool
    created_at: str
    
    class Config:
        from_attributes = True


@router.post("/users", response_model=UserResponse)
@limit_user_management()
async def create_user(
    http_request: Request,
    request: CreateUserRequest,
    db: Session = Depends(get_db),
    current_user: Optional[str] = Depends(get_current_user)
):
    """Create new user with role assignment. Requires 'manage_users' permission."""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # Get current user from database
    current_user_obj = get_user_by_id(db, current_user)
    if not current_user_obj:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check permission
    if not has_permission(current_user_obj.role, 'manage_users'):
        raise HTTPException(status_code=403, detail="Permission 'manage_users' required")
    
    # Use current user's tenant if not specified
    tenant_id = request.tenant_id or current_user_obj.tenant_id
    
    # Validate role
    if request.role not in ROLES:
        raise HTTPException(status_code=400, detail=f"Invalid role: {request.role}. Valid roles: {', '.join(ROLES.keys())}")
    
    # Check if email already exists
    existing = get_user_by_email(db, request.email)
    if existing:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    # Create user
    new_user = User(
        id=str(uuid.uuid4()),
        email=request.email,
        tenant_id=tenant_id,
        role=request.role,
        full_name=request.full_name,
        password_hash=hash_password(request.password) if request.password else None,
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    logger.info(f"User created: {request.email} with role {request.role} by {current_user}")
    
    return UserResponse(
        id=new_user.id,
        email=new_user.email,
        tenant_id=new_user.tenant_id,
        role=new_user.role,
        full_name=new_user.full_name,
        is_active=new_user.is_active,
        created_at=new_user.created_at.isoformat() if new_user.created_at else ""
    )


@router.get("/users", response_model=List[UserResponse])
@limit_user_management()
async def list_users(
    http_request: Request,
    db: Session = Depends(get_db),
    current_user: Optional[str] = Depends(get_current_user)
):
    """List all users in current user's tenant. Requires 'manage_users' permission."""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    current_user_obj = get_user_by_id(db, current_user)
    if not current_user_obj:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check permission
    if not has_permission(current_user_obj.role, 'manage_users'):
        raise HTTPException(status_code=403, detail="Permission 'manage_users' required")
    
    # Get users in same tenant
    users = db.query(User).filter(User.tenant_id == current_user_obj.tenant_id).all()
    
    return [
        UserResponse(
            id=user.id,
            email=user.email,
            tenant_id=user.tenant_id,
            role=user.role,
            full_name=user.full_name,
            is_active=user.is_active,
            created_at=user.created_at.isoformat() if user.created_at else ""
        )
        for user in users
    ]


@router.put("/users/{user_id}/role")
@limit_user_management()
async def assign_role(
    http_request: Request,
    user_id: str,
    request: AssignRoleRequest,
    db: Session = Depends(get_db),
    current_user: Optional[str] = Depends(get_current_user)
):
    """Assign role to user (same tenant only). Requires 'assign_roles' permission."""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    current_user_obj = get_user_by_id(db, current_user)
    if not current_user_obj:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check permission
    if not has_permission(current_user_obj.role, 'assign_roles'):
        raise HTTPException(status_code=403, detail="Permission 'assign_roles' required")
    
    # Get target user
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == current_user_obj.tenant_id  # Same tenant only
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Validate role
    if request.role not in ROLES:
        raise HTTPException(status_code=400, detail=f"Invalid role: {request.role}")
    
    # Update role
    user.role = request.role
    db.commit()
    
    logger.info(f"Role '{request.role}' assigned to user {user.email} by {current_user}")
    
    return {"success": True, "message": f"Role '{request.role}' assigned to user"}


@router.put("/users/{user_id}", response_model=UserResponse)
@limit_user_management()
async def update_user(
    http_request: Request,
    user_id: str,
    request: UpdateUserRequest,
    db: Session = Depends(get_db),
    current_user: Optional[str] = Depends(get_current_user)
):
    """Update user information. Requires 'manage_users' permission."""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    current_user_obj = get_user_by_id(db, current_user)
    if not current_user_obj:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check permission
    if not has_permission(current_user_obj.role, 'manage_users'):
        raise HTTPException(status_code=403, detail="Permission 'manage_users' required")
    
    # Get target user (same tenant only)
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == current_user_obj.tenant_id
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update fields
    if request.full_name is not None:
        user.full_name = request.full_name
    if request.is_active is not None:
        user.is_active = request.is_active
    if request.role is not None:
        if request.role not in ROLES:
            raise HTTPException(status_code=400, detail=f"Invalid role: {request.role}")
        user.role = request.role
    
    db.commit()
    db.refresh(user)
    
    return UserResponse(
        id=user.id,
        email=user.email,
        tenant_id=user.tenant_id,
        role=user.role,
        full_name=user.full_name,
        is_active=user.is_active,
        created_at=user.created_at.isoformat() if user.created_at else ""
    )


@router.delete("/users/{user_id}")
@limit_user_management()
async def delete_user(
    http_request: Request,
    user_id: str,
    db: Session = Depends(get_db),
    current_user: Optional[str] = Depends(get_current_user)
):
    """Delete user (soft delete - set is_active=False). Requires 'manage_users' permission."""
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    current_user_obj = get_user_by_id(db, current_user)
    if not current_user_obj:
        raise HTTPException(status_code=401, detail="User not found")
    
    # Check permission
    if not has_permission(current_user_obj.role, 'manage_users'):
        raise HTTPException(status_code=403, detail="Permission 'manage_users' required")
    
    # Get target user (same tenant only)
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == current_user_obj.tenant_id
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Soft delete
    user.is_active = False
    db.commit()
    
    logger.info(f"User {user.email} deactivated by {current_user}")
    
    return {"success": True, "message": "User deactivated"}
