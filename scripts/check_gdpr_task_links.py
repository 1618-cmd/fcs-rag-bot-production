"""Check which GDPR requirement tasks are linked to FRBP2-105."""

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
GDPR_EPIC = "FRBP2-105"

print("=" * 80)
print("CHECKING GDPR TASK LINKS TO EPIC FRBP2-105")
print("=" * 80)
print()

# Get all tasks linked to GDPR epic
jql = f'project = {PROJECT_KEY} AND "Epic Link" = {GDPR_EPIC}'
linked_tasks = jira.search_issues(jql, maxResults=100)

print(f"Tasks linked to {GDPR_EPIC}: {len(linked_tasks)}")
print()

linked_keys = set()
for task in linked_tasks:
    linked_keys.add(task.key)
    print(f"  {task.key}: {task.fields.summary}")

print()

# Check both sets
first_set = [f"FRBP2-{i}" for i in range(161, 173)]  # 161-172
second_set = [f"FRBP2-{i}" for i in range(173, 185)]  # 173-184

print("First set (FRBP2-161 to FRBP2-172):")
first_linked = [key for key in first_set if key in linked_keys]
print(f"  Linked to epic: {len(first_linked)}/{len(first_set)}")
if first_linked:
    print(f"  Keys: {', '.join(first_linked)}")

print()
print("Second set (FRBP2-173 to FRBP2-184):")
second_linked = [key for key in second_set if key in linked_keys]
print(f"  Linked to epic: {len(second_linked)}/{len(second_set)}")
if second_linked:
    print(f"  Keys: {', '.join(second_linked)}")

print()
print("=" * 80)
print("RECOMMENDATION:")
print("=" * 80)

if len(second_linked) == 12:
    print("Keep: Second set (FRBP2-173 to FRBP2-184) - all linked to epic")
    print("Delete: First set (FRBP2-161 to FRBP2-172) - duplicates")
    delete_set = first_set
elif len(first_linked) == 12:
    print("Keep: First set (FRBP2-161 to FRBP2-172) - all linked to epic")
    print("Delete: Second set (FRBP2-173 to FRBP2-184) - duplicates")
    delete_set = second_set
else:
    print("Mixed linking - need to check manually")
    delete_set = []

if delete_set:
    print()
    print(f"Would delete: {', '.join(delete_set)}")
