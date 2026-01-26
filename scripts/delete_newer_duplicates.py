"""
Delete newer duplicate epics and their stories.
This will delete FRBP2-92 through FRBP2-103 and their linked stories (FRBP2-106-160).
"""

import os
from dotenv import load_dotenv
from jira import JIRA

# Load credentials
env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

JIRA_SERVER_URL = os.getenv("JIRA_SERVER_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = "FRBP2"

# Newer duplicate epics to delete
NEWER_EPICS = [
    "FRBP2-92", "FRBP2-93", "FRBP2-94", "FRBP2-95", "FRBP2-96", "FRBP2-97",
    "FRBP2-98", "FRBP2-99", "FRBP2-100", "FRBP2-101", "FRBP2-102", "FRBP2-103"
]

def delete_newer_duplicates(dry_run=True):
    """
    Delete newer duplicate epics and their stories.
    
    Args:
        dry_run: If True, only shows what would be deleted
    """
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - No issues will be deleted")
    else:
        print("LIVE MODE - Epics and stories will be permanently deleted!")
    print("=" * 80)
    print()
    
    stories_to_delete = []
    epics_to_delete = []
    
    # First, collect all stories linked to these epics
    for epic_key in NEWER_EPICS:
        try:
            epic = jira.issue(epic_key)
            
            # Get linked stories
            jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
            linked_issues = jira.search_issues(jql, maxResults=100)
            
            for issue in linked_issues:
                stories_to_delete.append(issue.key)
            
            epics_to_delete.append(epic_key)
            
            if dry_run:
                print(f"[WOULD DELETE] Epic {epic_key} - {epic.fields.summary} ({len(linked_issues)} stories)")
            else:
                # Delete linked stories first
                for story_key in [issue.key for issue in linked_issues]:
                    try:
                        story = jira.issue(story_key)
                        story.delete()
                        print(f"[DELETED] Story {story_key} - {story.fields.summary}")
                    except Exception as e:
                        print(f"[ERROR] Failed to delete story {story_key}: {e}")
                
                # Then delete the epic
                epic.delete()
                print(f"[DELETED] Epic {epic_key} - {epic.fields.summary}")
                
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {epic_key} - Already deleted or does not exist")
            else:
                print(f"[ERROR] {epic_key} - {error_msg}")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    if dry_run:
        print(f"Would delete: {len(epics_to_delete)} epics")
        print(f"Would delete: {len(stories_to_delete)} stories")
        print()
        print("To actually delete, run:")
        print("  python scripts/delete_newer_duplicates.py --execute")
    else:
        print(f"Successfully deleted: {len(epics_to_delete)} epics")
        print(f"Successfully deleted: {len(stories_to_delete)} stories")

if __name__ == "__main__":
    import sys
    
    dry_run = "--execute" not in sys.argv
    
    if not dry_run:
        print("=" * 80)
        print("WARNING: This will permanently delete epics and stories!")
        print("=" * 80)
        print("This will delete:")
        print("  - 12 duplicate epics (FRBP2-92 through FRBP2-103)")
        print("  - ~55 duplicate stories (FRBP2-106 through FRBP2-160)")
        print()
        response = input("Are you sure you want to proceed? Type 'yes' to continue: ")
        if response.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    delete_newer_duplicates(dry_run=dry_run)
