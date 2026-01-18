"""
Jira integration service for creating tickets from RAG bot interactions.
"""

import logging
from typing import Optional, Dict, Any
from jira import JIRA
from jira.exceptions import JIRAError

from ..utils.config import settings

logger = logging.getLogger(__name__)


def get_jira_client() -> Optional[JIRA]:
    """
    Create and return a Jira client instance.
    
    Returns:
        JIRA client instance if configured, None otherwise
    """
    if not all([
        settings.jira_server_url,
        settings.jira_email,
        settings.jira_api_token
    ]):
        logger.debug("Jira not configured - missing required settings")
        return None
    
    try:
        jira = JIRA(
            server=settings.jira_server_url,
            basic_auth=(settings.jira_email, settings.jira_api_token)
        )
        logger.info(f"✅ Jira client connected to {settings.jira_server_url}")
        return jira
    except Exception as e:
        logger.error(f"Failed to connect to Jira: {e}")
        return None


def create_ticket(
    question: str,
    bot_response: Optional[str] = None,
    sources: Optional[list] = None,
    user_context: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a Jira ticket from a RAG bot interaction.
    
    Args:
        question: The user's question
        bot_response: The bot's response (if any)
        sources: List of source documents used
        user_context: Additional context about the user/session
        
    Returns:
        Dictionary with ticket information or error details
    """
    jira = get_jira_client()
    if not jira:
        return {
            "success": False,
            "error": "Jira not configured. Please set JIRA_SERVER_URL, JIRA_EMAIL, and JIRA_API_TOKEN."
        }
    
    if not settings.jira_project_key:
        return {
            "success": False,
            "error": "JIRA_PROJECT_KEY not configured"
        }
    
    try:
        # Format ticket description
        description_parts = []
        
        # User's question
        description_parts.append("h2. User Question")
        description_parts.append(question)
        description_parts.append("")
        
        # Bot response (if available)
        if bot_response:
            description_parts.append("h2. Bot Response")
            description_parts.append(bot_response)
            description_parts.append("")
        
        # Sources (if available)
        if sources:
            description_parts.append("h2. Knowledge Base Sources")
            for source in sources:
                source_name = source.get("name", "Unknown") if isinstance(source, dict) else str(source)
                description_parts.append(f"* {source_name}")
            description_parts.append("")
        
        # Additional context
        if user_context:
            description_parts.append("h2. Additional Context")
            description_parts.append(user_context)
            description_parts.append("")
        
        description_parts.append("---")
        description_parts.append("_This ticket was automatically created by the FCS RAG Bot._")
        
        description = "\n".join(description_parts)
        
        # Prepare ticket fields
        issue_dict = {
            "project": {"key": settings.jira_project_key},
            "summary": question[:255] if len(question) <= 255 else question[:252] + "...",  # Jira summary max 255 chars
            "description": description,
            "issuetype": {"name": settings.jira_issue_type}
        }
        
        # Add labels if configured
        if settings.jira_labels:
            labels = [label.strip() for label in settings.jira_labels.split(",")]
            issue_dict["labels"] = labels
        
        # Create the ticket
        new_issue = jira.create_issue(fields=issue_dict)
        
        # Get the ticket URL
        ticket_url = f"{settings.jira_server_url}/browse/{new_issue.key}"
        
        logger.info(f"✅ Created Jira ticket: {new_issue.key} - {ticket_url}")
        
        return {
            "success": True,
            "ticket_key": new_issue.key,
            "ticket_url": ticket_url,
            "ticket_id": new_issue.id
        }
        
    except JIRAError as e:
        error_msg = f"Jira API error: {e.text if hasattr(e, 'text') else str(e)}"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }
    except Exception as e:
        error_msg = f"Failed to create Jira ticket: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return {
            "success": False,
            "error": error_msg
        }


def is_jira_configured() -> bool:
    """
    Check if Jira is properly configured.
    
    Returns:
        True if Jira is configured, False otherwise
    """
    return all([
        settings.jira_server_url,
        settings.jira_email,
        settings.jira_api_token,
        settings.jira_project_key
    ])
