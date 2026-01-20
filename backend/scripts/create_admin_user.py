"""
Script to create the first admin user in the database.

Usage:
    python -m scripts.create_admin_user
    
Or with custom values:
    python -m scripts.create_admin_user --email admin@example.com --password mypassword --tenant-id default
"""

import argparse
import sys
import uuid
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from src.models.database import User, Tenant
from src.services.database import init_database, get_db_context
from src.utils.config import settings
from src.api.routes.users import hash_password

def create_admin_user(email: str, password: str, tenant_id: str = "default", tenant_name: str = "Default Tenant"):
    """Create admin user and tenant if they don't exist."""
    
    # Initialize database
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
            print(f"SUCCESS: Created tenant: {tenant_name} (ID: {tenant_id})")
        else:
            print(f"SUCCESS: Tenant already exists: {tenant_name} (ID: {tenant_id})")
        
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"WARNING: User with email {email} already exists!")
            print(f"   User ID: {existing_user.id}")
            print(f"   Role: {existing_user.role}")
            print(f"   Tenant: {existing_user.tenant_id}")
            response = input("   Do you want to update this user to admin? (y/n): ")
            if response.lower() == 'y':
                existing_user.role = 'admin'
                existing_user.tenant_id = tenant_id
                if password:
                    existing_user.password_hash = hash_password(password)
                existing_user.is_active = True
                db.commit()
                print(f"SUCCESS: Updated user {email} to admin role")
            return
        
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
        print(f"\nYou can now log in with these credentials!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the first admin user")
    parser.add_argument("--email", default=None, help="Admin email (default: from env or prompt)")
    parser.add_argument("--password", default=None, help="Admin password (default: from env or prompt)")
    parser.add_argument("--tenant-id", default="default", help="Tenant ID (default: 'default')")
    parser.add_argument("--tenant-name", default="Default Tenant", help="Tenant name (default: 'Default Tenant')")
    
    args = parser.parse_args()
    
    # Get email
    email = args.email or getattr(settings, 'admin_email', None)
    if not email:
        email = input("Enter admin email: ").strip()
    
    # Get password
    password = args.password or getattr(settings, 'admin_password', None)
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
    
    try:
        create_admin_user(email, password, args.tenant_id, args.tenant_name)
    except Exception as e:
        print(f"ERROR: Error creating admin user: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
