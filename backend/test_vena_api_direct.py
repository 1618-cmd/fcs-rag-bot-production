"""Test Vena API directly."""
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
    print(f"Base URL: {client.base_url}")
    
    if not client.enabled:
        print("Client not enabled - check credentials")
        return
    
    print("\nTesting format_vena_context('what are my dimensions?')...")
    result = await client.format_vena_context('what are my dimensions?')
    print(f"Result type: {type(result)}")
    print(f"Result: {result}")
    
    if result:
        print(f"\nResult length: {len(result)}")
        print(f"First 500 chars: {result[:500]}")
    else:
        print("\nResult is None or empty")

asyncio.run(test())
