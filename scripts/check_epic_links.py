"""
Check which epics have stories linked to them.
"""

import os
from dotenv import load_dotenv
from jira import JIRA

# Load credentials
env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

JIRA_SERVER_URL = os.getenv("JIRA_SERVER_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = "FRBP2"

def check_epic_links():
    """Check which epics have stories linked."""
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    # Check GDPR epics specifically
    gdpr_epics = ['FRBP2-104', 'FRBP2-105']
    
    print("Checking GDPR Compliance Implementation epics:")
    print("=" * 80)
    
    for epic_key in gdpr_epics:
        try:
            epic = jira.issue(epic_key)
            
            # Search for issues linked to this epic
            # Try different methods to find linked issues
            jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
            linked_issues = jira.search_issues(jql, maxResults=100)
            
            print(f"\nEpic: {epic_key} - {epic.fields.summary}")
            print(f"  Created: {epic.fields.created[:10]}")
            print(f"  Status: {epic.fields.status.name}")
            print(f"  Linked Issues: {len(linked_issues)}")
            
            if linked_issues:
                print(f"  Linked Stories:")
                for issue in linked_issues[:5]:  # Show first 5
                    print(f"    - {issue.key}: {issue.fields.summary[:60]}")
                if len(linked_issues) > 5:
                    print(f"    ... and {len(linked_issues) - 5} more")
        except Exception as e:
            print(f"  Error checking {epic_key}: {e}")
    
    print("\n" + "=" * 80)
    print("RECOMMENDATION:")
    print("=" * 80)
    print("Keep the epic that has the most linked stories.")
    print("Delete the one with fewer or no linked stories.")

if __name__ == "__main__":
    check_epic_links()
