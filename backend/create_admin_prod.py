#!/usr/bin/env python3
"""
Create admin user in production database.
Run this on Render Shell: python create_admin_prod.py
"""

import sys
import os
import uuid
from pathlib import Path

# Add backend/src to path
backend_dir = Path(__file__).parent
src_dir = backend_dir / "src"
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(src_dir))

try:
    from src.services.database import init_database, get_db_context
    from src.models.database import User, Tenant
    from src.api.routes.users import hash_password
    
    # Get credentials from environment or prompt
    email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    password = os.getenv('ADMIN_PASSWORD', 'admin')
    tenant_id = os.getenv('TENANT_ID', 'default')
    tenant_name = os.getenv('TENANT_NAME', 'Default Tenant')
    
    print("Initializing database connection...")
    init_database()
    
    with get_db_context() as db:
        # Create tenant if it doesn't exist
        tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
        if not tenant:
            tenant = Tenant(
                id=tenant_id,
                name=tenant_name,
                is_active=True
            )
            db.add(tenant)
            db.commit()
            print(f"Created tenant: {tenant_name} (ID: {tenant_id})")
        else:
            print(f"Tenant already exists: {tenant_name} (ID: {tenant_id})")
        
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"User {email} already exists!")
            print(f"   User ID: {existing_user.id}")
            print(f"   Role: {existing_user.role}")
            response = input("Update to admin? (y/n): ").strip().lower()
            if response == 'y':
                existing_user.role = 'admin'
                existing_user.password_hash = hash_password(password)
                existing_user.is_active = True
                existing_user.tenant_id = tenant_id
                db.commit()
                print(f"SUCCESS: Updated user {email} to admin")
            else:
                print("Skipped.")
        else:
            # Create admin user
            admin_user = User(
                id=str(uuid.uuid4()),
                email=email,
                tenant_id=tenant_id,
                role='admin',
                password_hash=hash_password(password),
                is_active=True,
                full_name="Admin User"
            )
            db.add(admin_user)
            db.commit()
            print(f"SUCCESS: Created admin user:")
            print(f"   Email: {email}")
            print(f"   User ID: {admin_user.id}")
            print(f"   Role: admin")
            print(f"   Tenant: {tenant_id}")
            print(f"\nYou can now log in with these credentials!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
