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


def get_epic_name_field_id(jira: Optional[JIRA] = None) -> Optional[str]:
    """
    Auto-detect the Epic Name custom field ID for the project.
    
    Args:
        jira: Optional Jira client instance. If None, will create one.
        
    Returns:
        The Epic Name custom field ID (e.g., "customfield_10011") or None if not found
    """
    if jira is None:
        jira = get_jira_client()
        if not jira:
            return None
    
    if not settings.jira_project_key:
        return None
    
    try:
        # Get project metadata
        project = jira.project(settings.jira_project_key)
        
        # Get issue types for the project
        issue_types = jira.issue_types()
        
        # Find Epic issue type
        epic_type = None
        for issue_type in issue_types:
            if issue_type.name.lower() == "epic":
                epic_type = issue_type
                break
        
        if not epic_type:
            logger.warning("Epic issue type not found in project")
            return None
        
        # Get create metadata for Epic issue type
        create_meta = jira.createmeta(
            projectKeys=settings.jira_project_key,
            issuetypeIds=epic_type.id,
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        project_meta = create_meta["projects"][0]
        if not project_meta.get("issuetypes"):
            return None
        
        epic_meta = project_meta["issuetypes"][0]
        fields = epic_meta.get("fields", {})
        
        # Common Epic Name field IDs to check
        # Epic Name is typically customfield_10011, but can vary
        common_epic_fields = [
            "customfield_10011",  # Most common
            "customfield_10014",  # Alternative
            "customfield_10015",  # Alternative
        ]
        
        # Check common field IDs
        for field_id in common_epic_fields:
            if field_id in fields:
                field = fields[field_id]
                # Verify it's the Epic Name field
                if "Epic Name" in field.get("name", ""):
                    logger.info(f"✅ Found Epic Name field: {field_id}")
                    return field_id
        
        # If not found in common fields, search all fields
        for field_id, field_data in fields.items():
            if field_id.startswith("customfield_") and "Epic Name" in field_data.get("name", ""):
                logger.info(f"✅ Found Epic Name field: {field_id}")
                return field_id
        
        logger.warning("Epic Name field not found. You may need to set JIRA_EPIC_NAME_FIELD_ID manually.")
        return None
        
    except Exception as e:
        logger.error(f"Error detecting Epic Name field: {e}", exc_info=True)
        return None


def create_epic(
    name: str,
    description: Optional[str] = None,
    project_key: Optional[str] = None,
    labels: Optional[list] = None
) -> Dict[str, Any]:
    """
    Create a Jira Epic.
    
    Args:
        name: The Epic name (required)
        description: Optional Epic description
        project_key: Optional project key (defaults to settings.jira_project_key)
        labels: Optional list of labels to add
        
    Returns:
        Dictionary with Epic information or error details
    """
    jira = get_jira_client()
    if not jira:
        return {
            "success": False,
            "error": "Jira not configured. Please set JIRA_SERVER_URL, JIRA_EMAIL, and JIRA_API_TOKEN."
        }
    
    project = project_key or settings.jira_project_key
    if not project:
        return {
            "success": False,
            "error": "JIRA_PROJECT_KEY not configured"
        }
    
    try:
        # Auto-detect Epic Name field ID
        epic_name_field_id = get_epic_name_field_id(jira)
        if not epic_name_field_id:
            # Try common field IDs as fallback
            epic_name_field_id = getattr(settings, 'jira_epic_name_field_id', None) or "customfield_10011"
            logger.warning(f"Using fallback Epic Name field ID: {epic_name_field_id}")
        
        # Prepare Epic fields
        issue_dict = {
            "project": {"key": project},
            "summary": name[:255] if len(name) <= 255 else name[:252] + "...",  # Jira summary max 255 chars
            "issuetype": {"name": "Epic"}
        }
        
        # Add Epic Name (required for Epics)
        issue_dict[epic_name_field_id] = name
        
        # Add description if provided
        if description:
            issue_dict["description"] = description
        
        # Add labels if provided
        if labels:
            issue_dict["labels"] = labels
        elif settings.jira_labels:
            labels_list = [label.strip() for label in settings.jira_labels.split(",")]
            issue_dict["labels"] = labels_list
        
        # Create the Epic
        new_epic = jira.create_issue(fields=issue_dict)
        
        # Get the Epic URL
        epic_url = f"{settings.jira_server_url}/browse/{new_epic.key}"
        
        logger.info(f"✅ Created Jira Epic: {new_epic.key} - {epic_url}")
        
        return {
            "success": True,
            "epic_key": new_epic.key,
            "epic_url": epic_url,
            "epic_id": new_epic.id,
            "epic_name": name
        }
        
    except JIRAError as e:
        error_msg = f"Jira API error: {e.text if hasattr(e, 'text') else str(e)}"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }
    except Exception as e:
        error_msg = f"Failed to create Jira Epic: {str(e)}"
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
