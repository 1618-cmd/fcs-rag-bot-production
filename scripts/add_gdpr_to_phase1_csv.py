"""Add FRBP2-105 (GDPR Compliance) epic to Phase 1.csv"""

import os
import csv
from datetime import datetime
from dotenv import load_dotenv
from jira import JIRA

env_file = "backend/.env"
if os.path.exists(env_file):
    load_dotenv(env_file)

jira = JIRA(
    server=os.getenv("JIRA_SERVER_URL"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

# Get GDPR epic details
print("Fetching FRBP2-105 details from Jira...")
gdpr = jira.issue("FRBP2-105")

# Read existing CSV
csv_path = "docs/Phase 1.csv"
print(f"Reading {csv_path}...")

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Prepare new row for GDPR epic
# Format dates
created = datetime.strptime(gdpr.fields.created[:10], "%Y-%m-%d").strftime("%d/%b/%y %I:%M %p")
updated = datetime.strptime(gdpr.fields.updated[:10], "%Y-%m-%d").strftime("%d/%b/%y %I:%M %p")

# Get priority
priority = getattr(gdpr.fields, 'priority', None)
priority_name = priority.name if priority else "Medium"

# Get description
description = getattr(gdpr.fields, 'description', '') or 'Epic: GDPR Compliance Implementation'

# Get assignee info
assignee = getattr(gdpr.fields, 'assignee', None)
assignee_name = assignee.displayName if assignee else ""
assignee_id = assignee.accountId if assignee else ""

# Get reporter info
reporter = getattr(gdpr.fields, 'reporter', None)
reporter_name = reporter.displayName if reporter else ""
reporter_id = reporter.accountId if reporter else ""

# Get creator info (same as reporter usually)
creator_name = reporter_name
creator_id = reporter_id

# Get project info
project = gdpr.fields.project
project_key = project.key
project_name = project.name
project_lead = getattr(project, 'lead', None)
project_lead_name = project_lead.displayName if project_lead else ""
project_lead_id = project_lead.accountId if project_lead else ""

# Get watchers
watchers = getattr(gdpr.fields, 'watcher', None)
watchers_name = watchers.displayName if watchers else ""
watchers_id = watchers.accountId if watchers else ""

# Get status category
status_category = gdpr.fields.status.statusCategory.key if hasattr(gdpr.fields.status, 'statusCategory') else "new"
status_category_changed = created

# Create new row
new_row = {
    'Summary': gdpr.fields.summary,
    'Issue key': gdpr.key,
    'Issue id': gdpr.id,
    'Issue Type': gdpr.fields.issuetype.name,
    'Status': gdpr.fields.status.name,
    'Project key': project_key,
    'Project name': project_name,
    'Project type': getattr(project, 'projectTypeKey', 'software'),
    'Project lead': project_lead_name,
    'Project lead id': project_lead_id,
    'Project description': '',
    'Priority': priority_name,
    'Resolution': '',
    'Assignee': assignee_name,
    'Assignee Id': assignee_id,
    'Reporter': reporter_name,
    'Reporter Id': reporter_id,
    'Creator': creator_name,
    'Creator Id': creator_id,
    'Created': created,
    'Updated': updated,
    'Last Viewed': '',
    'Resolved': '',
    'Due date': '',
    'Votes': '0',
    'Description': description,
    'Environment': '',
    'Watchers': watchers_name,
    'Watchers Id': watchers_id,
    'Original estimate': '',
    'Remaining Estimate': '',
    'Time Spent': '',
    'Work Ratio': '',
    'Σ Original Estimate': '',
    'Σ Remaining Estimate': '',
    'Σ Time Spent': '',
    'Security Level': '',
    'Attachment': '',
    'Custom field (Development)': '',
    'Custom field (Issue color)': '',
    'Custom field (Rank)': '',
    'Custom field (Start date)': '',
    'Custom field (Team)': '',
    'Custom field (Vulnerability)': '',
    'Status Category': status_category,
    'Status Category Changed': status_category_changed
}

# Add any missing fields (set to empty string)
for field in fieldnames:
    if field not in new_row:
        new_row[field] = ''

# Ensure row has all fields in correct order
ordered_row = {field: new_row.get(field, '') for field in fieldnames}

# Add to rows
rows.append(ordered_row)

# Write back to CSV
print(f"Writing updated CSV to {csv_path}...")
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {gdpr.key} ({gdpr.fields.summary}) to Phase 1.csv")
print(f"   Total rows: {len(rows)}")
