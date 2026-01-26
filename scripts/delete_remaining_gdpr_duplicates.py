"""Delete remaining duplicate GDPR requirement tasks (FRBP2-256 through FRBP2-260)."""

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

# Remaining tasks to delete (newer duplicates from today's import)
TASKS_TO_DELETE = [
    "FRBP2-256",  # REQ-003 duplicate
    "FRBP2-257",  # REQ-004 duplicate
    "FRBP2-258",  # REQ-005 duplicate
    "FRBP2-259",  # REQ-006 duplicate
    "FRBP2-260",  # REQ-007 duplicate
]

def delete_duplicate_tasks(dry_run=True):
    """Delete duplicate GDPR tasks."""
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - No tasks will be deleted")
    else:
        print("LIVE MODE - Tasks will be permanently deleted!")
    print("=" * 80)
    print()
    
    deleted = []
    errors = []
    
    for task_key in TASKS_TO_DELETE:
        try:
            task = jira.issue(task_key)
            summary = task.fields.summary
            
            if dry_run:
                print(f"[WOULD DELETE] {task_key}: {summary}")
            else:
                task.delete()
                print(f"[DELETED] {task_key}: {summary}")
                deleted.append(task_key)
                
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {task_key} - Already deleted or does not exist")
            else:
                print(f"[ERROR] {task_key} - {error_msg}")
                errors.append((task_key, error_msg))
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    if dry_run:
        print(f"Would delete: {len(TASKS_TO_DELETE)} tasks")
        print()
        print("To actually delete, run:")
        print("  python scripts/delete_remaining_gdpr_duplicates.py --execute")
    else:
        print(f"Successfully deleted: {len(deleted)} tasks")
        if errors:
            print(f"Errors: {len(errors)}")
            for task_key, error in errors:
                print(f"  {task_key}: {error}")

if __name__ == "__main__":
    import sys
    
    dry_run = "--execute" not in sys.argv
    
    if not dry_run:
        print("=" * 80)
        print("WARNING: This will permanently delete 5 duplicate GDPR tasks!")
        print("=" * 80)
        print("Tasks to delete:")
        for task_key in TASKS_TO_DELETE:
            print(f"  - {task_key}")
        print()
        print("These are duplicates of FRBP2-175 through FRBP2-179")
        print("(which are already linked to the GDPR epic)")
        print()
        response = input("Are you sure you want to proceed? Type 'yes' to continue: ")
        if response.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    delete_duplicate_tasks(dry_run=dry_run)
