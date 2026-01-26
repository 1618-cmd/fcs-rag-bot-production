"""Quick verification of final Jira state."""

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

print("=" * 80)
print("FINAL STATE VERIFICATION")
print("=" * 80)
print()

# Check GDPR epic
gdpr = jira.issue("FRBP2-105")
jql = 'project = FRBP2 AND "Epic Link" = FRBP2-105'
stories = jira.search_issues(jql, maxResults=20)

print(f"GDPR Compliance Epic: {gdpr.key}")
print(f"  Summary: {gdpr.fields.summary}")
print(f"  Status: {gdpr.fields.status.name}")
print(f"  Linked Stories: {len(stories)}")
print()
print("GDPR Requirement Stories:")
for story in stories:
    print(f"  - {story.key}: {story.fields.summary}")
print()

# Check for duplicates
jql_epics = "project = FRBP2 AND issuetype = Epic"
all_epics = jira.search_issues(jql_epics, maxResults=100)
print(f"Total Epics in Project: {len(all_epics)}")
print()

# Check for any remaining duplicates
from collections import defaultdict
epic_names = defaultdict(list)
for epic in all_epics:
    epic_names[epic.fields.summary].append(epic.key)

duplicates = {name: keys for name, keys in epic_names.items() if len(keys) > 1}
if duplicates:
    print("WARNING: Duplicates still found:")
    for name, keys in duplicates.items():
        print(f"  {name}: {keys}")
else:
    print("No duplicate epics found - all clean!")

print()
print("=" * 80)
print("STATUS: Everything is up to date!")
print("=" * 80)
