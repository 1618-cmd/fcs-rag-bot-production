"""
AWS Lambda function to trigger RAG bot ingestion when files are uploaded to S3.

Deploy this to AWS Lambda and configure S3 event notifications to call it.
"""

import json
import urllib.request
import urllib.error
import os
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables (set in Lambda configuration)
RENDER_API_URL = os.environ.get(
    'RENDER_API_URL', 
    'https://fcs-rag-bot-production.onrender.com/api/ingest'
)
API_KEY = os.environ.get('INGESTION_API_KEY', '')

def lambda_handler(event, context):
    """
    Handle S3 event and trigger ingestion.
    
    Args:
        event: S3 event containing bucket and object information
        context: Lambda context
    
    Returns:
        dict: Response with status code and message
    """
    # Log the S3 event
    logger.info(f"Received S3 event: {json.dumps(event)}")
    
    # Extract S3 information
    s3_objects = []
    for record in event.get('Records', []):
        if record.get('eventSource') == 'aws:s3':
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            s3_objects.append(f"s3://{bucket}/{key}")
            logger.info(f"New file uploaded: s3://{bucket}/{key}")
    
    if not s3_objects:
        logger.warning("No S3 objects found in event")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No S3 objects in event'})
        }
    
    # Trigger ingestion API
    try:
        logger.info(f"Triggering ingestion at {RENDER_API_URL}")
        
        # Create request
        req = urllib.request.Request(
            RENDER_API_URL,
            method='POST',
            headers={
                'Content-Type': 'application/json',
            }
        )
        
        # Add API key if configured
        if API_KEY:
            req.add_header('X-API-Key', API_KEY)
            logger.info("Using API key authentication")
        else:
            logger.warning("No API key configured - endpoint should be secured!")
        
        # Make request
        with urllib.request.urlopen(req, timeout=300) as response:  # 5 minute timeout
            result = json.loads(response.read().decode('utf-8'))
            logger.info(f"Ingestion triggered successfully: {result}")
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Ingestion triggered successfully',
                    's3_objects': s3_objects,
                    'ingestion_result': result
                })
            }
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else str(e)
        logger.error(f"HTTP error triggering ingestion: {e.code} - {error_body}")
        return {
            'statusCode': e.code,
            'body': json.dumps({
                'error': f'HTTP error: {e.code}',
                'detail': error_body
            })
        }
    except urllib.error.URLError as e:
        logger.error(f"URL error triggering ingestion: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to connect to ingestion API',
                'detail': str(e)
            })
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Unexpected error',
                'detail': str(e)
            })
        }
