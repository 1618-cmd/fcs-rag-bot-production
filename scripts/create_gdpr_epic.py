"""
Script to create GDPR Compliance epic and stories in Jira.

This script reads the GDPR business requirements and creates:
1. A GDPR Compliance epic
2. Stories for each requirement (REQ-001 through REQ-012)
3. Links all stories to the epic
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from jira import JIRA
from jira.exceptions import JIRAError
import logging

# Load environment variables from backend/.env
project_root = Path(__file__).parent.parent
env_file = project_root / "backend" / ".env"
if env_file.exists():
    load_dotenv(env_file)
else:
    # Try root .env
    root_env = project_root / ".env"
    if root_env.exists():
        load_dotenv(root_env)

# Get Jira settings from environment
JIRA_SERVER_URL = os.getenv("JIRA_SERVER_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "FRBP2")  # Default to FRBP2
JIRA_ISSUE_TYPE = os.getenv("JIRA_ISSUE_TYPE", "Task")
JIRA_LABELS = os.getenv("JIRA_LABELS", "")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GDPR Requirements data structure
GDPR_REQUIREMENTS = [
    {
        "req_id": "REQ-001",
        "title": "Data Subject Rights Implementation",
        "priority": "Critical",
        "phase": "Phase 1",
        "gdpr_articles": "15, 17, 20",
        "description": """Users must be able to exercise their fundamental GDPR rights: access to their data, deletion of their data, and export of their data in a portable format.

*Right of Access (Article 15)*
* Right of Erasure (Article 17)
* Right to Data Portability (Article 20)

Acceptance Criteria:
* All three endpoints are accessible to authenticated users
* Endpoints return complete data sets within 30 days
* Deletion requests are fully processed and verified
* Export format is machine-readable and complete
* All endpoints are documented and tested""",
    },
    {
        "req_id": "REQ-002",
        "title": "Automated Data Retention and Deletion",
        "priority": "Critical",
        "phase": "Phase 1",
        "gdpr_articles": "5(1)(e)",
        "description": """The Privacy Policy commits to specific data retention periods: query logs for 90 days, user accounts for active period plus 30 days, and cached data for 24 hours.

Requirements:
* Query logs automatically deleted 90 days after creation
* Inactive user accounts deleted 30 days after deactivation
* Redis cache entries expire after 24 hours
* Automated job runs daily to enforce retention policies
* All deletions are logged for audit purposes""",
    },
    {
        "req_id": "REQ-003",
        "title": "Consent Mechanism",
        "priority": "Critical",
        "phase": "Phase 1",
        "gdpr_articles": "7",
        "description": """The Privacy Policy states that users acknowledge reading and understanding the policy by using the service. However, there is no mechanism to track or record this consent.

Requirements:
* Database stores: privacy_policy_accepted, privacy_policy_accepted_at, privacy_policy_version
* Registration or first login displays Privacy Policy acceptance checkbox
* User cannot proceed without accepting policy
* Policy versioning is tracked
* Existing users are handled appropriately""",
    },
    {
        "req_id": "REQ-004",
        "title": "Third-Party Data Processing Agreement Verification",
        "priority": "Critical",
        "phase": "Phase 1",
        "gdpr_articles": "28",
        "description": """The Privacy Policy states that all third-party processors are bound by data processing agreements. However, these agreements have not been verified.

Requirements:
* Create processor register listing all third-party processors
* Verify DPA status for: OpenAI, Qdrant Cloud, Render, Vercel, Sentry, AWS S3, Redis provider, PostgreSQL provider
* Document international transfer safeguards (SCCs)
* Review and update quarterly""",
    },
    {
        "req_id": "REQ-005",
        "title": "Right to Restriction of Processing",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "18",
        "description": """Users have the right to request restriction of processing in certain circumstances.

