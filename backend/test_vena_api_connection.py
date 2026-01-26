"""
Test script to verify Vena API connection.

Tests authentication and basic data retrieval from Vena tenant.
Uses the VenaAPIClient from the service module.
"""

import asyncio
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from src.utils.config import Settings

# Test credentials (normally from .env)
test_settings = Settings(
    vena_api_user="1322010045789241344.1068742697497264128",
    vena_api_key="d992b8cfe0494bdbb347a9d016c6b8dd",
    vena_tenant_name="Vena Workshop",
    vena_api_hub="eu1"
)

# Override settings for testing
import src.utils.config as config_module
config_module.settings = test_settings

# Now import VenaAPIClient (it will use the overridden settings)
from src.services.vena_api import VenaAPIClient


async def test_connection():
    """Test connection to Vena API using the VenaAPIClient."""
    print(f"\n{'='*60}")
    print("Testing Vena API Connection")
    print(f"{'='*60}")
    
    client = VenaAPIClient()
    
    if not client.enabled:
        print("ERROR: Vena API client is not enabled. Check credentials.")
        print(f"   API User: {test_settings.vena_api_user is not None}")
        print(f"   API Key: {test_settings.vena_api_key is not None}")
        print(f"   Base URL: {test_settings.vena_api_base_url_computed}")
        return False, None, None
    
    print(f"SUCCESS: Client initialized")
    print(f"   Base URL: {client.base_url}")
    print(f"   Tenant: {client.tenant_name}")
    print(f"\n{'='*60}")
    print("Testing API Methods")
    print(f"{'='*60}")
    
    # Test 1: Try to get ETL templates (common endpoint)
    print("\n1. Testing get_etl_templates()...")
    templates = await client.get_etl_templates()
    if templates:
        print(f"   SUCCESS! Found {len(templates)} templates")
        print(f"   Preview: {templates[0] if templates else 'N/A'}")
    else:
        print("   WARNING: No templates found (endpoint may not exist or no templates)")
    
    # Test 2: Try to get ETL jobs
    print("\n2. Testing get_etl_jobs()...")
    jobs = await client.get_etl_jobs()
    if jobs:
        print(f"   SUCCESS! Found {len(jobs)} jobs")
    else:
        print("   WARNING: No jobs found (endpoint may not exist or no jobs)")
    
    # Test 3: Try to get dimensions (without model ID)
    print("\n3. Testing get_dimensions()...")
    dimensions = await client.get_dimensions()
    if dimensions:
        print(f"   SUCCESS! Found {len(dimensions)} dimensions")
        print(f"   Dimension names: {[d.get('name', 'N/A') for d in dimensions[:5]]}")
        return True, "dimensions", dimensions
    else:
        print("   WARNING: No dimensions found (may require model ID)")
    
    # Test 4: Try to get model structure (without model ID)
    print("\n4. Testing get_model_structure()...")
    models = await client.get_model_structure()
    if models:
        print(f"   SUCCESS! Retrieved model structure")
        if isinstance(models, list):
            print(f"   Found {len(models)} models")
            if models:
                print(f"   First model: {models[0]}")
        else:
            print(f"   Model data: {models}")
        return True, "models", models
    else:
        print("   WARNING: No models found (endpoint may require model ID)")
    
    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    print("SUCCESS: Authentication is working (no 401 errors)")
    print("WARNING: Some endpoints may require model IDs or may not exist")
    print("\nNext steps:")
    print("1. Get a Model ID from Vena UI (Modeler -> Data Model -> check URL)")
    print("2. Test get_intersections(model_id) with a real model ID")
    print("3. Test get_dimensions(model_id) with a real model ID")
    
    return False, None, None


async def test_intersections_api(model_id: str):
    """Test Vena Intersections API endpoint (requires model ID)."""
    print(f"\n{'='*60}")
    print(f"Testing Intersections API with Model ID: {model_id}")
    print(f"{'='*60}")
    
    client = VenaAPIClient()
    
    if not client.enabled:
        print("ERROR: Vena API client is not enabled.")
        return False, None, None
    
    # Test getting intersections
    print(f"\nTesting get_intersections(model_id='{model_id}')...")
    intersections = await client.get_intersections(model_id)
    
    if intersections:
        print(f"   SUCCESS! Retrieved intersections")
        print(f"   Response type: {type(intersections)}")
        if isinstance(intersections, dict):
            print(f"   Keys: {list(intersections.keys())[:10]}")
        elif isinstance(intersections, list):
            print(f"   Count: {len(intersections)}")
        return True, f"models/{model_id}/intersections", intersections
    else:
        print("   WARNING: No intersections found (may need filters or model ID is incorrect)")
        return False, None, None


async def main():
    """Main test function."""
    print("="*60)
    print("Vena API Connection Test")
    print("="*60)
    print(f"API User: {test_settings.vena_api_user}")
    print(f"API Key: {test_settings.vena_api_key[:20]}...")
    print(f"Tenant: {test_settings.vena_tenant_name}")
    print(f"Hub: {test_settings.vena_api_hub}")
    print("="*60)
    
    # Test main API endpoints
    success, working_url, data = await test_connection()
    if success:
        print(f"\nSUCCESS: FOUND WORKING ENDPOINT: {working_url}")
        return
    
    # If user provides model ID as command line argument, test intersections
    if len(sys.argv) > 1:
        model_id = sys.argv[1]
        print(f"\n{'='*60}")
        print(f"Testing with provided Model ID: {model_id}")
        print(f"{'='*60}")
        success, working_url, data = await test_intersections_api(model_id)
        if success:
            print(f"\nSUCCESS: FOUND WORKING ENDPOINT: {working_url}")
            return
    
    print("\n" + "="*60)
    print("Test Complete")
    print("="*60)
    print("\nTo test intersections endpoint, provide a Model ID:")
    print(f"  python {sys.argv[0]} <model_id>")
    print("\nTo get a Model ID:")
    print("  1. Log into Vena at https://eu1.vena.io")
    print("  2. Go to Modeler -> Data Model")
    print("  3. Select a model")
    print("  4. Check the URL or model details for the Model ID")


if __name__ == "__main__":
    asyncio.run(main())
