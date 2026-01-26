"""
Script to help find Vena Model ID.

Since the Vena Public API doesn't have an endpoint to list models,
this script helps discover the Model ID by:
1. Trying to access the Vena API base URL
2. Testing common model ID patterns (if you have a guess)
3. Providing instructions on how to find it in the UI
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.services.vena_api import VenaAPIClient
from src.utils.config import settings


async def test_model_id(client: VenaAPIClient, model_id: str) -> bool:
    """Test if a model ID is valid by trying to get intersections."""
    try:
        intersections = await client.get_intersections(model_id, limit=1)
        if intersections:
            print(f"[OK] Model ID {model_id} is VALID!")
            print(f"   Found {len(intersections)} intersection(s)")
            if intersections:
                print(f"   Sample intersection keys: {list(intersections[0].keys())[:5]}")
            return True
    except Exception as e:
        pass
    return False


async def discover_model_id():
    """Try to discover the Model ID."""
    print("=" * 60)
    print("Vena Model ID Discovery Tool")
    print("=" * 60)
    print()
    
    # Initialize client
    client = VenaAPIClient()
    
    if not client.enabled:
        print("[ERROR] Vena API is not configured.")
        print("   Please set VENA_API_USER, VENA_API_KEY, and VENA_TENANT_NAME in your .env file")
        return
    
    print(f"[OK] Vena API client initialized")
    print(f"   Tenant: {client.tenant_name}")
    print(f"   Base URL: {client.base_url}")
    print()
    
    # Try to access base URL to see what's available
    print("Checking Vena API base URL...")
    try:
        # Try to access root or common endpoints
        result = await client._make_request('GET', '')
        if result:
            print(f"   Base URL response: {result}")
    except Exception as e:
        print(f"   Base URL check: {type(e).__name__}")
    
    print()
    print("=" * 60)
    print("Model ID Discovery")
    print("=" * 60)
    print()
    print("The Vena Public API doesn't have an endpoint to list models.")
    print("You need to find your Model ID from the Vena UI.")
    print()
    print("HOW TO FIND YOUR MODEL ID:")
    print("1. Log into Vena: https://eu1.vena.io")
    print("2. Click 'Modeler' tab")
    print("3. Click 'Data Model' in the left sidebar")
    print("4. Check the URL in your browser")
    print("5. The Model ID is the number at the end")
    print("   Example: https://eu1.vena.io/modeler/data-model/12345")
    print("            Model ID = 12345")
    print()
    
    # Check if Model ID provided as command line argument
    test_ids = None
    if len(sys.argv) > 1:
        test_ids = sys.argv[1].strip()
        print("=" * 60)
        print(f"Testing Model ID from command line: {test_ids}")
        print("=" * 60)
        print()
    else:
        print("=" * 60)
        print("To test a Model ID, run:")
        print("  python find_model_id.py <MODEL_ID>")
        print()
        print("Example:")
        print("  python find_model_id.py 12345")
        print()
        print("Or find it manually in the Vena UI as described above.")
        return
    
    if test_ids:
        print()
        print(f"Testing Model ID: {test_ids}")
        is_valid = await test_model_id(client, test_ids)
        
        if is_valid:
            print()
            print("=" * 60)
            print("SUCCESS!")
            print("=" * 60)
            print(f"Your Model ID is: {test_ids}")
            print()
            print("You can now use this Model ID in the RAG bot by:")
            print("1. Adding it to your query: 'what are my dimensions?' (with Model ID)")
            print("2. Or setting it in .env as: VENA_MODEL_ID={test_ids}")
            print()
            
            # Try to get some basic info
            print("Fetching basic model information...")
            dimensions = await client.get_dimensions(test_ids)
            if dimensions:
                print(f"   Found {len(dimensions)} dimensions:")
                for dim in dimensions[:10]:
                    dim_name = dim.get('name') if isinstance(dim, dict) else str(dim)
                    print(f"   - {dim_name}")
        else:
            print(f"[ERROR] Model ID {test_ids} is not valid or not accessible")
            print("   Please check:")
            print("   1. The Model ID is correct")
            print("   2. Your API credentials have access to this model")
            print("   3. The model exists in your tenant")
    else:
        print("Skipping Model ID test.")
        print()
        print("To test a Model ID later, run:")
        print("  python find_model_id.py")
        print()
        print("Or find it manually in the Vena UI as described above.")


if __name__ == "__main__":
    asyncio.run(discover_model_id())
