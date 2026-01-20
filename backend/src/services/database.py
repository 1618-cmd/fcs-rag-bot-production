"""
Database connection and session management.
"""

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from contextlib import contextmanager

from ..utils.config import settings
from ..models.database import Base

logger = logging.getLogger(__name__)

# Global engine and session factory
_engine = None
_SessionLocal = None


def get_database_url() -> str:
    """Get database URL from settings."""
    if not settings.database_url:
        raise ValueError("DATABASE_URL not configured. Set DATABASE_URL in environment variables.")
    return settings.database_url


def init_database():
    """Initialize database connection and create tables."""
    global _engine, _SessionLocal
    
    if not settings.database_url:
        logger.warning("DATABASE_URL not configured - database features will be disabled")
        return
    
    try:
        # Create engine
        # Use NullPool for serverless environments (Render, Railway)
        _engine = create_engine(
            get_database_url(),
            poolclass=NullPool,  # Better for serverless
            echo=False,  # Set to True for SQL debugging
            pool_pre_ping=True,  # Verify connections before using
        )
        
        # Create session factory
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
        
        logger.info("Database connection initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


def get_db():
    """
    Get database session (dependency for FastAPI routes).
    
    Usage:
        @router.get("/endpoint")
        async def my_endpoint(db: Session = Depends(get_db)):
            # Use db here
            pass
    """
    if _SessionLocal is None:
        init_database()
    
    if _SessionLocal is None:
        raise RuntimeError("Database not initialized. Check DATABASE_URL configuration.")
    
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """
    Context manager for database sessions (for use outside FastAPI routes).
    
    Usage:
        with get_db_context() as db:
            # Use db here
            pass
    """
    if _SessionLocal is None:
        init_database()
    
    if _SessionLocal is None:
        raise RuntimeError("Database not initialized. Check DATABASE_URL configuration.")
    
    db = _SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():
    """Create all database tables (for migrations or initial setup)."""
    if _engine is None:
        init_database()
    
    if _engine is None:
        raise RuntimeError("Database not initialized. Check DATABASE_URL configuration.")
    
    Base.metadata.create_all(bind=_engine)
    logger.info("Database tables created successfully")


if __name__ == "__main__":
    # Test database connection
    init_database()
    if _engine:
        print("✅ Database connection successful!")
        print(f"   URL: {get_database_url().split('@')[1] if '@' in get_database_url() else 'hidden'}")
    else:
        print("❌ Database connection failed!")
