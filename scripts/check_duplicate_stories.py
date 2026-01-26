"""
Check if stories are duplicates by comparing summaries.
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

def check_duplicate_stories():
    """Check if stories are duplicates."""
    jira = JIRA(
        server=JIRA_SERVER_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    
    # Get stories from both epic sets
    older_epics = ["FRBP2-13", "FRBP2-14", "FRBP2-15", "FRBP2-16", "FRBP2-17", "FRBP2-18", 
                   "FRBP2-19", "FRBP2-20", "FRBP2-21", "FRBP2-22", "FRBP2-23", "FRBP2-24"]
    newer_epics = ["FRBP2-92", "FRBP2-93", "FRBP2-94", "FRBP2-95", "FRBP2-96", "FRBP2-97",
                   "FRBP2-98", "FRBP2-99", "FRBP2-100", "FRBP2-101", "FRBP2-102", "FRBP2-103"]
    
    print("=" * 80)
    print("CHECKING FOR DUPLICATE STORIES")
    print("=" * 80)
    print()
    
    # Get all stories from older epics
    older_stories = {}
    for epic_key in older_epics:
        try:
            jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
            issues = jira.search_issues(jql, maxResults=100)
            for issue in issues:
                older_stories[issue.fields.summary] = issue.key
        except:
            pass
    
    # Get all stories from newer epics
    newer_stories = {}
    duplicate_stories = []
    for epic_key in newer_epics:
        try:
            jql = f'project = {PROJECT_KEY} AND "Epic Link" = {epic_key}'
            issues = jira.search_issues(jql, maxResults=100)
            for issue in issues:
                summary = issue.fields.summary
                newer_stories[summary] = issue.key
                if summary in older_stories:
                    duplicate_stories.append({
                        'summary': summary,
                        'older_key': older_stories[summary],
                        'newer_key': issue.key
                    })
        except:
            pass
    
    if duplicate_stories:
        print(f"Found {len(duplicate_stories)} duplicate stories:")
        print()
        for dup in duplicate_stories[:10]:  # Show first 10
            print(f"  {dup['summary'][:60]}")
            print(f"    Older: {dup['older_key']}")
            print(f"    Newer: {dup['newer_key']}")
            print()
        if len(duplicate_stories) > 10:
            print(f"  ... and {len(duplicate_stories) - 10} more duplicates")
        print()
        print("=" * 80)
        print("RECOMMENDATION:")
        print("=" * 80)
        print("Since stories are duplicates, you can:")
        print("1. Keep the older epics (FRBP2-13-24) and their stories")
        print("2. Delete the newer epics (FRBP2-92-103) and their duplicate stories")
        print()
        print("Or keep the newer ones if they're more up-to-date.")
    else:
        print("No duplicate stories found - they're all unique!")
    
    return duplicate_stories

if __name__ == "__main__":
    check_duplicate_stories()
