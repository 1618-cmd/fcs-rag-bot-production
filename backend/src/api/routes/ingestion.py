"""
Ingestion endpoints for triggering knowledge base updates.
"""

import logging
from fastapi import APIRouter, HTTPException, Header
from typing import Optional

from ...core.ingestion import ingest_knowledge_base
from ...utils.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/ingest")
async def trigger_ingestion(
    x_api_key: Optional[str] = Header(None, alias="X-API-Key")
):
    """
    Trigger knowledge base ingestion from S3 or local filesystem.
    
    Requires API key authentication (set INGESTION_API_KEY in environment).
    """
    # Check API key if configured
    ingestion_api_key = getattr(settings, 'ingestion_api_key', None)
    if ingestion_api_key:
        if not x_api_key or x_api_key != ingestion_api_key:
            logger.warning("Unauthorized ingestion attempt")
            raise HTTPException(
                status_code=401,
                detail="Invalid or missing API key"
            )
    
    try:
        logger.info("Triggering knowledge base ingestion...")
        vector_store = ingest_knowledge_base()
        
        # Get collection stats
        collection_name = settings.qdrant_collection_name
        collection_info = vector_store.client.get_collection(collection_name)
        points_count = collection_info.points_count
        
        logger.info(f"Ingestion completed successfully. Collection '{collection_name}' now has {points_count} points")
        
        return {
            "status": "success",
            "message": "Ingestion completed successfully",
            "collection": collection_name,
            "points_count": points_count
        }
    except Exception as e:
        logger.error(f"Error during ingestion: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error during ingestion: {str(e)}"
        )
