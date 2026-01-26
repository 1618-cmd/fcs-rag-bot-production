"""
Verify that localhost and production configurations are aligned.

This script checks critical settings that must match between environments.
"""

import sys
import io
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add backend/src to path
project_root = Path(__file__).parent.parent
backend_src_path = project_root / "backend" / "src"
sys.path.insert(0, str(project_root / "backend"))

from src.utils.config import settings

def verify_alignment():
    """Verify critical settings are configured correctly."""
    
    print("=" * 60)
    print("LOCALHOST/PRODUCTION ALIGNMENT VERIFICATION")
    print("=" * 60)
    print()
    
    # Critical settings that MUST match
    critical_settings = {
        "QDRANT_COLLECTION_NAME": settings.qdrant_collection_name,
        "TOP_K_RESULTS": settings.top_k_results,
        "TEMPERATURE": settings.temperature,
        "MAX_TOKENS": settings.max_tokens,
        "OPENAI_MODEL": settings.openai_model,
        "EMBEDDING_MODEL": settings.embedding_model,
        "LLM_PROVIDER": settings.llm_provider,
    }
    
    # Expected values
    expected = {
        "QDRANT_COLLECTION_NAME": "fcs-rag-bot-prod",
        "TOP_K_RESULTS": 20,
        "TEMPERATURE": 0.1,
        "MAX_TOKENS": 2000,
        "OPENAI_MODEL": "gpt-4o",
        "EMBEDDING_MODEL": "text-embedding-3-small",
        "LLM_PROVIDER": "openai",
    }
    
    print("CRITICAL SETTINGS (Must Match):")
    print("-" * 60)
    
    all_match = True
    for key, value in critical_settings.items():
        expected_value = expected.get(key)
        match = value == expected_value
        status = "✅" if match else "❌"
        
        print(f"{status} {key}:")
        print(f"   Current:  {value}")
        print(f"   Expected: {expected_value}")
        
        if not match:
            all_match = False
            print(f"   ⚠️  MISMATCH!")
        print()
    
    # Environment-specific (should differ)
    print("ENVIRONMENT-SPECIFIC SETTINGS (Should Differ):")
    print("-" * 60)
    print(f"ENVIRONMENT: {settings.environment}")
    print(f"   ✅ Should be 'development' for localhost")
    print(f"   ✅ Should be 'production' for production")
    print()
    
    print("ADDITIONAL SETTINGS:")
    print("-" * 60)
    print(f"DEBUG: {settings.debug}")
    print(f"LOG_LEVEL: {settings.log_level}")
    print(f"FRONTEND_URL: {settings.frontend_url}")
    print()
    
    # Summary
    print("=" * 60)
    if all_match:
        print("✅ ALL CRITICAL SETTINGS MATCH!")
        print("   Localhost and production should produce identical results.")
    else:
        print("❌ MISMATCHES DETECTED!")
        print("   Please update your .env file to match expected values.")
    print("=" * 60)
    
    return all_match

if __name__ == "__main__":
    try:
        success = verify_alignment()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error verifying alignment: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
