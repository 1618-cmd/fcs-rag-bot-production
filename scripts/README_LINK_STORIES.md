# Link Stories to Epics - Script Guide

## Overview
This script automatically links all Jira stories/tasks to their parent epics after importing from CSV.

## Prerequisites
1. Jira API token (get from: https://id.atlassian.com/manage-profile/security/api-tokens)
2. Jira credentials configured in `.env` OR you'll be prompted

## How to Run

### Option 1: Using Config (Recommended)
If your `backend/.env` has Jira credentials configured:

```bash
cd backend
python ../scripts/link_stories_to_epics.py
```

### Option 2: Manual Credentials
If not configured, the script will prompt you:

```bash
cd backend
python ../scripts/link_stories_to_epics.py
# Enter your Jira email when prompted
# Enter your Jira API token when prompted
```

## What It Does

1. **Reads CSV**: Loads epic-story mappings from `docs/Phase Jira.csv`
2. **Finds Epics**: Searches Jira for all 12 epics by summary
3. **Finds Stories**: Searches Jira for all 55 stories/tasks by summary
4. **Links Them**: Automatically links each story to its parent epic

## Expected Output

```
✅ Connected to Jira: https://waitemiles.atlassian.net
Loaded mappings for 12 epics
  Prompt Versioning & Management System: 5 stories
  Sentry Integration with Prompt Breadcrumbs: 4 stories
  ...

Finding epics in Jira...
Found epic: FRBP2-1 = Prompt Versioning & Management System
...

Linking stories to epics...
✅ Linked FRBP2-13 to epic FRBP2-1 using field 'customfield_10014'
✅ Linked FRBP2-14 to epic FRBP2-1 using field 'customfield_10014'
...

Linking Complete!
✅ Successfully linked: 55 stories
❌ Failed to link: 0 stories
```

## Troubleshooting

### "Epic Link field not found"
- The script will try multiple field names automatically
- If it fails, check your Jira project's Epic Link field name
- You may need to manually link a few stories to discover the field name

### "Story not found"
- Story summary might not match exactly
- Check the story exists in Jira
- Verify the CSV has the correct summary

### "Could not link"
- Check you have permissions to edit issues
- Verify the epic key is correct
- Try linking one manually in Jira to see the field name

## Notes

- The script is idempotent - safe to run multiple times
- It will skip stories that are already linked
- Progress is logged to console