Requirements:
* User table includes processing_restricted (boolean) field
* When restricted, user queries are blocked or processing suspended
* Reason for restriction is recorded
* Administrators can apply and lift restrictions
* Users are notified when restriction is applied or lifted""",
    },
    {
        "req_id": "REQ-006",
        "title": "Right to Object",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "21",
        "description": """Users have the right to object to processing based on legitimate interests.

Requirements:
* Users can object to query logging (if not essential)
* Alternative: queries are anonymised immediately (user_id removed)
* Objection is recorded and honoured
* Impact on analytics is documented""",
    },
    {
        "req_id": "REQ-007",
        "title": "Data Breach Notification Procedures",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "33, 34",
        "description": """GDPR requires notification of data breaches to supervisory authorities within 72 hours and to affected users if high risk.

Requirements:
* System monitors for unauthorised access, data leaks, security incidents
* Automated alerts for suspicious activity
* Breach assessment procedure documented
* Notification templates prepared (supervisory authority and users)
* Response procedures documented and tested""",
    },
    {
        "req_id": "REQ-008",
        "title": "Security Verification and Documentation",
        "priority": "High",
        "phase": "Phase 2",
        "gdpr_articles": "32",
        "description": """The Privacy Policy lists security measures including encryption, access controls, and monitoring. These measures must be verified and documented.

Requirements:
* Verify encryption at rest for: PostgreSQL database, Redis cache, AWS S3 storage
* Verify encryption in transit (HTTPS/TLS) for all connections
* Verify authentication and authorisation controls
* Verify Sentry error tracking is operational
* Create security measures document""",
    },
    {
        "req_id": "REQ-009",
        "title": "Processing Activities Register (ROPA)",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "30",
        "description": """GDPR requires organisations to maintain a record of processing activities documenting all personal data processing.

Requirements:
* Create comprehensive record of processing activities
* Include: purposes of processing, categories of data subjects, categories of personal data, recipients, retention periods, security measures
* Review and update ROPA quarterly
* All processing activities must be documented""",
    },
    {
        "req_id": "REQ-010",
        "title": "Data Minimisation Review",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "5(1)(c)",
        "description": """GDPR requires data minimisation: only collect and process data that is necessary.

Requirements:
* Review what data is collected in query logs
* Assess whether full question/answer text is necessary
* Consider alternatives: previews, hashes, anonymisation
* Document data minimisation decisions
* Review periodically""",
    },
    {
        "req_id": "REQ-011",
        "title": "Audit Logging",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "30, 32",
        "description": """Audit logs are required to track data access, modifications, and security events. These logs must be retained for 7 years.

Requirements:
* Log all data access (who accessed what data, when)
* Log all data modifications (who changed what, when)
* Log all GDPR requests (access, deletion, export requests)
* Log security events and administrative actions
* Audit logs stored separately, tamper-evident, retained for 7 years""",
    },
    {
        "req_id": "REQ-012",
        "title": "Data Protection Impact Assessment (DPIA)",
        "priority": "Medium",
        "phase": "Phase 3",
        "gdpr_articles": "35",
        "description": """A DPIA is required for high-risk processing activities. The system processes personal data using AI/ML technologies.

