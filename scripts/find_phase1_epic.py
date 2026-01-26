"""Find the Phase 1 epic in Jira."""

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

# Search for Phase 1 epic
print("Searching for 'FCS RAG Bot - Phase 1' or similar...")
print("=" * 80)

# Search in current project
jql = 'project = FRBP2 AND summary ~ "Phase 1"'
results = jira.search_issues(jql, maxResults=50)

if results:
    print(f"Found {len(results)} issue(s) in FRBP2 project:")
    for issue in results:
        print(f"  {issue.key}: {issue.fields.summary} ({issue.fields.issuetype.name})")
else:
    print("No Phase 1 epic found in FRBP2 project.")
    print()
    print("Searching all projects...")
    
    # Search all projects
    jql_all = 'summary ~ "Phase 1" AND summary ~ "RAG Bot"'
    results_all = jira.search_issues(jql_all, maxResults=50)
    
    if results_all:
        print(f"Found {len(results_all)} issue(s) across all projects:")
        for issue in results_all:
            print(f"  {issue.key} ({issue.fields.project.key}): {issue.fields.summary} ({issue.fields.issuetype.name})")
    else:
        print("No Phase 1 epic found.")

print()
print("=" * 80)

# Also check if there's a parent epic field we can use
print("Checking if FRBP2-105 can have a parent epic...")
gdpr = jira.issue("FRBP2-105")
print(f"Current epic: {gdpr.key} - {gdpr.fields.summary}")
print(f"Issue type: {gdpr.fields.issuetype.name}")

# Check available fields
print("\nAvailable fields for linking:")
try:
    # Try to find parent or epic link fields
    if hasattr(gdpr.fields, 'parent'):
        print(f"  Parent field exists: {gdpr.fields.parent}")
    else:
        print("  No parent field found")
    
    # Check for custom fields that might be epic links
    print("\nCustom fields (sample):")
    for field_name in dir(gdpr.fields):
        if not field_name.startswith('_') and 'epic' in field_name.lower():
            print(f"  {field_name}")
except Exception as e:
    print(f"  Error checking fields: {e}")
