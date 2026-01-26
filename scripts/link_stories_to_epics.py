"""
Script to link Jira stories/tasks to their parent epics.

Reads the CSV file to get the epic-story mappings, then uses Jira API
to automatically link all stories to their epics.
"""

import csv
import logging
from pathlib import Path
from typing import Dict, List, Optional
from jira import JIRA
from jira.exceptions import JIRAError

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_epic_mappings(csv_path: Path) -> Dict[str, List[str]]:
    """
    Load epic-to-stories mapping from CSV file.
    
    Returns:
        Dictionary mapping epic summary to list of story summaries
    """
    mappings = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                issue_type = row.get('Issue Type', '').strip()
                summary = row.get('Summary', '').strip()
                parent_summary = row.get('Parent summary', '').strip()
                epic_link = row.get('Epic Link', '').strip()
                
                # Use Parent summary if available, otherwise Epic Link
                epic_name = parent_summary or epic_link
                
                if issue_type == 'Epic':
                    # This is an epic - initialize its list
                    if summary and summary not in mappings:
                        mappings[summary] = []
                elif issue_type in ['Story', 'Task'] and epic_name:
                    # This is a story/task with an epic link
                    if epic_name not in mappings:
                        mappings[epic_name] = []
                    mappings[epic_name].append(summary)
        
        logger.info(f"Loaded mappings for {len(mappings)} epics")
        for epic, stories in mappings.items():
            logger.info(f"  {epic}: {len(stories)} stories")
        
        return mappings
        
    except Exception as e:
        logger.error(f"Error reading CSV: {e}")
        raise


def get_jira_client(server_url: str, email: str, api_token: str) -> JIRA:
    """Create and return Jira client."""
    try:
        jira = JIRA(
            server=server_url,
            basic_auth=(email, api_token)
        )
        logger.info(f"✅ Connected to Jira: {server_url}")
        return jira
    except Exception as e:
        logger.error(f"Failed to connect to Jira: {e}")
        raise


def find_epic_by_summary(jira: JIRA, project_key: str, epic_summary: str) -> Optional[str]:
    """
    Find an epic by its summary in the project.
    
    Returns:
        Epic key (e.g., FRBP2-1) or None if not found
    """
    try:
        # Search for epic by summary
        jql = f'project = {project_key} AND issuetype = Epic AND summary ~ "{epic_summary}"'
        issues = jira.search_issues(jql, maxResults=1)
        
        if issues:
            epic_key = issues[0].key
            logger.info(f"Found epic: {epic_key} = {epic_summary}")
            return epic_key
        else:
            logger.warning(f"Epic not found: {epic_summary}")
            return None
            
    except Exception as e:
        logger.error(f"Error finding epic '{epic_summary}': {e}")
        return None


def find_story_by_summary(jira: JIRA, project_key: str, story_summary: str) -> Optional[str]:
    """
    Find a story/task by its summary in the project.
    
    Returns:
        Story key (e.g., FRBP2-13) or None if not found
    """
    try:
        # Search for story/task by summary (exact match)
        jql = f'project = {project_key} AND (issuetype = Task OR issuetype = Story) AND summary ~ "{story_summary}"'
        issues = jira.search_issues(jql, maxResults=1)
        
        if issues:
            story_key = issues[0].key
            return story_key
        else:
            logger.warning(f"Story not found: {story_summary}")
            return None
            
    except Exception as e:
        logger.error(f"Error finding story '{story_summary}': {e}")
        return None


def get_epic_link_field_name(jira: JIRA, project_key: str) -> Optional[str]:
    """
    Discover the Epic Link field name for the project.
    
    Returns:
        Field name (e.g., 'customfield_10014') or None if not found
    """
    try:
        # Get project metadata
        project = jira.project(project_key)
        
        # Get issue types
        issue_types = jira.issue_types()
        
        # Find Task/Story issue type
        task_type = None
        for it in issue_types:
            if it.name in ['Task', 'Story']:
                task_type = it
                break
        
        if not task_type:
            return None
        
        # Get create metadata to find fields
        create_meta = jira.createmeta(
            projectKeys=project_key,
            issuetypeIds=task_type.id,
            expand="projects.issuetypes.fields"
        )
        
        if not create_meta or not create_meta.get("projects"):
            return None
        
        project_meta = create_meta["projects"][0]
        if not project_meta.get("issuetypes"):
            return None
        
        task_meta = project_meta["issuetypes"][0]
        fields = task_meta.get("fields", {})
        
        # Look for Epic Link field
        for field_id, field_data in fields.items():
            field_name = field_data.get("name", "")
            if "epic" in field_name.lower() and "link" in field_name.lower():
                logger.info(f"Found Epic Link field: {field_id} ({field_name})")
                return field_id
        
        # Common Epic Link field IDs
        common_fields = ['customfield_10014', 'customfield_10011']
        for field_id in common_fields:
            if field_id in fields:
                logger.info(f"Using common Epic Link field: {field_id}")
                return field_id
        
        return None
        
    except Exception as e:
        logger.warning(f"Could not discover Epic Link field: {e}")
        return None


