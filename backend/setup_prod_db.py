#!/usr/bin/env python3
"""
Simple script to set up production database tables.
Run this on Render Shell: python setup_prod_db.py
"""

import sys
import os
from pathlib import Path

# Add backend/src to path
backend_dir = Path(__file__).parent
src_dir = backend_dir / "src"
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(src_dir))

try:
    from src.services.database import init_database, create_tables
    from src.models.database import Base, User, Tenant, QueryLog
    
    print("Initializing database connection...")
    init_database()
    
    print("Creating tables...")
    create_tables()
    
    print("SUCCESS: Database tables created!")
    print("Tables: tenants, users, query_logs")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
