"""
Script to create database tables directly (without Alembic).

Run this on Render Shell:
    python -m scripts.setup_database
"""

import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from src.services.database import init_database
from src.models.database import Base, User, Tenant, QueryLog
from sqlalchemy import inspect

def setup_database():
    """Create all database tables."""
    print("Initializing database connection...")
    
    # Initialize database
    init_database()
    
    # Get engine from database service
    from src.services.database import _engine
    if _engine is None:
        print("ERROR: Database engine not initialized. Check DATABASE_URL.")
        sys.exit(1)
    
    print("Creating tables...")
    
    # Create all tables
    Base.metadata.create_all(bind=_engine)
    
    print("SUCCESS: Tables created successfully!")
    
    # Verify tables exist
    inspector = inspect(_engine)
    tables = inspector.get_table_names()
    print(f"Created tables: {', '.join(tables)}")
    
    # Check if tables have data
    from sqlalchemy import text
    with _engine.connect() as conn:
        for table_name in tables:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.scalar()
            print(f"   - {table_name}: {count} rows")

if __name__ == "__main__":
    try:
        setup_database()
    except Exception as e:
        print(f"ERROR: Error setting up database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
