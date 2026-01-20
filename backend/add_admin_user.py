#!/usr/bin/env python3
"""
Add an additional admin user to the production database.
Run this on Render Shell: python add_admin_user.py
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
    
    # Get credentials from command line args or environment
    if len(sys.argv) >= 2:
        email = sys.argv[1]
        password = sys.argv[2] if len(sys.argv) >= 3 else None
        tenant_id = sys.argv[3] if len(sys.argv) >= 4 else 'default'
    else:
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')
        tenant_id = os.getenv('TENANT_ID', 'default')
    
    if not email:
        email = input("Enter admin email: ").strip()
    
    if not password:
        import getpass
        password = getpass.getpass("Enter admin password: ").strip()
        password_confirm = getpass.getpass("Confirm admin password: ").strip()
        if password != password_confirm:
            print("ERROR: Passwords don't match!")
            sys.exit(1)
    
    if not email or not password:
        print("ERROR: Email and password are required!")
        sys.exit(1)
    
    print(f"Initializing database connection...")
    init_database()
    
    with get_db_context() as db:
        # Check if tenant exists
        tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
        if not tenant:
            print(f"ERROR: Tenant '{tenant_id}' does not exist!")
            sys.exit(1)
        
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"User {email} already exists!")
            print(f"   User ID: {existing_user.id}")
            print(f"   Role: {existing_user.role}")
            print(f"   Tenant: {existing_user.tenant_id}")
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
            db.refresh(admin_user)
            print(f"SUCCESS: Created admin user:")
            print(f"   Email: {email}")
            print(f"   User ID: {admin_user.id}")
            print(f"   Role: admin")
            print(f"   Tenant: {tenant_id}")
            print(f"\nUser can now log in with these credentials!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
