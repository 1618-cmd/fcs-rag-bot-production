"""Delete duplicate epics that have no linked stories."""

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

duplicate_epics = [
    {"keep": "FRBP2-13", "delete": "FRBP2-185", "name": "Prompt Versioning & Management System"},
    {"keep": "FRBP2-14", "delete": "FRBP2-186", "name": "Sentry Integration with Prompt Breadcrumbs"},
    {"keep": "FRBP2-15", "delete": "FRBP2-187", "name": "Prompt Context Injection & Templating System"},
    {"keep": "FRBP2-16", "delete": "FRBP2-188", "name": "Prompt Engineering & Optimization Framework"},
    {"keep": "FRBP2-17", "delete": "FRBP2-189", "name": "Enhanced Document Management System"},
]

print("=" * 80)
print("DELETING DUPLICATE EPICS")
print("=" * 80)
print()

deleted = []
errors = []

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

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Successfully deleted: {len(deleted)} epics")
if errors:
    print(f"Errors: {len(errors)}")
    for epic_key, error in errors:
        print(f"  {epic_key}: {error}")
