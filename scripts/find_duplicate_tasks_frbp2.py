"""Find duplicate tasks/stories in FRBP2 project."""

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
print("CHECKING FOR DUPLICATE TASKS/STORIES IN FRBP2")
print("=" * 80)
print()

# Get all issues (not epics) in FRBP2
jql = f'project = {PROJECT_KEY} AND issuetype != Epic ORDER BY created DESC'
all_issues = jira.search_issues(jql, maxResults=1000)

print(f"Total issues (non-epics) in FRBP2: {len(all_issues)}")
print()

# Group by summary
issue_groups = defaultdict(list)
for issue in all_issues:
    summary = issue.fields.summary
    issue_groups[summary].append({
        'key': issue.key,
        'created': issue.fields.created,
        'status': issue.fields.status.name,
        'issuetype': issue.fields.issuetype.name,
        'epic_link': getattr(issue.fields, 'customfield_10014', None) or 
                     getattr(issue.fields, 'customfield_10011', None) or
                     'N/A'
    })

# Find duplicates
duplicates = {summary: issues for summary, issues in issue_groups.items() if len(issues) > 1}

if duplicates:
    print(f"Found {len(duplicates)} duplicate task/story summaries:")
    print()
    
    for summary, issues in sorted(duplicates.items()):
        print(f"Summary: {summary}")
        print("-" * 80)
        for issue in sorted(issues, key=lambda x: x['created']):
            print(f"  {issue['key']}:")
            print(f"    Type: {issue['issuetype']}")
            print(f"    Status: {issue['status']}")
            print(f"    Created: {issue['created'][:10]}")
            print(f"    Epic Link: {issue['epic_link']}")
        print()
    
    print("=" * 80)
    print("RECOMMENDATION:")
    print("=" * 80)
    print("For each duplicate set, keep the one that:")
    print("  1. Is linked to the correct epic")
    print("  2. Has the most recent updates")
    print("  3. Is older (if they're identical)")
    print()
    
    # Count total duplicates
    total_duplicate_issues = sum(len(issues) for issues in duplicates.values())
    total_unique = len(duplicates)
    print(f"Total duplicate issues: {total_duplicate_issues}")
    print(f"Unique summaries with duplicates: {total_unique}")
    print(f"Would need to delete: {total_duplicate_issues - total_unique} issues")
else:
    print("No duplicate tasks/stories found!")
