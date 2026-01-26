"""
Script to find duplicate epics in Jira by name.
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

def find_duplicate_epics():
    """Find all duplicate epics by name."""
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    # Search for all epics in the project
    jql = f'project = {PROJECT_KEY} AND issuetype = Epic'
    epics = jira.search_issues(jql, maxResults=1000)
    
    # Group by summary
    epic_groups = defaultdict(list)
    for epic in epics:
        epic_groups[epic.fields.summary].append({
            'key': epic.key,
            'id': epic.id,
            'created': epic.fields.created,
            'updated': epic.fields.updated,
            'status': epic.fields.status.name
        })
    
    # Find duplicates
    duplicates = {name: epics for name, epics in epic_groups.items() if len(epics) > 1}
    
    print("=" * 80)
    print("DUPLICATE EPICS FOUND")
    print("=" * 80)
    print()
    
    if duplicates:
        for name, epic_list in duplicates.items():
            print(f"Epic: {name}")
            print(f"  Found {len(epic_list)} duplicates:")
            for epic in sorted(epic_list, key=lambda x: x['created']):
                print(f"    - {epic['key']} (Created: {epic['created'][:10]}, Status: {epic['status']})")
            print()
        
        print("=" * 80)
        print("RECOMMENDATION:")
        print("=" * 80)
        print("Keep the OLDEST epic (first created) and delete the newer duplicates.")
        print("The oldest one likely has the stories already linked to it.")
        print()
    else:
        print("No duplicate epics found!")
    
    return duplicates

if __name__ == "__main__":
    find_duplicate_epics()
