"""
Admin endpoints for document approval workflow.
"""

import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Request
from pydantic import BaseModel

from ...services.s3_documents import (
    get_pending_documents,
    get_approved_documents,
    get_archived_documents,
    approve_document,
    reject_document,
    upload_document_to_staging
)
from ...services.kill_switch import (
    is_kill_switch_enabled,
    set_kill_switch,
    get_kill_switch_status
)
from ...utils.config import settings
from .auth import get_current_user_info
from ...services.rate_limiter import limit_admin
from qdrant_client import QdrantClient

logger = logging.getLogger(__name__)
router = APIRouter()


class DocumentInfo(BaseModel):
    """Document information model."""
    key: str
    name: str
    path: str
    size: int
    last_modified: str
    status: Optional[str] = None


class ApproveRequest(BaseModel):
    """Request model for approving a document."""
    document_key: str


class RejectRequest(BaseModel):
    """Request model for rejecting a document."""
    document_key: str
    reason: Optional[str] = None


class KillSwitchRequest(BaseModel):
    """Request model for kill switch toggle."""
    enabled: bool  # True to disable system, False to enable
    message: Optional[str] = None  # Optional custom message


@router.get("/documents/pending", response_model=List[DocumentInfo])
@limit_admin()
async def get_pending(request: Request, user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Get list of all pending documents in staging folder.
    
    Returns list of documents awaiting approval.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        documents = get_pending_documents()
        return [
            DocumentInfo(
                key=doc['key'],
                name=doc['name'],
                path=doc['path'],
                size=doc['size'],
                last_modified=doc['last_modified'],
                status='pending'
            )
            for doc in documents
        ]
    except Exception as e:
        logger.error(f"Error getting pending documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting pending documents: {str(e)}")


@router.get("/documents/approved", response_model=List[DocumentInfo])
async def get_approved():
    """
    Get list of all approved documents (knowledge base contents).
    
    Returns list of documents that have been approved and are ready for ingestion.
    This endpoint is read-only and does not require authentication for viewing.
    """
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        documents = get_approved_documents()
        return [
            DocumentInfo(
                key=doc['key'],
                name=doc['name'],
                path=doc['path'],
                size=doc['size'],
                last_modified=doc['last_modified'],
                status='approved'
            )
            for doc in documents
        ]
    except Exception as e:
        logger.error(f"Error getting approved documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting approved documents: {str(e)}")


@router.get("/documents/archived", response_model=List[DocumentInfo])
@limit_admin()
async def get_archived(request: Request, user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Get list of all archived/rejected documents.
    
    Returns list of documents that have been rejected.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        documents = get_archived_documents()
        return [
            DocumentInfo(
                key=doc['key'],
                name=doc['name'],
                path=doc['path'],
                size=doc['size'],
                last_modified=doc['last_modified'],
                status='rejected'
            )
            for doc in documents
        ]
    except Exception as e:
        logger.error(f"Error getting archived documents: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting archived documents: {str(e)}")


@router.post("/documents/approve")
@limit_admin()
async def approve(request: Request, body: ApproveRequest, user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Approve a document by moving it from staging to approved folder.
    
    After approval, document will be available for ingestion.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        success = approve_document(body.document_key)
        if not success:
            raise HTTPException(status_code=400, detail=f"Failed to approve document: {body.document_key}")
        
        return {
            "success": True,
            "message": f"Document approved: {body.document_key}",
            "document_key": body.document_key
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error approving document: {e}")
        raise HTTPException(status_code=500, detail=f"Error approving document: {str(e)}")


@router.post("/documents/reject")
@limit_admin()
async def reject(request: Request, body: RejectRequest, user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Reject a document by moving it from staging to archive folder.
    
    Rejected documents are archived and will not be ingested.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        success = reject_document(body.document_key)
        if not success:
            raise HTTPException(status_code=400, detail=f"Failed to reject document: {body.document_key}")
        
        return {
            "success": True,
            "message": f"Document rejected: {body.document_key}",
            "document_key": body.document_key,
            "reason": body.reason
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error rejecting document: {e}")
        raise HTTPException(status_code=500, detail=f"Error rejecting document: {str(e)}")


@router.post("/documents/upload")
@limit_admin()
async def upload_document(
    request: Request,
    file: UploadFile = File(...),
    user_info: Optional[dict] = Depends(get_current_user_info)
):
    """
    Upload a document to the staging folder for approval.
    
    The uploaded file will be placed in the staging folder and require approval
    before being available for ingestion.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    
    try:
        if not settings.use_s3 or not settings.s3_bucket_name:
            raise HTTPException(status_code=400, detail="S3 is not configured. Set USE_S3=true and S3_BUCKET_NAME.")
        
        # Read file content
        file_content = await file.read()
        
        if not file_content:
            raise HTTPException(status_code=400, detail="File is empty")
        
        # Upload to S3 staging
        s3_key = upload_document_to_staging(file_content, file.filename or "document")
        
        return {
            "success": True,
            "message": f"Document uploaded successfully: {file.filename}",
            "document_key": s3_key,
            "filename": file.filename
        }
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(status_code=500, detail=f"Error uploading document: {str(e)}")


@router.get("/kill-switch/status")
@limit_admin()
async def get_kill_switch_status_endpoint(request: Request, user_info: Optional[dict] = Depends(get_current_user_info)):
    """
    Get current kill switch status.
    Requires admin authentication.
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # Check if user is admin
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    return get_kill_switch_status()


@router.post("/kill-switch/toggle")
@limit_admin()
async def toggle_kill_switch(
    request: Request,
    body: KillSwitchRequest,
    user_info: Optional[dict] = Depends(get_current_user_info)
):
    """
    Toggle kill switch (enable/disable system).
    Requires admin authentication.
    
    Args:
        request: Kill switch request with enabled flag and optional message
        user_info: Current user info from auth
        
    Returns:
        Updated kill switch status
    """
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # Check if user is admin
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    user_id = user_info.get("user_id") or user_info.get("email", "unknown")
    
    # Set kill switch
    success = set_kill_switch(
        enabled=body.enabled,
        message=body.message,
        user_id=user_id
    )
    
    if not success:
        raise HTTPException(
            status_code=500,
            detail="Failed to update kill switch. Check logs for details."
        )
    
    status = get_kill_switch_status()
    action = "disabled" if body.enabled else "enabled"
    logger.info(f"Kill switch {action} by {user_id}. Message: {body.message}")
    
    return {
        "success": True,
        "message": f"System {action} successfully",
        "status": status
    }
