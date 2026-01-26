# Query Logging Design for User Profiles & Multi-Tenancy

## Overview

Query logging is **essential** for:
1. **User Profiles** - Track individual user history, preferences, patterns
2. **Multi-Tenancy** - Isolate data per organization/tenant

## Database Schema Design

### User Table (PostgreSQL)

```python
class User(Base):
    __tablename__ = "users"
    
    # Primary Key
    id = Column(String, primary_key=True)  # UUID or email-based ID
    email = Column(String, unique=True, nullable=False, index=True)
    
    # Multi-Tenancy (CRITICAL)
    tenant_id = Column(String, nullable=False, index=True)  # Link to tenant/organization
    
    # Authentication
    password_hash = Column(String, nullable=True)  # Hashed password (if using local auth)
    is_active = Column(Boolean, default=True)  # Can user login?
    
    # User Profile
    full_name = Column(String, nullable=True)
    role = Column(String, nullable=False, default='viewer')  # 'admin', 'modeler', 'contributor', 'viewer'
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Indexes
    __table_args__ = (
        Index('idx_tenant_email', 'tenant_id', 'email'),
        Index('idx_tenant_role', 'tenant_id', 'role'),
    )
```

### Tenant Table (PostgreSQL) - Optional but Recommended

```python
class Tenant(Base):
    __tablename__ = "tenants"
    
    # Primary Key
    id = Column(String, primary_key=True)  # Tenant identifier
    name = Column(String, nullable=False)  # Organization/company name
    
    # Configuration
    is_active = Column(Boolean, default=True)
    max_users = Column(Integer, nullable=True)  # Optional: user limit
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### QueryLog Table (PostgreSQL)

```python
class QueryLog(Base):
    __tablename__ = "query_logs"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Multi-Tenancy (CRITICAL)
    tenant_id = Column(String, index=True, nullable=False)  # Organization/tenant identifier
    
    # User Profile (CRITICAL)
    user_id = Column(String, index=True, nullable=True)     # User identifier (from JWT)
    user_email = Column(String, index=True, nullable=True)  # User email (for display)
    
    # Query Data
    question = Column(Text, nullable=False)                  # Full question
    answer_preview = Column(Text, nullable=True)            # First 200 chars (saves space)
    answer_full = Column(Text, nullable=True)               # Full answer (optional, for search)
    
    # Sources & Metadata
    sources_count = Column(Integer, default=0)              # Number of sources
    sources_list = Column(JSONB, nullable=True)             # List of source names (JSON array)
    
    # Performance
    latency_ms = Column(Float, nullable=False)              # Response time
    was_cached = Column(Boolean, default=False)             # Cache hit?
    
    # Quality Metrics
    was_refusal = Column(Boolean, default=False)            # Did bot refuse?
    refusal_reason = Column(Text, nullable=True)            # Why refused (if applicable)
    
    # User Feedback (for profiles)
    feedback = Column(String, nullable=True)                # 'positive' | 'negative' | null
    feedback_timestamp = Column(DateTime, nullable=True)    # When feedback given
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Indexes (for fast queries)
    __table_args__ = (
        Index('idx_tenant_user', 'tenant_id', 'user_id'),
        Index('idx_tenant_created', 'tenant_id', 'created_at'),
        Index('idx_user_created', 'user_id', 'created_at'),
    )
```

## Role & Permission System

### Role Definitions

```python
# Role hierarchy and permissions
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

def require_permission(permission: str):
    """Decorator to require specific permission."""
    def decorator(func):
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(401, "Authentication required")
            
            user = get_user_by_id(current_user)
            if not has_permission(user.role, permission):
                raise HTTPException(403, f"Permission '{permission}' required")
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator
```

### Permission Checks

**Common Permissions:**
- `query` - Can query the RAG bot
- `upload` - Can upload documents to staging
- `approve_documents` - Can approve/reject documents
- `run_ingestion` - Can trigger knowledge base ingestion
- `view_queries` - Can view all queries (tenant-wide)
- `view_own_queries` - Can view only own queries
- `view_analytics` - Can view analytics dashboard
- `manage_users` - Can create/update/delete users
- `assign_roles` - Can assign roles to users
- `*` - All permissions (admin only)

## Key Design Decisions

### 1. **User Management & Roles**

**Why**: Need to assign roles, manage users, and control access to features.

**Implementation**:
- **User table** stores user accounts with `tenant_id` and `role`
- **Role-based permissions** control access to endpoints
- **User management API** for CRUD operations and role assignment
- **Permission decorators** enforce access control

**Security**:
```python
# Example: Protect document approval endpoint
@router.post("/documents/approve")
@require_permission('approve_documents')
async def approve_document(...):
    # Only users with 'approve_documents' permission can access
    pass
