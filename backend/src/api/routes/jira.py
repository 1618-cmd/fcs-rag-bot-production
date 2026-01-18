"""
Jira integration endpoints for ticket creation.
"""

import logging
from typing import Optional, List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ...services.jira import create_ticket, is_jira_configured
from ...utils.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()


class Source(BaseModel):
    """Source document model."""
    name: str
    content: Optional[str] = None


class CreateTicketRequest(BaseModel):
    """Request model for creating a Jira ticket."""
    question: str = Field(..., description="The user's question", min_length=1, max_length=1000)
    bot_response: Optional[str] = Field(None, description="The bot's response (if any)", max_length=5000)
    sources: Optional[List[Source]] = Field(None, description="List of source documents used")
    user_context: Optional[str] = Field(None, description="Additional context about the user/session", max_length=1000)


class CreateTicketResponse(BaseModel):
    """Response model for ticket creation."""
    success: bool
    ticket_key: Optional[str] = None
    ticket_url: Optional[str] = None
    error: Optional[str] = None


@router.post("/jira/create-ticket", response_model=CreateTicketResponse)
async def create_jira_ticket(request: CreateTicketRequest):
    """
    Create a Jira ticket from a RAG bot interaction.
    
    This endpoint allows users to create support tickets when the bot
    cannot answer their question or when they need additional help.
    """
    # Check if Jira is configured
    if not is_jira_configured():
        raise HTTPException(
            status_code=503,
            detail="Jira integration is not configured. Please contact your administrator."
        )
    
    try:
        # Convert sources to list of dicts if provided
        sources_list = None
        if request.sources:
            sources_list = [{"name": source.name} for source in request.sources]
        
        # Create the ticket
        result = create_ticket(
            question=request.question,
            bot_response=request.bot_response,
            sources=sources_list,
            user_context=request.user_context
        )
        
        if result["success"]:
            return CreateTicketResponse(
                success=True,
                ticket_key=result["ticket_key"],
                ticket_url=result["ticket_url"]
            )
        else:
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to create Jira ticket")
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating Jira ticket: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error creating Jira ticket: {str(e)}"
        )


@router.get("/jira/status")
async def jira_status():
    """
    Check if Jira integration is configured and available.
    
    Returns:
        Status information about Jira integration
    """
    configured = is_jira_configured()
    
    return {
        "configured": configured,
        "server_url": settings.jira_server_url if configured else None,
        "project_key": settings.jira_project_key if configured else None,
        "issue_type": settings.jira_issue_type if configured else None
    }
