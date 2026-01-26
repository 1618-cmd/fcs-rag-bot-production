"""Check and delete remaining duplicates, keeping the ones linked to epics."""

import os
from dotenv import load_dotenv
from jira import JIRA

env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

jira = JIRA(
    server=os.getenv("JIRA_SERVER_URL"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

PROJECT_KEY = "FRBP2"

# Duplicates to check
DUPLICATE_EPIC = {
    "keep": "FRBP2-105",  # Original, has linked stories
    "delete": "FRBP2-197"  # Newer duplicate
}

DUPLICATE_TASKS = [
    {"keep": "FRBP2-78", "delete": "FRBP2-252", "name": "Alerting for prompt degradation"},
    {"keep": "FRBP2-79", "delete": "FRBP2-253", "name": "Cost tracking per prompt version"},
    {"keep": "FRBP2-173", "delete": "FRBP2-254", "name": "REQ-001: Data Subject Rights Implementation"},
    {"keep": "FRBP2-174", "delete": "FRBP2-255", "name": "REQ-002: Automated Data Retention and Deletion"},
]

def check_epic_links(epic_key):
    """Check how many stories are linked to an epic."""
    try:
        jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
        linked = jira.search_issues(jql, maxResults=100)
        return len(linked)
    except:
        return 0

def delete_duplicates(dry_run=True):
    """Delete duplicate issues."""
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - No issues will be deleted")
    else:
        print("LIVE MODE - Issues will be permanently deleted!")
    print("=" * 80)
    print()
    
    # Check epic
    keep_epic_links = check_epic_links(DUPLICATE_EPIC["keep"])
    delete_epic_links = check_epic_links(DUPLICATE_EPIC["delete"])
    
    print(f"Epic {DUPLICATE_EPIC['keep']}: {keep_epic_links} linked stories")
    print(f"Epic {DUPLICATE_EPIC['delete']}: {delete_epic_links} linked stories")
    print()
    
    deleted = []
    errors = []
    
    # Delete duplicate epic
    if delete_epic_links == 0:
        try:
            epic = jira.issue(DUPLICATE_EPIC["delete"])
            if dry_run:
                print(f"[WOULD DELETE] Epic {DUPLICATE_EPIC['delete']}: {epic.fields.summary}")
            else:
                epic.delete()
                print(f"[DELETED] Epic {DUPLICATE_EPIC['delete']}: {epic.fields.summary}")
                deleted.append(DUPLICATE_EPIC["delete"])
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {DUPLICATE_EPIC['delete']} - Already deleted")
            else:
                print(f"[ERROR] {DUPLICATE_EPIC['delete']} - {error_msg}")
                errors.append((DUPLICATE_EPIC["delete"], error_msg))
    else:
        print(f"[SKIP] Epic {DUPLICATE_EPIC['delete']} - Has {delete_epic_links} linked stories, keeping it")
    
    print()
    
    # Delete duplicate tasks
    for task_info in DUPLICATE_TASKS:
        task_key = task_info["delete"]
        try:
            task = jira.issue(task_key)
            if dry_run:
                print(f"[WOULD DELETE] {task_key}: {task_info['name']}")
            else:
                task.delete()
                print(f"[DELETED] {task_key}: {task_info['name']}")
                deleted.append(task_key)
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {task_key} - Already deleted")
            else:
                print(f"[ERROR] {task_key} - {error_msg}")
                errors.append((task_key, error_msg))
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    if dry_run:
        print(f"Would delete: {len(DUPLICATE_TASKS) + (1 if delete_epic_links == 0 else 0)} issues")
        print()
        print("To actually delete, run:")
        print("  python scripts/check_and_delete_remaining_duplicates.py --execute")
    else:
        print(f"Successfully deleted: {len(deleted)} issues")
        if errors:
            print(f"Errors: {len(errors)}")
            for issue_key, error in errors:
                print(f"  {issue_key}: {error}")

if __name__ == "__main__":
    import sys
    
    dry_run = "--execute" not in sys.argv
    
    if not dry_run:
        print("=" * 80)
        print("WARNING: This will permanently delete duplicate issues!")
        print("=" * 80)
        print("Issues to delete:")
        if check_epic_links(DUPLICATE_EPIC["delete"]) == 0:
            print(f"  - Epic: {DUPLICATE_EPIC['delete']}")
        for task_info in DUPLICATE_TASKS:
            print(f"  - Task: {task_info['delete']} ({task_info['name']})")
        print()
        response = input("Are you sure you want to proceed? Type 'yes' to continue: ")
        if response.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    delete_duplicates(dry_run=dry_run)
