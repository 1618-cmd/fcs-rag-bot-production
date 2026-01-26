"""Test Vena API calls directly."""
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
        print("Client not enabled")
        return
    
    print("\n1. Testing get_dimensions()...")
    try:
        dimensions = await client.get_dimensions()
        print(f"Dimensions result: {dimensions}")
        print(f"Type: {type(dimensions)}")
        if dimensions:
            print(f"Length: {len(dimensions)}")
            print(f"First item: {dimensions[0] if len(dimensions) > 0 else 'N/A'}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n2. Testing get_etl_templates()...")
    try:
        templates = await client.get_etl_templates()
        print(f"Templates result: {templates}")
        if templates:
            print(f"Length: {len(templates)}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

asyncio.run(test())
