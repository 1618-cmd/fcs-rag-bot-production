"""
List all files in S3 bucket for the RAG bot knowledge base.
"""

import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Load environment variables from backend/.env
load_dotenv('backend/.env')

# Get S3 configuration
bucket_name = os.getenv('S3_BUCKET_NAME', 'fcs-rag-bot-kb-prod')
prefix = os.getenv('S3_PREFIX', 'knowledge_base/')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION', 'eu-north-1')

print("=" * 60)
print(f"Listing contents of: s3://{bucket_name}/{prefix}")
print("=" * 60)

try:
    # Initialize S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )
    
    # List objects
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    
    total_files = 0
    total_size = 0
    file_types = {}
    
    for page in pages:
        for obj in page.get('Contents', []):
            key = obj['Key']
            size = obj['Size']
            last_modified = obj['LastModified']
            
            # Skip if it's a folder (ends with /)
            if key.endswith('/'):
                continue
            
            total_files += 1
            total_size += size
            
            # Get file extension
            ext = os.path.splitext(key)[1].lower() or 'no extension'
            file_types[ext] = file_types.get(ext, 0) + 1
            
            # Print file info
            size_kb = size / 1024
            print(f"{key:<60} {size_kb:>8.1f} KB  {last_modified.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  Total files: {total_files}")
    print(f"  Total size: {total_size / (1024*1024):.2f} MB")
    print(f"\nFile types:")
    for ext, count in sorted(file_types.items()):
        print(f"  {ext or '(no extension)':<20} {count:>5} files")
    
except ClientError as e:
    error_code = e.response.get("Error", {}).get("Code")
    error_message = e.response.get("Error", {}).get("Message")
    print(f"\n❌ Error: [{error_code}] {error_message}")
    print("\nCheck your AWS credentials and bucket name in backend/.env")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