```

### 2. **Tenant Isolation (Multi-Tenancy)**

**Why**: Each organization/tenant needs complete data isolation.

**Implementation**:
- **Every query MUST have `tenant_id`**
- Extract from JWT token or request headers
- All database queries filter by `tenant_id`
- Users can ONLY see their tenant's queries

**Security**:
```python
# In API endpoint - extract tenant from JWT
async def query_rag(request: QueryRequest, current_user: Optional[str] = Depends(get_current_user)):
    # Extract tenant_id from JWT or request context
    tenant_id = get_tenant_from_user(current_user)  # Must be set!
    
    # Log with tenant_id
    log_query(
        tenant_id=tenant_id,
        user_id=current_user,
        question=request.question,
        ...
    )
```

### 2. **User Profiles (Individual Tracking)**

**Why**: Build user-specific insights, preferences, history.

**Implementation**:
- **Extract `user_id` from JWT token**
- Link all queries to specific users
- Build query history per user
- Track user preferences (topics, sources)

**Use Cases**:
- "Show me my query history"
- "What topics do I ask about most?"
- "Continue from previous conversation"
- Personalized suggestions based on history

### 3. **Answer Storage Strategy**

**Option A: Preview Only** (Recommended to start)
```python
answer_preview = answer[:200]  # First 200 chars
answer_full = None  # Don't store full answer
```
- **Pros**: Small database, fast writes
- **Cons**: Can't search full answers

**Option B: Full Answer** (Later, if needed)
```python
answer_preview = answer[:200]
answer_full = answer  # Store full answer
```
- **Pros**: Searchable answers, full history
- **Cons**: Large database (~10-50KB per query)

**Recommendation**: Start with **Option A**, add `answer_full` later if needed.

## User Management API

### 1. User CRUD Endpoints

```python
# backend/src/api/routes/users.py

