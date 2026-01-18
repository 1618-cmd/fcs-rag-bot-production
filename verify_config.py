"""Verify local configuration matches production (except USE_S3)"""
import os
from dotenv import load_dotenv

# Load local .env
load_dotenv('backend/.env')

print("=" * 60)
print("Configuration Verification")
print("=" * 60)
print()

# Critical variables that should match
critical_vars = {
    'OPENAI_API_KEY': 'OpenAI API Key',
    'OPENAI_MODEL': 'OpenAI Model',
    'EMBEDDING_MODEL': 'Embedding Model',
    'QDRANT_URL': 'Qdrant URL',
    'QDRANT_API_KEY': 'Qdrant API Key',
    'QDRANT_COLLECTION_NAME': 'Qdrant Collection',
    'CHUNK_SIZE': 'Chunk Size',
    'CHUNK_OVERLAP': 'Chunk Overlap',
    'TOP_K_RESULTS': 'Top K Results',
}

print("Critical Variables (should match production):")
print("-" * 60)
all_set = True
for var, name in critical_vars.items():
    value = os.getenv(var)
    if value:
        # Mask sensitive values
        if 'KEY' in var or 'SECRET' in var:
            display_value = value[:10] + "..." if len(value) > 10 else "***"
        else:
            display_value = value
        print(f"[OK] {name:25} = {display_value}")
    else:
        print(f"[MISSING] {name:25} = NOT SET")
        all_set = False

print()
print("Environment-Specific Variables (should differ):")
print("-" * 60)
use_s3 = os.getenv('USE_S3', 'false').lower()
env = os.getenv('ENVIRONMENT', 'development')
print(f"  USE_S3              = {use_s3} (local should be 'false')")
print(f"  ENVIRONMENT         = {env} (local should be 'development')")

print()
print("=" * 60)
if all_set:
    print("[SUCCESS] All critical variables are set!")
    print()
    print("Next: Compare these values with your Render production environment")
    print("They should match (except USE_S3 and ENVIRONMENT)")
else:
    print("[WARNING] Some critical variables are missing!")
    print("Please add them to backend/.env")
