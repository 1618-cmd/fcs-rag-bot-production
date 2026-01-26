"""Quick check if backend is running."""
import requests
import sys

try:
    response = requests.get("http://localhost:8000/api/health", timeout=3)
    if response.status_code == 200:
        data = response.json()
        print("✓ Backend is running!")
        print(f"  Status: {data.get('status')}")
        print(f"  Environment: {data.get('environment')}")
        sys.exit(0)
    else:
        print(f"✗ Backend returned status {response.status_code}")
        sys.exit(1)
except requests.exceptions.ConnectionError:
    print("✗ Backend is NOT running on port 8000")
    print("  → Start it with: cd backend && python -m uvicorn src.api.main:app --reload")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
