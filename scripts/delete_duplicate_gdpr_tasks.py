"""Delete duplicate GDPR requirement tasks (FRBP2-161 to FRBP2-172)."""

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

# Tasks to delete (first set - not linked to epic)
TASKS_TO_DELETE = [
    "FRBP2-161", "FRBP2-162", "FRBP2-163", "FRBP2-164", "FRBP2-165", "FRBP2-166",
    "FRBP2-167", "FRBP2-168", "FRBP2-169", "FRBP2-170", "FRBP2-171", "FRBP2-172"
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
        print("  python scripts/delete_duplicate_gdpr_tasks.py --execute")
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
        print("WARNING: This will permanently delete 12 duplicate GDPR tasks!")
        print("=" * 80)
        print("Tasks to delete:")
        for task_key in TASKS_TO_DELETE:
            print(f"  - {task_key}")
        print()
        response = input("Are you sure you want to proceed? Type 'yes' to continue: ")
        if response.lower() != "yes":
            print("Cancelled.")
            sys.exit(0)
    
    delete_duplicate_tasks(dry_run=dry_run)
