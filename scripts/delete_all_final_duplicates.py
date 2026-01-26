"""Delete all remaining duplicate epics and tasks."""

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

def check_epic_links(epic_key):
    """Check how many stories are linked to an epic."""
    try:
        jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
        linked = jira.search_issues(jql, maxResults=100)
        return len(linked)
    except:
        return 0

# Duplicate epics to check
duplicate_epics = [
    {"keep": "FRBP2-23", "delete": "FRBP2-195", "name": "Advanced Prompt Features"},
    {"keep": "FRBP2-24", "delete": "FRBP2-196", "name": "Monitoring & Analytics Dashboards"},
]

# Duplicate tasks to delete
duplicate_tasks = [
    "FRBP2-199",  # Create prompt versioning database schema
    "FRBP2-200",  # Create prompt management service
    "FRBP2-201",  # Add prompt version tracking to query logs
]

print("=" * 80)
print("DELETING ALL REMAINING DUPLICATES")
print("=" * 80)
print()

deleted = []
errors = []

# Check and delete duplicate epics
for epic_info in duplicate_epics:
    keep_links = check_epic_links(epic_info["keep"])
    delete_links = check_epic_links(epic_info["delete"])
    
    print(f"Epic {epic_info['keep']}: {keep_links} linked stories")
    print(f"Epic {epic_info['delete']}: {delete_links} linked stories")
    
    if delete_links == 0:
        try:
            epic = jira.issue(epic_info["delete"])
            epic.delete()
            print(f"[DELETED] Epic {epic_info['delete']}: {epic_info['name']}")
            deleted.append(epic_info["delete"])
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                print(f"[SKIP] {epic_info['delete']} - Already deleted")
            else:
                print(f"[ERROR] {epic_info['delete']} - {error_msg}")
                errors.append((epic_info["delete"], error_msg))
    else:
        print(f"[SKIP] Epic {epic_info['delete']} - Has {delete_links} linked stories")
    print()

# Delete duplicate tasks
for task_key in duplicate_tasks:
    try:
        task = jira.issue(task_key)
        summary = task.fields.summary
        task.delete()
        print(f"[DELETED] {task_key}: {summary}")
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
print(f"Successfully deleted: {len(deleted)} issues")
if errors:
    print(f"Errors: {len(errors)}")
    for issue_key, error in errors:
        print(f"  {issue_key}: {error}")
