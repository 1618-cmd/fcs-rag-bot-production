"""
Script to identify which duplicate epics should be deleted.
Keeps the oldest epic and marks newer ones for deletion.
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

def identify_duplicates_to_delete():
    """Identify which duplicate epics should be deleted."""
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
        # Get linked issues count
        try:
            linked_count = len(epic.fields.subtasks) if hasattr(epic.fields, 'subtasks') else 0
        except:
            linked_count = 0
        
        epic_groups[epic.fields.summary].append({
            'key': epic.key,
            'id': epic.id,
            'created': epic.fields.created,
            'updated': epic.fields.updated,
            'status': epic.fields.status.name,
            'linked_count': linked_count
        })
    
    # Find duplicates and determine which to keep/delete
    duplicates = {name: epics for name, epics in epic_groups.items() if len(epics) > 1}
    
    print("=" * 80)
    print("DUPLICATE EPICS - KEEP vs DELETE")
    print("=" * 80)
    print()
    
    keep_list = []
    delete_list = []
    
    if duplicates:
        for name, epic_list in sorted(duplicates.items()):
            # Sort by created date (oldest first)
            sorted_epics = sorted(epic_list, key=lambda x: x['created'])
            
            # Keep the oldest one
            keep = sorted_epics[0]
            keep_list.append(keep['key'])
            
            # Mark all others for deletion
            to_delete = sorted_epics[1:]
            delete_list.extend([e['key'] for e in to_delete])
            
            print(f"Epic: {name}")
            print(f"  [KEEP] {keep['key']} (Created: {keep['created'][:10]}, Linked: {keep['linked_count']})")
            for epic in to_delete:
                print(f"  [DELETE] {epic['key']} (Created: {epic['created'][:10]}, Linked: {epic['linked_count']})")
            print()
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Epics to KEEP: {len(keep_list)}")
        print(f"Epics to DELETE: {len(delete_list)}")
        print()
        print("Epics to DELETE (copy these keys):")
        print(", ".join(sorted(delete_list)))
        print()
        print("=" * 80)
        print("NOTE:")
        print("=" * 80)
        print("Before deleting, verify that the stories are linked to the KEEP epics.")
        print("If stories are linked to DELETE epics, you'll need to relink them first.")
        print()
    else:
        print("No duplicate epics found!")
    
    return keep_list, delete_list

if __name__ == "__main__":
    identify_duplicates_to_delete()
