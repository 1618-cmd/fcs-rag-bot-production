"""Delete all remaining duplicate tasks from today's import."""

import os
from dotenv import load_dotenv
from jira import JIRA
from collections import defaultdict

env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

jira = JIRA(
    server=os.getenv("JIRA_SERVER_URL"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

PROJECT_KEY = "FRBP2"

# Get all issues
jql = f'project = {PROJECT_KEY} ORDER BY created DESC'
all_issues = jira.search_issues(jql, maxResults=1000)

# Group by summary
task_groups = defaultdict(list)
for issue in all_issues:
    if issue.fields.issuetype.name != 'Epic':
        summary = issue.fields.summary
        task_groups[summary].append({
            'key': issue.key,
            'created': issue.fields.created
        })

# Find duplicates (keep oldest, delete newer)
duplicates_to_delete = []
for summary, tasks in task_groups.items():
    if len(tasks) > 1:
        # Sort by created date (oldest first)
        sorted_tasks = sorted(tasks, key=lambda x: x['created'])
        # Keep the oldest, delete the rest
        for task in sorted_tasks[1:]:
            duplicates_to_delete.append(task['key'])

print("=" * 80)
print("DELETING ALL REMAINING DUPLICATES")
print("=" * 80)
print(f"Found {len(duplicates_to_delete)} duplicate tasks to delete")
print()

deleted = []
errors = []

for task_key in duplicates_to_delete:
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
print(f"Successfully deleted: {len(deleted)} tasks")
if errors:
    print(f"Errors: {len(errors)}")
    for task_key, error in errors:
        print(f"  {task_key}: {error}")