Requirements:
* Complete DPIA document assessing risks of processing
* Identify risks to data subjects
* Document mitigation measures
* Review with data protection officer or legal counsel
* Assess risks of: AI processing, data storage, third-party processors, international transfers""",
    },
]


def get_jira_client() -> Optional[JIRA]:
    """Create and return a Jira client instance."""
    if not all([JIRA_SERVER_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
        logger.error("Jira not configured - missing required settings")
        return None
    
    try:
        jira = JIRA(
            server=JIRA_SERVER_URL,
            basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
        )
        logger.info(f"✅ Jira client connected to {JIRA_SERVER_URL}")
        return jira
    except Exception as e:
        logger.error(f"Failed to connect to Jira: {e}")
        return None


def get_epic_name_field_id(jira: JIRA) -> Optional[str]:
    """Auto-detect the Epic Name custom field ID."""
    if not JIRA_PROJECT_KEY:
        return None
    
    try:
        # Get all issue types for the project
        project = jira.project(JIRA_PROJECT_KEY)
        
        # Get create metadata for the project
        create_meta = jira.createmeta(
            projectKeys=JIRA_PROJECT_KEY,
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        project_meta = create_meta["projects"][0]
        if not project_meta.get("issuetypes"):
            return None
        
        # Find Epic issue type
        epic_meta = None
        for issue_type in project_meta["issuetypes"]:
            if issue_type["name"].lower() == "epic":
                epic_meta = issue_type
                break
        
        if not epic_meta:
            logger.warning("Epic issue type not found in project")
            return None
        
        fields = epic_meta.get("fields", {})
        
        # Search for Epic Name field
        for field_id, field_data in fields.items():
            field_name = field_data.get("name", "")
            if "Epic Name" in field_name or (field_id.startswith("customfield_") and "epic" in field_name.lower()):
                logger.info(f"✅ Found Epic Name field: {field_id} ({field_name})")
                return field_id
        
        # Try common field IDs
        common_epic_fields = ["customfield_10011", "customfield_10014", "customfield_10015", "customfield_10016"]
        for field_id in common_epic_fields:
            if field_id in fields:
                logger.info(f"✅ Using common Epic Name field: {field_id}")
                return field_id
        
        logger.warning("Epic Name field not found. Will try using summary field.")
        return None
        
    except Exception as e:
        logger.error(f"Error detecting Epic Name field: {e}", exc_info=True)
        return None


def create_epic(
    jira: JIRA,
    name: str,
    description: Optional[str] = None,
    labels: Optional[list] = None
) -> Dict[str, Any]:
    """Create a Jira Epic."""
    if not JIRA_PROJECT_KEY:
        return {
            "success": False,
            "error": "JIRA_PROJECT_KEY not configured"
        }
    
    try:
        epic_name_field_id = get_epic_name_field_id(jira)
        
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        
        issue_dict = {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": name[:255] if len(name) <= 255 else name[:252] + "...",
            "issuetype": {"name": "Epic"}
        }
        
        # Add Epic Name field if found, otherwise summary will be used
        if epic_name_field_id:
            issue_dict[epic_name_field_id] = name
        else:
            logger.info("Epic Name field not found, using summary as Epic Name")
        
        if description:
            issue_dict["description"] = description
        
        # Get required fields from metadata
        try:
            create_meta = jira.createmeta(
                projectKeys=JIRA_PROJECT_KEY,
                issuetypeNames=["Epic"],
                expand="projects.issuetypes.fields"
            )
            if create_meta and create_meta.get("projects"):
                project_meta = create_meta["projects"][0]
                if project_meta.get("issuetypes"):
                    epic_meta = project_meta["issuetypes"][0]
                    fields = epic_meta.get("fields", {})
                    
                    # Find and set required date fields
                    for field_id, field_data in fields.items():
                        if field_id in issue_dict or field_id == epic_name_field_id:
                            continue
                        
                        field_name = field_data.get("name", "").lower()
                        field_schema = field_data.get("schema", {})
                        field_type = field_schema.get("type", "")
                        
                        # Check for date fields
                        if field_type == "date" or "date" in field_name:
                            if field_data.get("required", False) or "start" in field_name:
                                issue_dict[field_id] = today
                                logger.info(f"Set date field: {field_data.get('name', field_id)} ({field_id}) = {today}")
        except Exception as e:
            logger.debug(f"Could not check required fields: {e}")
        
        # Try common start date field IDs as fallback
        if "customfield_10020" not in issue_dict:
            issue_dict["customfield_10020"] = today  # Common Start Date field
        
        label_list = labels or []
        if JIRA_LABELS:
            label_list.extend([label.strip() for label in JIRA_LABELS.split(",")])
        if label_list:
            issue_dict["labels"] = list(set(label_list))
        
        new_epic = jira.create_issue(fields=issue_dict)
        epic_url = f"{JIRA_SERVER_URL}/browse/{new_epic.key}"
        
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


def _get_epic_link_field_id(jira: JIRA) -> Optional[str]:
    """Get the Epic Link custom field ID for linking stories to epics."""
    if not JIRA_PROJECT_KEY:
        return None
    
    try:
        # Get create metadata for Story/Task issue type
        create_meta = jira.createmeta(
            projectKeys=JIRA_PROJECT_KEY,
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        project_meta = create_meta["projects"][0]
        if not project_meta.get("issuetypes"):
            return None
        
        # Check all issue types for Epic Link field
        for issue_type in project_meta["issuetypes"]:
            fields = issue_type.get("fields", {})
            for field_id, field_data in fields.items():
                field_name = field_data.get("name", "")
                if "Epic Link" in field_name or "Epic" in field_name:
                    if field_id.startswith("customfield_"):
                        logger.info(f"✅ Found Epic Link field: {field_id} ({field_name})")
                        return field_id
        
        # Common Epic Link field IDs
        common_epic_link_fields = [
            "customfield_10014",  # Most common
            "customfield_10013",  # Alternative
            "customfield_10015",  # Alternative
        ]
        
        for field_id in common_epic_link_fields:
            if field_id in fields:
                logger.info(f"✅ Using common Epic Link field: {field_id}")
                return field_id
        
        logger.warning("Epic Link field not found. Stories may not be linked to epic.")
        return None
        
    except Exception as e:
        logger.error(f"Error detecting Epic Link field: {e}", exc_info=True)
        return None


def create_story(
    jira: JIRA,
    title: str,
    description: str,
    epic_key: Optional[str] = None,
    priority: str = "Medium",
    labels: Optional[list] = None
) -> Dict[str, Any]:
    """
    Create a Jira Story/Task and optionally link it to an Epic.
    
    Args:
        jira: Jira client instance
        title: Story title
        description: Story description
        epic_key: Optional Epic key to link to
        priority: Story priority
        labels: Optional list of labels
        
    Returns:
        Dictionary with story information or error details
    """
    if not JIRA_PROJECT_KEY:
        return {
            "success": False,
            "error": "JIRA_PROJECT_KEY not configured"
        }
    
    try:
        # Prepare story fields
        issue_dict = {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": title[:255] if len(title) <= 255 else title[:252] + "...",
            "description": description,
            "issuetype": {"name": "Story"}  # Try Story first, fallback to Task
        }
        
        # Add priority
        priority_map = {
            "Critical": "Highest",
            "High": "High",
            "Medium": "Medium",
            "Low": "Low"
        }
        issue_dict["priority"] = {"name": priority_map.get(priority, "Medium")}
        
        # Add labels
        label_list = labels or []
        if JIRA_LABELS:
            label_list.extend([label.strip() for label in JIRA_LABELS.split(",")])
        if label_list:
            issue_dict["labels"] = list(set(label_list))  # Remove duplicates
        
        # Link to Epic if provided
        if epic_key:
            epic_link_field_id = _get_epic_link_field_id(jira)
            if epic_link_field_id:
                issue_dict[epic_link_field_id] = epic_key
            else:
                logger.warning(f"Could not find Epic Link field. Story will be created but not linked to epic {epic_key}")
        
        # Create the story
        try:
            new_issue = jira.create_issue(fields=issue_dict)
        except JIRAError as e:
            # If Story type doesn't exist, try Task
            if "issuetype" in str(e).lower():
                logger.info("Story type not available, trying Task...")
                issue_dict["issuetype"] = {"name": "Task"}
                new_issue = jira.create_issue(fields=issue_dict)
            else:
                raise
        
        # Get the story URL
        story_url = f"{JIRA_SERVER_URL}/browse/{new_issue.key}"
        
        logger.info(f"✅ Created Jira Story: {new_issue.key} - {story_url}")
        
        return {
            "success": True,
            "story_key": new_issue.key,
            "story_url": story_url,
            "story_id": new_issue.id
        }
        
    except JIRAError as e:
        error_msg = f"Jira API error: {e.text if hasattr(e, 'text') else str(e)}"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }
    except Exception as e:
        error_msg = f"Failed to create Jira Story: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return {
            "success": False,
            "error": error_msg
        }


def main():
    """Main function to create GDPR epic and stories."""
    
    # Check if Jira is configured
    if not all([JIRA_SERVER_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY]):
        logger.error("❌ Jira is not configured. Please set JIRA_SERVER_URL, JIRA_EMAIL, JIRA_API_TOKEN, and JIRA_PROJECT_KEY in your .env file.")
        return
    
    jira = get_jira_client()
    if not jira:
        logger.error("❌ Failed to connect to Jira")
        return
    
    logger.info("🚀 Starting GDPR Compliance Epic creation...")
    
    # Create Epic
    epic_description = """This epic covers all GDPR compliance requirements for the FCS RAG Bot system, as outlined in the GDPR Compliance Business Requirements Document.

