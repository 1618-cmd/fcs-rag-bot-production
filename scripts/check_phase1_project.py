"""Check the FRBP (Phase 1) project and find the Phase 1 epic."""

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
print("CHECKING FRBP PROJECT (Phase 1)")
print("=" * 80)
print()

# Search for Phase 1 epic in FRBP project
jql = 'project = FRBP AND summary ~ "Phase 1"'
results = jira.search_issues(jql, maxResults=50)

if results:
    print(f"Found {len(results)} issue(s) in FRBP project matching 'Phase 1':")
    for issue in results:
        print(f"  {issue.key}: {issue.fields.summary} ({issue.fields.issuetype.name})")
        print(f"    Status: {issue.fields.status.name}")
        print()
else:
    print("No 'Phase 1' epic found in FRBP project.")
    print()

# Get all epics in FRBP project
print("All epics in FRBP project:")
jql_epics = "project = FRBP AND issuetype = Epic"
epics = jira.search_issues(jql_epics, maxResults=100)

if epics:
    print(f"Found {len(epics)} epic(s):")
    for epic in epics:
        print(f"  {epic.key}: {epic.fields.summary}")
        print(f"    Status: {epic.fields.status.name}")
        print()
else:
    print("No epics found in FRBP project.")
    print()

# Check current GDPR epic (FRBP2-105)
print("=" * 80)
print("CURRENT GDPR EPIC (FRBP2-105)")
print("=" * 80)
try:
    gdpr = jira.issue("FRBP2-105")
    print(f"Key: {gdpr.key}")
    print(f"Summary: {gdpr.fields.summary}")
    print(f"Project: {gdpr.fields.project.key}")
    print(f"Status: {gdpr.fields.status.name}")
    print()
    print("Note: FRBP2-105 is in FRBP2 project, not FRBP project.")
    print("To link it to Phase 1, we can:")
    print("  1. Create a link between the two epics (if Phase 1 epic exists)")
    print("  2. Move FRBP2-105 to FRBP project (requires admin permissions)")
    print("  3. Create a parent epic in FRBP and link FRBP2-105 to it")
except Exception as e:
    print(f"Error: {e}")
