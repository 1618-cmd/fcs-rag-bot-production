"""
Test Vena API with a Model ID.
Run: python test_with_model_id.py YOUR_MODEL_ID
"""

import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.services.vena_api import VenaAPIClient
from src.utils.config import Settings
import src.utils.config as config

config.settings = Settings()

async def test_with_model_id(model_id: str):
    """Test Vena API with a specific Model ID."""
    
    print("=" * 70)
    print(f"Testing Vena API with Model ID: {model_id}")
    print("=" * 70)
    
    client = VenaAPIClient()
    
    if not client.enabled:
        print("[ERROR] Vena API client not enabled. Check credentials.")
        return
    
    print(f"\nClient Status:")
    print(f"  Base URL: {client.base_url}")
    print(f"  Tenant: {client.tenant_name}")
    
    # Test 1: Get intersections (small sample)
    print(f"\n{'='*70}")
    print("Test 1: Get Intersections (Sample)")
    print(f"{'='*70}")
    
    try:
        print(f"Calling: GET /models/{model_id}/intersections?limit=3")
        intersections = await client.get_intersections(model_id, limit=3)
        
        if intersections:
            print(f"[OK] Retrieved {len(intersections)} intersections")
            print(f"\nFirst intersection structure:")
            if len(intersections) > 0:
                first = intersections[0]
                print(f"  Keys: {list(first.keys())}")
                print(f"  Sample data:")
                for key, value in list(first.items())[:5]:
                    print(f"    {key}: {value}")
        else:
            print("[WARNING] No intersections returned")
            print("  Possible reasons:")
            print("  - Model ID is incorrect")
            print("  - Model has no data")
            print("  - API authentication issue")
    except Exception as e:
        print(f"[ERROR] Failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Test 2: Extract dimensions
    print(f"\n{'='*70}")
    print("Test 2: Extract Dimensions from Intersections")
    print(f"{'='*70}")
    
    try:
        dimensions = await client.get_dimensions(model_id)
        if dimensions:
            print(f"[OK] Found {len(dimensions)} dimensions:")
            for dim in dimensions:
                print(f"  - {dim.get('name', dim)}")
        else:
            print("[WARNING] Could not extract dimensions")
    except Exception as e:
        print(f"[ERROR] Failed: {e}")
    
    # Test 3: Extract members for first dimension
    print(f"\n{'='*70}")
    print("Test 3: Extract Dimension Members")
    print(f"{'='*70}")
    
    try:
        dimensions = await client.get_dimensions(model_id)
        if dimensions and len(dimensions) > 0:
            first_dim = dimensions[0].get('name') if isinstance(dimensions[0], dict) else str(dimensions[0])
            print(f"Extracting members for dimension: {first_dim}")
            
            members = await client.get_dimension_members(first_dim, model_id)
            if members:
                print(f"[OK] Found {len(members)} members (showing first 20):")
                for member in members[:20]:
                    print(f"  - {member.get('name', member)}")
                if len(members) > 20:
                    print(f"  ... and {len(members) - 20} more")
            else:
                print("[WARNING] Could not extract members")
        else:
            print("[INFO] No dimensions found to test members")
    except Exception as e:
        print(f"[ERROR] Failed: {e}")
    
    # Test 4: Test format_vena_context
    print(f"\n{'='*70}")
    print("Test 4: Test format_vena_context (Full Integration)")
    print(f"{'='*70}")
    
    test_questions = [
        "give me all hierarchies",
        "what are my dimensions?",
        "show me my account members"
    ]
    
    for question in test_questions:
        print(f"\nQuestion: '{question}'")
        try:
            context = await client.format_vena_context(question, model_id=model_id)
            if context:
                print(f"[OK] Generated context ({len(context)} chars)")
                print(f"Preview: {context[:200]}...")
            else:
                print("[WARNING] No context generated")
        except Exception as e:
            print(f"[ERROR] Failed: {e}")
    
    print(f"\n{'='*70}")
    print("Test Complete!")
    print(f"{'='*70}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_with_model_id.py YOUR_MODEL_ID")
        print("\nTo find your Model ID:")
        print("1. Log into Vena")
        print("2. Go to Modeler -> Data Model")
        print("3. Check the URL - it contains the Model ID")
        print("   Example: https://eu1.vena.io/modeler/data-model/12345")
        print("   Model ID: 12345")
        sys.exit(1)
    
    model_id = sys.argv[1]
    asyncio.run(test_with_model_id(model_id))
