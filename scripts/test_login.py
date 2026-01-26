"""Test login endpoint to diagnose login issues."""

import requests
import json
import sys

API_URL = "http://localhost:8000"

print("=" * 60)
print("LOGIN DIAGNOSTIC TEST")
print("=" * 60)
print()

# Test 1: Check if backend is running
print("1. Testing backend health...")
try:
    response = requests.get(f"{API_URL}/api/health", timeout=5)
    if response.status_code == 200:
        print("   ✓ Backend is running")
        print(f"   Response: {response.json()}")
    else:
        print(f"   ✗ Backend returned status {response.status_code}")
        sys.exit(1)
except requests.exceptions.ConnectionError:
    print("   ✗ Backend is NOT running!")
    print("   → Start backend with: cd backend && uvicorn src.api.main:app --reload")
    sys.exit(1)
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

print()

# Test 2: Test login endpoint
print("2. Testing login endpoint...")
login_data = {
    "email": "admin@example.com",
    "password": "admin"
}

try:
    response = requests.post(
        f"{API_URL}/api/auth/login",
        json=login_data,
        timeout=5
    )
    
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("   ✓ Login successful!")
        print(f"   Token received: {data.get('token', '')[:20]}...")
        print(f"   Message: {data.get('message', '')}")
    else:
        print(f"   ✗ Login failed!")
        try:
            error = response.json()
            print(f"   Error: {error}")
        except:
            print(f"   Response: {response.text}")
        
        if response.status_code == 401:
            print()
            print("   Possible issues:")
            print("   - ALLOW_FALLBACK_ADMIN_LOGIN not set to true in .env")
            print("   - Wrong credentials")
            print("   - Database user doesn't exist")
        
except requests.exceptions.ConnectionError:
    print("   ✗ Cannot connect to backend!")
except Exception as e:
    print(f"   ✗ Error: {e}")

print()
print("=" * 60)
print("DIAGNOSTIC COMPLETE")
print("=" * 60)
