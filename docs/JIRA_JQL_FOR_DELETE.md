# Jira JQL Queries for Deleting Duplicate Epics

## JQL Queries for Bulk Delete

You can use these JQL queries in Jira to find and delete duplicate epics.

### Option 1: Delete by Issue Key (Recommended)

Use this JQL query to find all the duplicate epics:

```
project = FRBP2 AND issuetype = Epic AND key IN (FRBP2-1, FRBP2-2, FRBP2-3, FRBP2-4, FRBP2-5, FRBP2-6, FRBP2-7, FRBP2-8, FRBP2-9, FRBP2-10, FRBP2-11, FRBP2-12, FRBP2-80, FRBP2-81, FRBP2-82, FRBP2-83, FRBP2-84, FRBP2-85, FRBP2-86, FRBP2-87, FRBP2-88, FRBP2-89, FRBP2-90, FRBP2-91, FRBP2-92, FRBP2-93, FRBP2-94, FRBP2-95, FRBP2-96, FRBP2-97, FRBP2-98, FRBP2-99, FRBP2-100, FRBP2-101, FRBP2-102, FRBP2-103, FRBP2-104)
```

### Option 2: Delete Epics Created on 2026-01-25 (Newer Duplicates)

If you want to delete only the newer duplicates from today's import:

```
project = FRBP2 AND issuetype = Epic AND created >= "2026-01-25" AND key IN (FRBP2-80, FRBP2-81, FRBP2-82, FRBP2-83, FRBP2-84, FRBP2-85, FRBP2-86, FRBP2-87, FRBP2-88, FRBP2-89, FRBP2-90, FRBP2-91, FRBP2-92, FRBP2-93, FRBP2-94, FRBP2-95, FRBP2-96, FRBP2-97, FRBP2-98, FRBP2-99, FRBP2-100, FRBP2-101, FRBP2-102, FRBP2-103, FRBP2-104)
```

**IMPORTANT:** Exclude FRBP2-105 from deletion (it has the GDPR stories linked)!

### Option 3: Delete Epics with No Linked Stories

Delete epics that have no stories linked to them:

```
project = FRBP2 AND issuetype = Epic AND key IN (FRBP2-1, FRBP2-2, FRBP2-3, FRBP2-4, FRBP2-5, FRBP2-6, FRBP2-7, FRBP2-8, FRBP2-9, FRBP2-10, FRBP2-11, FRBP2-12, FRBP2-80, FRBP2-81, FRBP2-82, FRBP2-83, FRBP2-84, FRBP2-85, FRBP2-86, FRBP2-87, FRBP2-88, FRBP2-89, FRBP2-90, FRBP2-91, FRBP2-92, FRBP2-93, FRBP2-94, FRBP2-95, FRBP2-96, FRBP2-97, FRBP2-98, FRBP2-99, FRBP2-100, FRBP2-101, FRBP2-102, FRBP2-103, FRBP2-104)
```

## How to Use in Jira

1. Go to Jira → Issues → Search for issues
2. Paste one of the JQL queries above
3. Click "Search"
4. Select all results (checkbox at top)
5. Click "Tools" → "Bulk Change"
6. Choose "Delete Issues"
7. Confirm deletion

## Epics to KEEP (Do NOT Delete)

These epics have linked stories and should be kept:

- FRBP2-13: Prompt Versioning & Management System
- FRBP2-14: Sentry Integration with Prompt Breadcrumbs
- FRBP2-15: Prompt Context Injection & Templating System
- FRBP2-16: Prompt Engineering & Optimization Framework
- FRBP2-17: Enhanced Document Management System
- FRBP2-18: Vena API Integration & Data Pulling
- FRBP2-19: LLM Provider Compatibility Fixes
- FRBP2-20: Infrastructure & Code Quality Improvements
- FRBP2-21: Testing & Quality Assurance
- FRBP2-22: Documentation & Knowledge Base Updates
- FRBP2-23: Advanced Prompt Features
- FRBP2-24: Monitoring & Analytics Dashboards
- **FRBP2-105: GDPR Compliance Implementation** (has 12 linked stories)

## Using the Python Script

Alternatively, you can use the Python script:

```powershell
# Dry run (shows what would be deleted)
python scripts/delete_duplicate_epics.py

# Actually delete (requires confirmation)
python scripts/delete_duplicate_epics.py --execute
```

The script includes safety checks:
- Verifies each issue is an Epic
- Checks if epics have linked stories (skips if they do)
- Requires explicit confirmation before deleting
