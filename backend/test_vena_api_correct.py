"""
Test Vena API with correct endpoints (intersections only).
Tests dimension/member extraction from intersections.
"""

import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.services.vena_api import VenaAPIClient
from src.utils.config import Settings
import src.utils.config as config

config.settings = Settings()

async def test():
    print("=" * 70)
    print("Testing Vena API with Correct Endpoints")
    print("=" * 70)
    
    client = VenaAPIClient()
    print(f"\n1. Client Status:")
    print(f"   Enabled: {client.enabled}")
    print(f"   Base URL: {client.base_url}")
    print(f"   Tenant: {client.tenant_name}")
    
    if not client.enabled:
        print("\n[ERROR] Vena API client not enabled. Check credentials in .env")
        return
    
    # Test intersections endpoint (the only real endpoint)
    print("\n2. Testing Intersections Endpoint (Primary API Endpoint)")
    print("-" * 70)
    
    # Model ID is required - check if user provided one
    model_id = None
    if len(sys.argv) > 1:
        model_id = sys.argv[1]
        print(f"   Using Model ID from command line: {model_id}")
    else:
        print("   [INFO] No Model ID provided.")
        print("   To test, provide a Model ID as argument:")
        print("   python test_vena_api_correct.py YOUR_MODEL_ID")
        print("\n   How to find your Model ID:")
        print("   1. Log into Vena")
        print("   2. Go to Modeler -> Data Model")
        print("   3. Check the URL - it will contain the Model ID")
        print("   4. Example URL: https://eu1.vena.io/modeler/data-model/12345")
        print("      Model ID would be: 12345")
        print("\n   Testing without Model ID (will show limitations)...")
    
    if model_id:
        # Test 1: Get intersections (small sample)
        print(f"\n   Test 1: Get intersections (limit=5)")
        try:
            intersections = await client.get_intersections(model_id, limit=5)
            if intersections:
                print(f"   [OK] Retrieved {len(intersections)} intersections")
                if len(intersections) > 0:
                    print(f"   Sample intersection keys: {list(intersections[0].keys())[:5]}")
                    print(f"   Sample intersection: {intersections[0]}")
            else:
                print("   [WARNING] No intersections returned (might be empty model or wrong Model ID)")
        except Exception as e:
            print(f"   [ERROR] Failed to get intersections: {e}")
            import traceback
            traceback.print_exc()
        
        # Test 2: Extract dimensions from intersections
        print(f"\n   Test 2: Extract dimensions from intersections")
        try:
            dimensions = await client.get_dimensions(model_id)
            if dimensions:
                print(f"   [OK] Extracted {len(dimensions)} dimensions:")
                for dim in dimensions:
                    print(f"      - {dim.get('name', dim)}")
            else:
                print("   [WARNING] Could not extract dimensions")
        except Exception as e:
            print(f"   [ERROR] Failed to extract dimensions: {e}")
        
        # Test 3: Extract dimension members (if Account dimension exists)
        print(f"\n   Test 3: Extract Account dimension members")
        try:
            account_members = await client.get_dimension_members("Account", model_id)
            if account_members:
                print(f"   [OK] Extracted {len(account_members)} Account members (showing first 10):")
                for member in account_members[:10]:
                    print(f"      - {member.get('name', member)}")
            else:
                print("   [WARNING] Could not extract Account members (dimension might not exist or be named differently)")
        except Exception as e:
            print(f"   [ERROR] Failed to extract Account members: {e}")
        
        # Test 4: Get model structure
        print(f"\n   Test 4: Get model structure (inferred from intersections)")
        try:
            structure = await client.get_model_structure(model_id)
            if structure:
                print(f"   [OK] Model structure:")
                print(f"      Model ID: {structure.get('modelId')}")
                print(f"      Dimensions: {[d.get('name') for d in structure.get('dimensions', [])]}")
            else:
                print("   [WARNING] Could not infer model structure")
        except Exception as e:
            print(f"   [ERROR] Failed to get model structure: {e}")
        
        # Test 5: Test format_vena_context with Model ID
        print(f"\n   Test 5: Test format_vena_context with Model ID")
        try:
            question = "what are my dimensions?"
            context = await client.format_vena_context(question, model_id=model_id)
            if context:
                print(f"   [OK] Generated Vena context:")
                print(f"   {context[:300]}...")
            else:
                print("   [WARNING] No context generated")
        except Exception as e:
            print(f"   [ERROR] Failed to generate context: {e}")
            import traceback
            traceback.print_exc()
    else:
        # Test without Model ID
        print("\n   Testing format_vena_context without Model ID...")
        try:
            question = "what are my dimensions?"
            context = await client.format_vena_context(question, model_id=None)
            if context:
                print(f"   Context: {context}")
            else:
                print("   [INFO] No context (expected - Model ID required)")
        except Exception as e:
            print(f"   [ERROR] {e}")
    
    print("\n" + "=" * 70)
    print("Test Complete!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Get your Model ID from Vena UI")
    print("2. Run: python test_vena_api_correct.py YOUR_MODEL_ID")
    print("3. Test the full RAG integration with Model ID")

if __name__ == "__main__":
    asyncio.run(test())
