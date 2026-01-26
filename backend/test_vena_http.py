"""Test Vena API HTTP request directly."""
import asyncio
import httpx
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.utils.config import Settings
import src.utils.config as config

settings = Settings()

async def test():
    api_user = settings.vena_api_user
    api_key = settings.vena_api_key
    base_url = f"https://{settings.vena_api_hub}.vena.io/api/public/v1"
    
    print(f"API User: {api_user}")
    print(f"API Key: {api_key[:10]}...")
    print(f"Base URL: {base_url}")
    
    # Test templates endpoint
    endpoint = f"{base_url}/templates"
    print(f"\nTesting: {endpoint}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                endpoint,
                auth=(api_user, api_key),
                headers={'Accept': 'application/json'},
                timeout=30.0
            )
            print(f"Status: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")
            print(f"Response text: {response.text[:500]}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"JSON data: {data}")
                except:
                    print("Not JSON")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

asyncio.run(test())
