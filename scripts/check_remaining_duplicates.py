"""
Check remaining duplicate epics and their linked stories.
"""

import os
from dotenv import load_dotenv
from jira import JIRA
from collections import defaultdict

# Load credentials
env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

JIRA_SERVER_URL = os.getenv("JIRA_SERVER_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = "FRBP2"

def check_remaining_duplicates():
    """Check remaining duplicate epics."""
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    # Search for all epics
    jql = f'project = {PROJECT_KEY} AND issuetype = Epic'
    epics = jira.search_issues(jql, maxResults=1000)
    
    # Group by summary
    epic_groups = defaultdict(list)
    for epic in epics:
        # Count linked issues
        try:
            jql_linked = f'project = {PROJECT_KEY} AND "Epic Link" = {epic.key}'
            linked_issues = jira.search_issues(jql_linked, maxResults=100)
            linked_count = len(linked_issues)
            linked_keys = [issue.key for issue in linked_issues[:5]]  # First 5
        except:
            linked_count = 0
            linked_keys = []
        
        epic_groups[epic.fields.summary].append({
            'key': epic.key,
            'created': epic.fields.created,
            'linked_count': linked_count,
            'linked_keys': linked_keys
        })
    
    # Find duplicates
    duplicates = {name: epics for name, epics in epic_groups.items() if len(epics) > 1}
    
    print("=" * 80)
    print("REMAINING DUPLICATE EPICS")
    print("=" * 80)
    print()
    
    if duplicates:
        for name, epic_list in sorted(duplicates.items()):
            print(f"Epic: {name}")
            print("-" * 80)
            for epic in sorted(epic_list, key=lambda x: x['created']):
                print(f"  {epic['key']}:")
                print(f"    Created: {epic['created'][:10]}")
                print(f"    Linked Stories: {epic['linked_count']}")
                if epic['linked_keys']:
                    print(f"    Sample: {', '.join(epic['linked_keys'])}")
            print()
        
        print("=" * 80)
        print("RECOMMENDATION:")
        print("=" * 80)
        print("For each duplicate set, keep the one with the most linked stories.")
        print("If tied, keep the older one (first created).")
    else:
        print("No duplicate epics found! All duplicates have been cleaned up.")
    
    return duplicates

if __name__ == "__main__":
    check_remaining_duplicates()
