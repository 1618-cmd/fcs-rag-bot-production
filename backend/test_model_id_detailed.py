"""
Detailed test script to debug Model ID access.
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.services.vena_api import VenaAPIClient
from src.utils.config import settings


async def test_model_detailed(model_id: str):
    """Test Model ID with detailed error reporting."""
    print(f"Testing Model ID: {model_id}")
    print(f"API User: {settings.vena_api_user}")
    print(f"API Key: {settings.vena_api_key[:10]}..." if settings.vena_api_key else "None")
    print(f"Base URL: {settings.vena_api_base_url_computed}")
    print()
    
    client = VenaAPIClient()
    
    if not client.enabled:
        print("[ERROR] Vena API client is not enabled")
        return
    
    # Try to get intersections with detailed error handling
    endpoint = f"models/{model_id}/intersections"
    print(f"Testing endpoint: {endpoint}")
    print()
    
    try:
        # Make a direct request to see the actual error
        result = await client._make_request('GET', endpoint, params={'limit': 1})
        
        if result:
            print("[SUCCESS] Model ID is valid!")
            print(f"Response: {result}")
        else:
            print("[ERROR] Request returned None")
            print("This could mean:")
            print("  1. Model ID doesn't exist")
            print("  2. API credentials don't have access")
            print("  3. Model is in a different tenant")
            print("  4. API endpoint returned an error (check logs)")
    except Exception as e:
        print(f"[EXCEPTION] Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    model_id = sys.argv[1] if len(sys.argv) > 1 else "1406395748766973952"
    asyncio.run(test_model_detailed(model_id))
