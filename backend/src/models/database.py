"""
SQLAlchemy database models for User Management, Query Logging, and Multi-Tenancy.

Based on QUERY_LOGGING_DESIGN_MULTI_TENANCY.md
"""

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, Float, Boolean, Text, DateTime, Index, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Tenant(Base):
    """Tenant/Organization table for multi-tenancy."""
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


class User(Base):
    """User table with roles and tenant association."""
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


class QueryLog(Base):
    """Query log table for analytics, user profiles, and multi-tenancy."""
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
    sources_list = Column(JSON, nullable=True)             # List of source names (JSON array)
    
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
