"""
Recommend which duplicate epics to keep based on linked stories.
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

def recommend_epics_to_keep():
    """Recommend which duplicate epics to keep based on linked stories."""
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
        except:
            linked_count = 0
        
        epic_groups[epic.fields.summary].append({
            'key': epic.key,
            'created': epic.fields.created,
            'linked_count': linked_count
        })
    
    # Find duplicates
    duplicates = {name: epics for name, epics in epic_groups.items() if len(epics) > 1}
    
    print("=" * 80)
    print("EPIC DUPLICATES - KEEP vs DELETE (Based on Linked Stories)")
    print("=" * 80)
    print()
    
    keep_list = []
    delete_list = []
    
    if duplicates:
        for name, epic_list in sorted(duplicates.items()):
            # Sort by linked count (descending), then by created date (oldest first)
            sorted_epics = sorted(epic_list, key=lambda x: (-x['linked_count'], x['created']))
            
            # Keep the one with most linked stories (or oldest if tied)
            keep = sorted_epics[0]
            keep_list.append(keep['key'])
            
            # Mark all others for deletion
            to_delete = sorted_epics[1:]
            delete_list.extend([e['key'] for e in to_delete])
            
            print(f"Epic: {name}")
            print(f"  [KEEP] {keep['key']} (Linked: {keep['linked_count']}, Created: {keep['created'][:10]})")
            for epic in to_delete:
                print(f"  [DELETE] {epic['key']} (Linked: {epic['linked_count']}, Created: {epic['created'][:10]})")
            print()
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Epics to KEEP: {len(keep_list)}")
        print(f"Epics to DELETE: {len(delete_list)}")
        print()
        print("Epics to DELETE:")
        print(", ".join(sorted(delete_list)))
        print()
        print("=" * 80)
        print("NOTE:")
        print("=" * 80)
        print("The KEEP epics are the ones with the most linked stories.")
        print("You can delete the others in Jira manually or use bulk delete.")
    else:
        print("No duplicate epics found!")
    
    return keep_list, delete_list

if __name__ == "__main__":
    recommend_epics_to_keep()
