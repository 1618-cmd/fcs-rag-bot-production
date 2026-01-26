"""Test Vena API intent detection."""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.services.vena_api import VenaAPIClient
from src.utils.config import Settings
import src.utils.config as config

config.settings = Settings()

async def test():
    client = VenaAPIClient()
    print(f"Enabled: {client.enabled}")
    
    if not client.enabled:
        print("Client not enabled")
        return
    
    question = "what are my dimensions?"
    print(f"\nTesting intent detection for: '{question}'")
    
    # Test keyword-based intent (fallback)
    intent = client._keyword_based_intent(question)
    print(f"Keyword-based intent: {intent}")
    
    # Test LLM intent detection
    print("\nTesting LLM intent detection...")
    try:
        llm_intent = await client._detect_vena_intent(question)
        print(f"LLM intent: {llm_intent}")
    except Exception as e:
        print(f"LLM intent detection failed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test format_vena_context with debug
    print("\nTesting format_vena_context with debug logging...")
    result = await client.format_vena_context(question)
    print(f"Result: {result}")

asyncio.run(test())