@router.post("/users", response_model=UserResponse)
@require_permission('manage_users')
async def create_user(
    request: CreateUserRequest,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Create new user with role assignment."""
    
    # Get current user's tenant
    current_user_obj = get_user_by_id(current_user)
    tenant_id = current_user_obj.tenant_id
    
    # Check if email already exists
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(400, "User with this email already exists")
    
    # Create user
    new_user = User(
        id=str(uuid.uuid4()),  # Or use email as ID
        email=request.email,
        tenant_id=tenant_id,  # Same tenant as creator
        role=request.role,
        full_name=request.full_name,
        password_hash=hash_password(request.password) if request.password else None,
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    
    return UserResponse.from_orm(new_user)


@router.get("/users", response_model=List[UserResponse])
@require_permission('manage_users')
async def list_users(
    current_user: Optional[str] = Depends(get_current_user)
):
    """List all users in current user's tenant."""
    
    current_user_obj = get_user_by_id(current_user)
    tenant_id = current_user_obj.tenant_id
    
    users = db.query(User).filter(
        User.tenant_id == tenant_id
    ).all()
    
    return [UserResponse.from_orm(u) for u in users]


@router.put("/users/{user_id}/role")
@require_permission('assign_roles')
async def assign_role(
    user_id: str,
    request: AssignRoleRequest,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Assign role to user (same tenant only)."""
    
    current_user_obj = get_user_by_id(current_user)
    tenant_id = current_user_obj.tenant_id
    
    # Get target user
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == tenant_id  # Same tenant only
    ).first()
    
    if not user:
        raise HTTPException(404, "User not found")
    
    # Validate role
    if request.role not in ROLES:
        raise HTTPException(400, f"Invalid role: {request.role}")
    
    # Update role
    user.role = request.role
    db.commit()
    
    return {"success": True, "message": f"Role '{request.role}' assigned to user"}


@router.put("/users/{user_id}")
@require_permission('manage_users')
async def update_user(
    user_id: str,
    request: UpdateUserRequest,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Update user information."""
    
    current_user_obj = get_user_by_id(current_user)
    tenant_id = current_user_obj.tenant_id
    
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == tenant_id
    ).first()
    
    if not user:
        raise HTTPException(404, "User not found")
    
    # Update fields
    if request.full_name is not None:
        user.full_name = request.full_name
    if request.is_active is not None:
        user.is_active = request.is_active
    
    db.commit()
    
    return UserResponse.from_orm(user)


@router.delete("/users/{user_id}")
@require_permission('manage_users')
async def delete_user(
    user_id: str,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Delete user (soft delete - set is_active=False)."""
    
    current_user_obj = get_user_by_id(current_user)
    tenant_id = current_user_obj.tenant_id
    
    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == tenant_id
    ).first()
    
    if not user:
        raise HTTPException(404, "User not found")
    
    # Soft delete
    user.is_active = False
    db.commit()
    
    return {"success": True, "message": "User deactivated"}
```

### 2. User Request/Response Models

```python
# backend/src/models/schemas.py

class CreateUserRequest(BaseModel):
    email: str
    password: Optional[str] = None  # Optional if using external auth
    full_name: Optional[str] = None
    role: str = 'viewer'  # Default role


class UpdateUserRequest(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class AssignRoleRequest(BaseModel):
    role: str


class UserResponse(BaseModel):
    id: str
    email: str
    tenant_id: str
    role: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### 3. Helper Functions

```python
# backend/src/services/user_service.py

def get_user_by_id(user_id: str) -> Optional[User]:
    """Get user by ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str) -> Optional[User]:
    """Get user by email."""
    return db.query(User).filter(User.email == email).first()


def get_user_role(user_id: str) -> Optional[str]:
    """Get user's role."""
    user = get_user_by_id(user_id)
    return user.role if user else None


def is_admin(user_id: str) -> bool:
    """Check if user is admin."""
    return get_user_role(user_id) == 'admin'
```

## API Design

### 1. Logging Service (Background Task)

```python
# backend/src/services/query_logging.py

async def log_query(
    tenant_id: str,           # REQUIRED - from JWT/context
    user_id: Optional[str],   # From JWT
    question: str,
    answer: str,
    sources: List[str],
    latency_ms: float,
    was_cached: bool = False,
    was_refusal: bool = False
):
    """Log query to database (async, non-blocking)."""
    try:
        query_log = QueryLog(
            tenant_id=tenant_id,
            user_id=user_id,
            question=question,
            answer_preview=answer[:200],  # Store preview
            sources_count=len(sources),
            sources_list=sources,
            latency_ms=latency_ms,
            was_cached=was_cached,
            was_refusal=was_refusal,
            created_at=datetime.utcnow()
        )
        db.add(query_log)
        db.commit()
    except Exception as e:
        # Fail gracefully - don't break queries
        logger.error(f"Failed to log query: {e}")
```

### 2. Query Endpoint (Add Logging)

```python
# backend/src/api/routes/query.py

@router.post("/query")
async def query_rag(
    request: QueryRequest,
    background_tasks: BackgroundTasks,
    current_user: Optional[str] = Depends(get_current_user)  # Extract user from JWT
):
    # Extract tenant_id from JWT or user context
    tenant_id = get_tenant_id(current_user)  # Must be implemented!
    
    # Process query (fast)
    response = await process_query(request.question)
    
    # Log in background (doesn't block response)
    background_tasks.add_task(
        log_query,
        tenant_id=tenant_id,
        user_id=current_user,
        question=request.question,
        answer=response.answer,
        sources=[s.name for s in response.sources],
        latency_ms=response.latency_ms,
        was_cached=False  # TODO: Track cache hits
    )
    
    return response  # User gets response immediately
```

### 3. Admin Endpoints (Tenant-Aware)

```python
# backend/src/api/routes/admin.py

@router.get("/queries")
async def list_queries(
    skip: int = 0,
    limit: int = 50,
    tenant_id: Optional[str] = None,  # Filter by tenant
    user_id: Optional[str] = None,    # Filter by user
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    current_user: Optional[str] = Depends(get_current_user)
):
    """List queries with tenant isolation."""
    
    # Security: Only show queries for current user's tenant
    user_tenant_id = get_tenant_id(current_user)
    if tenant_id and tenant_id != user_tenant_id:
        raise HTTPException(403, "Cannot access other tenant's queries")
    
    # Build query with filters
    query = db.query(QueryLog).filter(QueryLog.tenant_id == user_tenant_id)
    
    if user_id:
        query = query.filter(QueryLog.user_id == user_id)
    if start_date:
        query = query.filter(QueryLog.created_at >= start_date)
    if end_date:
        query = query.filter(QueryLog.created_at <= end_date)
    
    # Order by newest first
    query = query.order_by(QueryLog.created_at.desc())
    
    # Paginate
    total = query.count()
    queries = query.offset(skip).limit(limit).all()
    
    return {
        "total": total,
        "queries": queries,
        "skip": skip,
        "limit": limit
    }


@router.get("/analytics")
async def get_analytics(
    tenant_id: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Get analytics for tenant."""
    
    # Security: Only show analytics for current user's tenant
    user_tenant_id = get_tenant_id(current_user)
    if tenant_id and tenant_id != user_tenant_id:
        raise HTTPException(403, "Cannot access other tenant's analytics")
    
    # Build query
    query = db.query(QueryLog).filter(QueryLog.tenant_id == user_tenant_id)
    if start_date:
        query = query.filter(QueryLog.created_at >= start_date)
    if end_date:
        query = query.filter(QueryLog.created_at <= end_date)
    
    # Calculate analytics
    total_queries = query.count()
    avg_latency = db.query(func.avg(QueryLog.latency_ms)).scalar() or 0
    
    # Top questions (group by question, count)
    top_questions = (
        query.group_by(QueryLog.question)
        .order_by(func.count(QueryLog.id).desc())
        .limit(10)
        .all()
    )
    
    return {
        "tenant_id": user_tenant_id,
        "total_queries": total_queries,
        "average_latency_ms": round(avg_latency, 2),
        "top_questions": [q.question for q in top_questions]
    }
```

## User Profile Features

### 1. User Query History

```python
@router.get("/users/{user_id}/queries")
async def get_user_queries(
    user_id: str,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Get query history for specific user (same tenant only)."""
    
    # Security: Only show own queries or same tenant
    user_tenant_id = get_tenant_id(current_user)
    
    queries = db.query(QueryLog).filter(
        QueryLog.tenant_id == user_tenant_id,
        QueryLog.user_id == user_id
    ).order_by(QueryLog.created_at.desc()).limit(100).all()
    
    return {"queries": queries}
```

### 2. User Analytics

```python
@router.get("/users/{user_id}/analytics")
async def get_user_analytics(
    user_id: str,
    current_user: Optional[str] = Depends(get_current_user)
):
    """Get analytics for specific user."""
    
    user_tenant_id = get_tenant_id(current_user)
    
    # Get user's queries
    user_queries = db.query(QueryLog).filter(
        QueryLog.tenant_id == user_tenant_id,
        QueryLog.user_id == user_id
    )
    
    # Calculate user-specific metrics
    total_queries = user_queries.count()
    top_topics = extract_topics(user_queries)  # Extract keywords/topics
    avg_latency = db.query(func.avg(QueryLog.latency_ms)).scalar()
    
    return {
        "user_id": user_id,
        "total_queries": total_queries,
        "average_latency_ms": avg_latency,
        "top_topics": top_topics
    }
```

## Multi-Tenancy Implementation

### Step 1: Extract Tenant from JWT

```python
# Update JWT payload to include tenant_id
def create_jwt_token(email: str, tenant_id: str) -> str:
    payload = {
        'email': email,
        'tenant_id': tenant_id,  # Add tenant_id
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_jwt_token(token: str) -> Optional[dict]:
    """Return full payload including tenant_id."""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return {
            'email': payload.get('email'),
            'tenant_id': payload.get('tenant_id')
        }
    except:
        return None


def get_tenant_id(user: Optional[str]) -> str:
    """Extract tenant_id from user context (JWT or request)."""
    if not user:
        return "default"  # Or raise error - decide based on requirements
    
    # Extract from JWT token
    token_data = get_token_from_request()  # Implement this
    return token_data.get('tenant_id', 'default')
```

### Step 2: Tenant-Aware Query Filtering

**CRITICAL**: All database queries MUST filter by `tenant_id`:

```python
# ✅ CORRECT - Tenant isolation
queries = db.query(QueryLog).filter(QueryLog.tenant_id == user_tenant_id).all()

# ❌ WRONG - No tenant filter (security risk!)
queries = db.query(QueryLog).all()
```

## Security Considerations

### 1. **Tenant Isolation (CRITICAL)**

- **NEVER** query without `tenant_id` filter
- **NEVER** allow users to specify `tenant_id` in requests
- Always extract `tenant_id` from authenticated user's JWT
- Validate user belongs to tenant before showing data

### 2. **User Data Privacy**

- Users can only see their own queries (within tenant)
- Admins can see all tenant queries (but not other tenants)
- Never expose `tenant_id` or `user_id` in public APIs

### 3. **Access Control**

```python
# Example: Admin can see all tenant queries
# Regular user can only see own queries

if is_admin(current_user):
    queries = db.query(QueryLog).filter(QueryLog.tenant_id == tenant_id).all()
else:
    queries = db.query(QueryLog).filter(
        QueryLog.tenant_id == tenant_id,
        QueryLog.user_id == current_user_id
    ).all()
```

## Integration with Existing Auth

### Current State
- Simple JWT auth (email/password from env vars)
- No user database
- No role system

### Migration Path

**Step 1: Add User Table**
1. Create `User` table with `tenant_id` and `role`
2. Migrate existing admin user to database
3. Update JWT to include `user_id` and `tenant_id`

**Step 2: Update Authentication**
```python
# Update login endpoint to check User table
@router.post("/auth/login")
async def login(request: LoginRequest):
    # Check User table instead of env vars
    user = get_user_by_email(request.email)
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")
    
    if not user.is_active:
        raise HTTPException(403, "User account is inactive")
    
    # Create JWT with user_id and tenant_id
    token = create_jwt_token(
        user_id=user.id,
        email=user.email,
        tenant_id=user.tenant_id,
        role=user.role
    )
    
    return {"token": token, "user": UserResponse.from_orm(user)}
```

**Step 3: Add Permission Checks**
1. Add `@require_permission()` decorator to protected endpoints
2. Update document management endpoints to check permissions
3. Update admin endpoints to check roles

## Migration Path

### Phase 1: User Management & Roles (Now)
1. Create `User` table with `tenant_id` and `role`
2. Create `Tenant` table (optional but recommended)
3. Implement user CRUD API
4. Implement role/permission system
5. Migrate existing auth to use User table
6. Add permission checks to endpoints

### Phase 2: Query Logging (Next)
1. Create `QueryLog` table with `tenant_id` and `user_id`
2. Implement logging service (async)
3. Add logging to query endpoint
4. Test with single tenant

### Phase 3: Multi-Tenancy (Later)
1. Update JWT to include `tenant_id`
2. Add tenant extraction from JWT
3. Add tenant filtering to all queries
4. Test with multiple tenants

### Phase 4: User Profiles (Future)
1. Add user query history endpoint
2. Add user analytics endpoint
3. Build user profile UI
4. Add personalization features

## Document Management Permissions

### Permission Mapping

| Action | Required Permission | Roles with Permission |
|--------|-------------------|----------------------|
| Upload document | `upload` | admin, modeler, contributor |
| Approve document | `approve_documents` | admin, modeler |
| Reject document | `approve_documents` | admin, modeler |
| View pending documents | `approve_documents` | admin, modeler |
| Run ingestion | `run_ingestion` | admin |
| View all queries | `view_queries` | admin, modeler |
| View own queries | `view_own_queries` | admin, modeler, contributor, viewer |
| View analytics | `view_analytics` | admin, modeler |

### Example: Protected Document Endpoints

```python
@router.post("/documents/upload")
@require_permission('upload')
async def upload_document(...):
    """Upload document - requires 'upload' permission."""
    pass

@router.post("/documents/approve")
@require_permission('approve_documents')
async def approve_document(...):
    """Approve document - requires 'approve_documents' permission."""
    pass

@router.post("/ingestion/run")
@require_permission('run_ingestion')
async def run_ingestion(...):
    """Run ingestion - requires 'run_ingestion' permission (admin only)."""
    pass
```

## Summary

**User Management & Roles are REQUIRED** for:
- ✅ Role-based access control
- ✅ Document approval workflow
- ✅ User assignment and management
- ✅ Multi-tenant user isolation
- ✅ Permission enforcement

**Query logging is NOT optional** for user profiles and multi-tenancy:

✅ **Required for**:
- User query history
- User preferences/topics
- Tenant data isolation
- Tenant analytics
- Billing/usage per tenant

✅ **Design now**:
- Add `User` table with `tenant_id` and `role` from the start
- Add `tenant_id` and `user_id` to QueryLog from the start
- Build tenant-aware queries from day one
- Implement permission system early
- Avoid migration pain later

✅ **Benefits**:
- Complete data isolation
- Rich user profiles
- Tenant-specific insights
- Secure multi-tenant system
- Role-based access control
- Scalable user management
