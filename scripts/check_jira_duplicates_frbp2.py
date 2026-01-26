"""Check for duplicate epics and tasks in FRBP2 Jira project."""

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

print("=" * 80)
print("CHECKING FOR DUPLICATES IN FRBP2 JIRA PROJECT")
print("=" * 80)
print()

# Get all issues
jql = f'project = {PROJECT_KEY} ORDER BY created DESC'
all_issues = jira.search_issues(jql, maxResults=1000)

print(f"Total issues in project: {len(all_issues)}")
print()

# Group by summary
epic_groups = defaultdict(list)
task_groups = defaultdict(list)

for issue in all_issues:
    summary = issue.fields.summary
    issue_type = issue.fields.issuetype.name
    
    entry = {
        'key': issue.key,
        'created': issue.fields.created,
        'status': issue.fields.status.name
    }
    
    if issue_type == 'Epic':
        epic_groups[summary].append(entry)
    else:
        task_groups[summary].append(entry)

# Find duplicate epics
duplicate_epics = {name: epics for name, epics in epic_groups.items() if len(epics) > 1}
duplicate_tasks = {name: tasks for name, tasks in task_groups.items() if len(tasks) > 1}

print("=" * 80)
print("DUPLICATE EPICS")
print("=" * 80)
if duplicate_epics:
    print(f"Found {len(duplicate_epics)} duplicate epic summaries:")
    print()
    for name, epics in sorted(duplicate_epics.items()):
        print(f"Epic: {name}")
        print("-" * 80)
        for epic in sorted(epics, key=lambda x: x['created']):
            print(f"  {epic['key']}:")
            print(f"    Created: {epic['created'][:10]}")
            print(f"    Status: {epic['status']}")
        print()
else:
    print("No duplicate epics found!")
    print()

print("=" * 80)
print("DUPLICATE TASKS/STORIES")
print("=" * 80)
if duplicate_tasks:
    print(f"Found {len(duplicate_tasks)} duplicate task/story summaries:")
    print()
    for name, tasks in sorted(duplicate_tasks.items()):
        print(f"Task: {name}")
        print("-" * 80)
        for task in sorted(tasks, key=lambda x: x['created']):
            print(f"  {task['key']}:")
            print(f"    Created: {task['created'][:10]}")
            print(f"    Status: {task['status']}")
        print()
else:
    print("No duplicate tasks/stories found!")
    print()

# Summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total epics: {len(epic_groups)}")
print(f"Total tasks/stories: {len(task_groups)}")
print(f"Duplicate epics: {len(duplicate_epics)}")
print(f"Duplicate tasks: {len(duplicate_tasks)}")

if duplicate_epics or duplicate_tasks:
    total_duplicate_issues = sum(len(epics) for epics in duplicate_epics.values()) + sum(len(tasks) for tasks in duplicate_tasks.values())
    unique_duplicates = len(duplicate_epics) + len(duplicate_tasks)
    print(f"Total duplicate issues: {total_duplicate_issues}")
    print(f"Would need to delete: {total_duplicate_issues - unique_duplicates} issues")
else:
    print("No duplicates found - all clean!")
