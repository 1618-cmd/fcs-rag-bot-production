"""
Upload a specific file to S3 bucket for the RAG bot knowledge base.
"""

import os
import boto3
from pathlib import Path
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Load environment variables from backend/.env
load_dotenv('backend/.env')

# Get S3 configuration
bucket_name = os.getenv('S3_BUCKET_NAME', 'fcs-rag-bot-kb-prod')
base_prefix = os.getenv('S3_PREFIX', 'knowledge_base/')
# Upload to staging by default (requires approval)
staging_prefix = os.getenv('S3_STAGING_PREFIX', f'{base_prefix}staging/')
approved_prefix = os.getenv('S3_APPROVED_PREFIX', f'{base_prefix}approved/')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION', 'eu-north-1')

def upload_file_to_s3(local_file_path: str, s3_key: str = None, target: str = 'staging'):
    """
    Upload a file to S3 bucket.
    
    Args:
        local_file_path: Path to local file
        s3_key: S3 key (path in bucket). If None, uses relative path from knowledge_base/
        target: Target folder - 'staging' (default, requires approval) or 'approved' (direct)
    """
    if not os.path.exists(local_file_path):
        print(f"File not found: {local_file_path}")
        return False
    
    # Determine S3 key
    if s3_key is None:
        # Get relative path from knowledge_base/
        local_path = Path(local_file_path)
        kb_path = Path('knowledge_base')
        try:
            relative_path = local_path.relative_to(kb_path)
            # Use staging or approved prefix based on target
            if target == 'approved':
                base_key = f"{approved_prefix}{relative_path.as_posix()}"
            else:
                base_key = f"{staging_prefix}{relative_path.as_posix()}"
            s3_key = base_key
        except ValueError:
            # If not under knowledge_base/, use filename
            if target == 'approved':
                s3_key = f"{approved_prefix}{local_path.name}"
            else:
                s3_key = f"{staging_prefix}{local_path.name}"
    
    print(f"Uploading: {local_file_path}")
    print(f"   To: s3://{bucket_name}/{s3_key}")
    
    try:
        # Initialize S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )
        
        # Upload file
        s3_client.upload_file(local_file_path, bucket_name, s3_key)
        
        print(f"Successfully uploaded to s3://{bucket_name}/{s3_key}")
        return True
        
    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code")
        error_message = e.response.get("Error", {}).get("Message")
        print(f"Error: [{error_code}] {error_message}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python upload_to_s3.py <local_file_path> [s3_key] [--approved]")
        print("\nBy default, uploads to 'staging/' folder (requires approval)")
        print("Use --approved flag to upload directly to 'approved/' folder")
        print("\nExample:")
        print('  python upload_to_s3.py "knowledge_base/Modeler/document.md"')
        print('  python upload_to_s3.py "knowledge_base/Modeler/document.md" --approved')
        sys.exit(1)
    
    local_file = sys.argv[1]
    s3_key = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
    target = 'approved' if '--approved' in sys.argv else 'staging'
    
    success = upload_file_to_s3(local_file, s3_key, target)
    sys.exit(0 if success else 1)