The requirements are organized into three phases:
* Phase 1 (Critical): Must be implemented before Privacy Policy publication
* Phase 2 (High Priority): Within one month
* Phase 3 (Medium Priority): Within three months

Reference: GDPR/GDPR_COMPLIANCE_BUSINESS_REQUIREMENTS.md"""
    
    epic_result = create_epic(
        jira=jira,
        name="GDPR Compliance Implementation",
        description=epic_description,
        labels=["gdpr", "compliance", "legal"]
    )
    
    if not epic_result["success"]:
        logger.error(f"❌ Failed to create epic: {epic_result.get('error')}")
        return
    
    epic_key = epic_result["epic_key"]
    epic_url = epic_result["epic_url"]
    logger.info(f"✅ Created Epic: {epic_key} - {epic_url}")
    
    # Create Stories for each requirement
    created_stories = []
    failed_stories = []
    
    for req in GDPR_REQUIREMENTS:
        req_id = req["req_id"]
        title = f"{req_id}: {req['title']}"
        
        # Build description with all details
        description_parts = [
            f"*Requirement ID:* {req_id}",
            f"*Priority:* {req['priority']}",
            f"*Phase:* {req['phase']}",
            f"*GDPR Articles:* {req['gdpr_articles']}",
            "",
            "h2. Description",
            req["description"],
            "",
            "---",
            f"_This story is part of the GDPR Compliance Implementation epic._"
        ]
        
        description = "\n".join(description_parts)
        
        # Create story
        story_result = create_story(
            jira=jira,
            title=title,
            description=description,
            epic_key=epic_key,
            priority=req["priority"],
            labels=["gdpr", "compliance", req["phase"].lower().replace(" ", "-")]
        )
        
        if story_result["success"]:
            created_stories.append({
                "req_id": req_id,
                "key": story_result["story_key"],
                "url": story_result["story_url"]
            })
            logger.info(f"✅ Created Story {req_id}: {story_result['story_key']}")
        else:
            failed_stories.append({
                "req_id": req_id,
                "error": story_result.get("error", "Unknown error")
            })
            logger.error(f"❌ Failed to create Story {req_id}: {story_result.get('error')}")
    
    # Summary
    logger.info("\n" + "="*60)
    logger.info("📊 Summary")
    logger.info("="*60)
    logger.info(f"✅ Epic created: {epic_key} - {epic_url}")
    logger.info(f"✅ Stories created: {len(created_stories)}/{len(GDPR_REQUIREMENTS)}")
    
    if created_stories:
        logger.info("\nCreated Stories:")
        for story in created_stories:
            logger.info(f"  - {story['req_id']}: {story['key']} - {story['url']}")
    
    if failed_stories:
        logger.info(f"\n❌ Failed Stories ({len(failed_stories)}):")
        for story in failed_stories:
            logger.error(f"  - {story['req_id']}: {story['error']}")
    
    logger.info("\n✅ GDPR Compliance Epic creation complete!")


if __name__ == "__main__":
    main()
