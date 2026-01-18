"""
S3 Document Management Service for Document Approval Workflow.

Handles moving documents between staging, approved, and archive folders in S3.
"""

import logging
import boto3
from typing import List, Optional, Dict
from botocore.exceptions import ClientError
from datetime import datetime

from ..utils.config import settings

logger = logging.getLogger(__name__)

# Initialize S3 client (lazy loading)
_s3_client = None


def get_s3_client():
    """Get or create S3 client."""
    global _s3_client
    if _s3_client is None:
        _s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )
    return _s3_client


def list_documents_in_folder(bucket_name: str, prefix: str) -> List[Dict]:
    """
    List all documents in an S3 folder.
    
    Args:
        bucket_name: S3 bucket name
        prefix: S3 prefix/folder path
        
    Returns:
        List of document info dictionaries with keys: key, name, path, size, last_modified
    """
    if not bucket_name:
        raise ValueError("S3_BUCKET_NAME must be set")
    
    s3_client = get_s3_client()
    documents = []
    
    try:
        paginator = s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        
        supported_extensions = {'.md', '.txt', '.pdf'}
        
        for page in pages:
            if 'Contents' not in page:
                continue
            
            for obj in page['Contents']:
                key = obj['Key']
                
                # Skip if it's a directory (ends with /)
                if key.endswith('/'):
                    continue
                
                # Check if file extension is supported
                file_ext = None
                if '.' in key:
                    file_ext = '.' + key.split('.')[-1].lower()
                if file_ext and file_ext not in supported_extensions:
                    continue
                
                # Extract document name and path
                relative_path = key.replace(prefix, '', 1) if key.startswith(prefix) else key
                document_name = relative_path.split('/')[-1]
                document_path = relative_path
                
                documents.append({
                    'key': key,
                    'name': document_name,
                    'path': document_path,
                    'size': obj.get('Size', 0),
                    'last_modified': obj.get('LastModified', datetime.now()).isoformat()
                })
        
        logger.info(f"Found {len(documents)} documents in s3://{bucket_name}/{prefix}")
        return documents
        
    except ClientError as e:
        logger.error(f"Error listing documents from S3: {e}")
        raise


def move_document(bucket_name: str, source_key: str, dest_prefix: str) -> bool:
    """
    Move a document from one S3 location to another.
    
    Args:
        bucket_name: S3 bucket name
        source_key: Source S3 key (full path)
        dest_prefix: Destination prefix/folder
        
    Returns:
        True if successful, False otherwise
    """
    if not bucket_name:
        raise ValueError("S3_BUCKET_NAME must be set")
    
    s3_client = get_s3_client()
    
    try:
        # Extract filename from source key
        filename = source_key.split('/')[-1]
        dest_key = f"{dest_prefix}{filename}"
        
        # If dest_prefix doesn't end with /, add it
        if not dest_prefix.endswith('/'):
            dest_key = f"{dest_prefix}/{filename}"
        
        # Copy object to new location
        copy_source = {'Bucket': bucket_name, 'Key': source_key}
        s3_client.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=dest_key)
        
        # Delete original object
        s3_client.delete_object(Bucket=bucket_name, Key=source_key)
        
        logger.info(f"Moved document from {source_key} to {dest_key}")
        return True
        
    except ClientError as e:
        logger.error(f"Error moving document in S3: {e}")
        return False


def approve_document(document_key: str) -> bool:
    """
    Approve a document by moving it from staging to approved.
    
    Args:
        document_key: S3 key of the document in staging folder
        
    Returns:
        True if successful, False otherwise
    """
    bucket_name = settings.s3_bucket_name
    approved_prefix = settings.s3_approved_prefix or f"{settings.s3_prefix}approved/"
    
    # Verify document is in staging
    staging_prefix = settings.s3_staging_prefix or f"{settings.s3_prefix}staging/"
    if not document_key.startswith(staging_prefix):
        logger.warning(f"Document {document_key} is not in staging folder")
        return False
    
    return move_document(bucket_name, document_key, approved_prefix)


def reject_document(document_key: str) -> bool:
    """
    Reject a document by moving it from staging to archive.
    
    Args:
        document_key: S3 key of the document in staging folder
        
    Returns:
        True if successful, False otherwise
    """
    bucket_name = settings.s3_bucket_name
    archive_prefix = settings.s3_archive_prefix or f"{settings.s3_prefix}archive/"
    
    # Verify document is in staging
    staging_prefix = settings.s3_staging_prefix or f"{settings.s3_prefix}staging/"
    if not document_key.startswith(staging_prefix):
        logger.warning(f"Document {document_key} is not in staging folder")
        return False
    
    return move_document(bucket_name, document_key, archive_prefix)


def get_pending_documents() -> List[Dict]:
    """
    Get list of all pending documents in staging folder.
    
    Returns:
        List of document info dictionaries
    """
    bucket_name = settings.s3_bucket_name
    staging_prefix = settings.s3_staging_prefix or f"{settings.s3_prefix}staging/"
    
    return list_documents_in_folder(bucket_name, staging_prefix)


def get_approved_documents() -> List[Dict]:
    """
    Get list of all approved documents.
    
    Returns:
        List of document info dictionaries
    """
    bucket_name = settings.s3_bucket_name
    approved_prefix = settings.s3_approved_prefix or f"{settings.s3_prefix}approved/"
    
    return list_documents_in_folder(bucket_name, approved_prefix)


def get_archived_documents() -> List[Dict]:
    """
    Get list of all archived/rejected documents.
    
    Returns:
        List of document info dictionaries
    """
    bucket_name = settings.s3_bucket_name
    archive_prefix = settings.s3_archive_prefix or f"{settings.s3_prefix}archive/"
    
    return list_documents_in_folder(bucket_name, archive_prefix)


def upload_document_to_staging(file_content: bytes, filename: str) -> str:
    """
    Upload a document to the staging folder in S3.
    
    Args:
        file_content: File content as bytes
        filename: Name of the file (will be sanitized)
        
    Returns:
        S3 key of the uploaded file
        
    Raises:
        ValueError: If S3_BUCKET_NAME is not set
        ClientError: If S3 upload fails
    """
    if not settings.s3_bucket_name:
        raise ValueError("S3_BUCKET_NAME must be set")
    
    # Sanitize filename (remove path separators and special chars)
    import os
    safe_filename = os.path.basename(filename).replace('/', '_').replace('\\', '_')
    
    # Get staging prefix
    staging_prefix = settings.s3_staging_prefix or f"{settings.s3_prefix}staging/"
    
    # Construct S3 key
    s3_key = f"{staging_prefix}{safe_filename}"
    
    # Upload to S3
    s3_client = get_s3_client()
    
    try:
        s3_client.put_object(
            Bucket=settings.s3_bucket_name,
            Key=s3_key,
            Body=file_content,
            ContentType='application/octet-stream'
        )
        
        logger.info(f"Uploaded document to s3://{settings.s3_bucket_name}/{s3_key}")
        return s3_key
        
    except ClientError as e:
        logger.error(f"Error uploading document to S3: {e}")
        raise
