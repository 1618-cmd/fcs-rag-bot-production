"""
Script to delete duplicate epics from Jira.
WARNING: This will permanently delete issues. Use with caution!
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

# Epics to DELETE (from the recommendation script)
EPICS_TO_DELETE = [
    "FRBP2-1", "FRBP2-2", "FRBP2-3", "FRBP2-4", "FRBP2-5", "FRBP2-6", "FRBP2-7", "FRBP2-8", 
    "FRBP2-9", "FRBP2-10", "FRBP2-11", "FRBP2-12", "FRBP2-80", "FRBP2-81", "FRBP2-82", 
    "FRBP2-83", "FRBP2-84", "FRBP2-85", "FRBP2-86", "FRBP2-87", "FRBP2-88", "FRBP2-89", 
    "FRBP2-90", "FRBP2-91", "FRBP2-92", "FRBP2-93", "FRBP2-94", "FRBP2-95", "FRBP2-96", 
    "FRBP2-97", "FRBP2-98", "FRBP2-99", "FRBP2-100", "FRBP2-101", "FRBP2-102", "FRBP2-103", 
    "FRBP2-104"
]

def delete_duplicate_epics(dry_run=True):
    """
    Delete duplicate epics.
    
    Args:
        dry_run: If True, only shows what would be deleted without actually deleting
    """
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - No epics will be deleted")
    else:
        print("LIVE MODE - Epics will be permanently deleted!")
    print("=" * 80)
    print()
    
    deleted_count = 0
    failed_count = 0
    
    for epic_key in EPICS_TO_DELETE:
        try:
            epic = jira.issue(epic_key)
            
            # Verify it's an epic
            if epic.fields.issuetype.name != "Epic":
                print(f"[SKIP] {epic_key} - Not an Epic (type: {epic.fields.issuetype.name})")
                continue
            
            # Check if it has linked stories
            try:
                jql_linked = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
                linked_issues = jira.search_issues(jql_linked, maxResults=10)
                linked_count = len(linked_issues)
            except:
                linked_count = 0
            
            if linked_count > 0:
                print(f"[SKIP] {epic_key} - Has {linked_count} linked stories (safety check)")
                continue
            
            if dry_run:
                print(f"[WOULD DELETE] {epic_key} - {epic.fields.summary}")
            else:
                # Delete the epic
                epic.delete()
                print(f"[DELETED] {epic_key} - {epic.fields.summary}")
                deleted_count += 1
                
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {epic_key} - Already deleted or does not exist")
            else:
                print(f"[ERROR] {epic_key} - {error_msg}")
                failed_count += 1
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    if dry_run:
        print(f"Would delete: {len(EPICS_TO_DELETE)} epics")
        print()
        print("To actually delete, run:")
        print("  python scripts/delete_duplicate_epics.py --execute")
    else:
        print(f"Successfully deleted: {deleted_count} epics")
        print(f"Failed: {failed_count} epics")
        print(f"Skipped: {len(EPICS_TO_DELETE) - deleted_count - failed_count} epics")

if __name__ == "__main__":
    import sys
    
    dry_run = "--execute" not in sys.argv
    
    if not dry_run:
        print("=" * 80)
        print("WARNING: This will permanently delete epics!")
        print("=" * 80)
        response = input("Are you sure you want to proceed? Type 'yes' to continue: ")
        if response.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    delete_duplicate_epics(dry_run=dry_run)