def link_story_to_epic(jira: JIRA, story_key: str, epic_key: str, epic_field_name: Optional[str] = None) -> bool:
    """
    Link a story to an epic using the Epic Link field.
    
    Args:
        jira: Jira client
        story_key: Story issue key (e.g., FRBP2-13)
        epic_key: Epic issue key (e.g., FRBP2-1)
        epic_field_name: Epic Link field name (if known)
    
    Returns:
        True if successful, False otherwise
    """
    try:
        issue = jira.issue(story_key)
        
        # Try different field names
        field_names_to_try = []
        
        if epic_field_name:
            field_names_to_try.append(epic_field_name)
        
        # Add common variations
        field_names_to_try.extend([
            'customfield_10014',  # Common Epic Link field
            'customfield_10011',  # Alternative
            'Epic Link',
            'epicLink',
            'parent'
        ])
        
        updated = False
        for field_name in field_names_to_try:
            try:
                if field_name == 'parent':
                    # Parent field needs dict format
                    issue.update(fields={'parent': {'key': epic_key}})
                else:
                    # Epic Link field just needs the key
                    issue.update(fields={field_name: epic_key})
                
                logger.info(f"✅ Linked {story_key} to epic {epic_key} using field '{field_name}'")
                updated = True
                break
            except (JIRAError, KeyError, AttributeError) as e:
                # Field doesn't exist or wrong format, try next
                continue
        
        if not updated:
            logger.warning(f"❌ Could not link {story_key} to {epic_key} - tried all field names")
            return False
        
        return updated
        
    except Exception as e:
        logger.error(f"Error linking {story_key} to {epic_key}: {e}")
        return False


def main():
    """Main function to link all stories to their epics."""
    
    import os
    
    # Try to load from environment variables first
    JIRA_SERVER_URL = os.getenv("JIRA_SERVER_URL", "https://waitemiles.atlassian.net")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    # Use FRBP2 (where epics were imported) instead of VRBP from config
    PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "FRBP2")
    if PROJECT_KEY == "VRBP":
        PROJECT_KEY = "FRBP2"  # Epics were imported to FRBP2
        logger.info("Using FRBP2 project (epics were imported here)")
    
    # If not in env vars, try to load from .env file directly
    if not JIRA_EMAIL or not JIRA_API_TOKEN:
        try:
            env_file = Path(__file__).parent.parent / "backend" / ".env"
            if env_file.exists():
                logger.info(f"Loading credentials from: {env_file}")
                with open(env_file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip().strip('"').strip("'")
                            if key == 'JIRA_SERVER_URL':
                                JIRA_SERVER_URL = value
                            elif key == 'JIRA_EMAIL':
                                JIRA_EMAIL = value
                            elif key == 'JIRA_API_TOKEN':
                                JIRA_API_TOKEN = value
                            # Don't read JIRA_PROJECT_KEY - we force FRBP2 below
                if JIRA_EMAIL and JIRA_API_TOKEN:
                    logger.info("✅ Using Jira credentials from .env file")
        except Exception as e:
            logger.debug(f"Could not load from .env: {e}")
    
    # If still not found, error out
    if not JIRA_EMAIL or not JIRA_API_TOKEN:
        logger.error("Jira credentials not found!")
        logger.error("Please set JIRA_EMAIL and JIRA_API_TOKEN environment variables,")
        logger.error("or configure them in backend/.env file")
        return
    
    # Force project to FRBP2 (where epics were imported)
    PROJECT_KEY = "FRBP2"
    logger.info(f"Using project: {PROJECT_KEY} (epics were imported here)")
    logger.info(f"Server: {JIRA_SERVER_URL}")
    
    # Path to CSV file
    project_root = Path(__file__).parent.parent
    csv_path = project_root / "docs" / "Phase Jira.csv"
    
    if not csv_path.exists():
        logger.error(f"CSV file not found: {csv_path}")
        return
    
    logger.info("=" * 60)
    logger.info("Jira Story-to-Epic Linking Script")
    logger.info("=" * 60)
    
    # Load mappings from CSV
    logger.info(f"Loading epic-story mappings from: {csv_path}")
    mappings = load_epic_mappings(csv_path)
    
    # Connect to Jira
    logger.info("Connecting to Jira...")
    jira = get_jira_client(JIRA_SERVER_URL, JIRA_EMAIL, JIRA_API_TOKEN)
    
    # Find all epics first
    logger.info("\nFinding epics in Jira...")
    epic_keys = {}
    for epic_summary in mappings.keys():
        epic_key = find_epic_by_summary(jira, PROJECT_KEY, epic_summary)
        if epic_key:
            epic_keys[epic_summary] = epic_key
    
    logger.info(f"\nFound {len(epic_keys)} epics out of {len(mappings)}")
    
    # Discover Epic Link field name
    logger.info("\nDiscovering Epic Link field name...")
    epic_field_name = get_epic_link_field_name(jira, PROJECT_KEY)
    if epic_field_name:
        logger.info(f"Using Epic Link field: {epic_field_name}")
    else:
        logger.warning("Could not discover Epic Link field - will try common field names")
    
    # Link stories to epics
    logger.info("\nLinking stories to epics...")
    success_count = 0
    fail_count = 0
    
    for epic_summary, epic_key in epic_keys.items():
        story_summaries = mappings[epic_summary]
        logger.info(f"\nEpic: {epic_summary} ({epic_key})")
        logger.info(f"  Linking {len(story_summaries)} stories...")
        
        for story_summary in story_summaries:
            story_key = find_story_by_summary(jira, PROJECT_KEY, story_summary)
            if story_key:
                if link_story_to_epic(jira, story_key, epic_key, epic_field_name):
                    success_count += 1
                else:
                    fail_count += 1
            else:
                logger.warning(f"  ⚠️  Story not found: {story_summary}")
                fail_count += 1
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("Linking Complete!")
    logger.info(f"✅ Successfully linked: {success_count} stories")
    logger.info(f"❌ Failed to link: {fail_count} stories")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
