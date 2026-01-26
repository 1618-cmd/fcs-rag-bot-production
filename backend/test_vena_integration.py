"""
Quick test script for Vena API integration in RAG pipeline.
Tests both keyword detection and LLM intent detection.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.rag import RAGPipeline

async def test_vena_integration():
    """Test Vena API integration with various questions."""
    
    print("=" * 60)
    print("Testing Vena API Integration")
    print("=" * 60)
    
    # Initialize pipeline
    print("\n1. Initializing RAG pipeline...")
    try:
        pipeline = RAGPipeline()
        print("[OK] RAG pipeline initialized")
        
        if pipeline.vena_api:
            if pipeline.vena_api.enabled:
                print(f"[OK] Vena API client enabled for tenant: {pipeline.vena_api.tenant_name}")
            else:
                print("[WARNING] Vena API client disabled (credentials not configured)")
                print("   Add VENA_API_USER, VENA_API_KEY, VENA_TENANT_NAME, VENA_API_HUB to .env")
                return
        else:
            print("[WARNING] Vena API client not initialized")
            return
    except Exception as e:
        print(f"[ERROR] Error initializing pipeline: {e}")
        return
    
    # Test questions
    test_questions = [
        # Should trigger Vena API
        ("show me my stuff", True),
        ("what accounts do I have?", True),
        ("what's in my model?", True),
        ("help me build a script for my entities", True),
        ("what are my dimensions?", True),
        
        # Should NOT trigger Vena API
        ("how do I write VenaQL?", False),
        ("what is Line Item Details?", False),
        ("explain Vena Copilot", False),
    ]
    
    print("\n2. Testing smart detection...")
    print("-" * 60)
    
    for question, should_trigger in test_questions:
        will_trigger = pipeline._should_use_vena_api(question)
        status = "[OK]" if will_trigger == should_trigger else "[FAIL]"
        print(f"{status} '{question[:40]}...'")
        print(f"   Expected: {'YES' if should_trigger else 'NO'}, Got: {'YES' if will_trigger else 'NO'}")
    
    # Test actual API call with a simple question
    print("\n3. Testing actual Vena API call...")
    print("-" * 60)
    
    test_question = "what are my dimensions?"
    print(f"Question: '{test_question}'")
    
    try:
        # Fetch Vena context
        vena_context = await pipeline._fetch_vena_context(test_question)
        
        if vena_context:
            print("[OK] Vena API context fetched successfully!")
            print(f"\nContext preview (first 200 chars):")
            print(vena_context[:200] + "...")
        else:
            print("[WARNING] No Vena context returned (might be cached or API returned empty)")
            
    except Exception as e:
        print(f"[ERROR] Error fetching Vena context: {e}")
        import traceback
        traceback.print_exc()
    
    # Test full query
    print("\n4. Testing full RAG query with Vena API...")
    print("-" * 60)
    
    test_question = "show me my stuff"
    print(f"Question: '{test_question}'")
    print("Processing...")
    
    try:
        response, documents = await pipeline.query_async(test_question)
        print("[OK] Query completed!")
        print(f"\nResponse preview (first 300 chars):")
        print(response[:300] + "...")
        print(f"\nDocuments retrieved: {len(documents)}")
        
    except Exception as e:
        print(f"[ERROR] Error processing query: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Test complete!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_vena_integration())
