# Report Prompts for Monthly Breakdowns and Detail Levels in Vena Copilot

## Overview

When Vena Copilot generates reports, it may default to showing summary-level data (e.g., Full Year totals) instead of detailed breakdowns (e.g., monthly periods). This guide explains how to use Report Prompts to control the level of detail in reports, specifically focusing on changing from Full Year to monthly breakdowns.

## The Problem: Reports Showing Wrong Detail Level

### Common Scenario

**User Request:** "Create a revenue report for 2024"

**What Copilot Generates:**
- Report shows Full Year totals only
- No monthly breakdown (January, February, March, etc.)

**What User Wants:**
- Monthly breakdown showing revenue for each month (January through December)

### Why This Happens

1. **Assumed Member Default**: If the Period dimension Assumed Member is set to "Full Year", Copilot defaults to showing full year totals when users don't specify a period
2. **No Report Prompt**: Without a Report Prompt, Copilot uses default report formatting
3. **Period Dimension Mapping**: The report may be mapping Period dimension at the parent level (Full Year) instead of the child level (individual months)

## The Solution: Report Prompts

Report Prompts allow you to customize how Vena Copilot generates reports, including the level of detail. When you create a Report Prompt that specifies monthly breakdowns, Copilot will use that format for similar report requests.

## Step-by-Step: Creating a Report Prompt for Monthly Breakdowns

### Method 1: From an Existing Report (Recommended)

If Copilot has already generated a report that shows Full Year instead of monthly breakdowns:

1. **Navigate to Vena Copilot → Builder → Select AI Model → Chats Tab**
2. **Find the chat** where the report was generated
3. **Select View Chat** to see the full conversation
4. **Select the Create Prompt icon** under the report request
5. **Open the report** from your downloads folder (it will open in Vena Ad Hoc)
6. **A feedback message appears** - Select **Modify** (not Keep, since the report needs changes)
7. **In Vena Ad Hoc, modify the Period dimension mapping**:
   - Find the Period dimension in the report
   - Change from `'full year'` to `bottomlevel('full year')`
   - This tells Copilot to show all months (January through December) instead of just the Full Year total
8. **Select Refresh Data** to update the report with the new mapping
9. **Select Vena Copilot** (notification icon appears)
10. **Select Keep** in the feedback message to save this as a Report Prompt

### Method 2: From a New Chat

If you want to create a Report Prompt proactively:

1. **Start a chat with Vena Copilot**
2. **Ask Copilot to create a report** (e.g., "Create a revenue report for 2024")
3. **Select Download Report** and open it in Vena Ad Hoc
4. **If the report shows Full Year instead of monthly breakdowns, select Modify**
5. **Change the Period dimension** from `'full year'` to `bottomlevel('full year')`
6. **Select Refresh Data**
7. **Select Vena Copilot** (notification icon)
8. **Select Keep** to save as a Report Prompt

## Understanding `bottomlevel('full year')`

### What It Means

- **`'full year'`**: Shows only the Full Year total (parent member)
- **`bottomlevel('full year')`**: Shows all bottom-level children of Full Year (January, February, March, etc.)

### When to Use

Use `bottomlevel('full year')` when you want:
- Monthly breakdowns instead of annual totals
- Quarterly breakdowns (if your Period dimension has quarters)
- Any child-level detail instead of parent-level summary

### Example Period Dimension Hierarchy

```
Period Dimension:
  ├── All Periods
  │     └── Full Year
  │           ├── Q1
  │           │     ├── January
  │           │     ├── February
  │           │     └── March
  │           ├── Q2
  │           │     ├── April
  │           │     ├── May
  │           │     └── June
  │           ├── Q3
  │           │     ├── July
  │           │     ├── August
  │           │     └── September
  │           └── Q4
  │                 ├── October
  │                 ├── November
  │                 └── December
```

**Using `bottomlevel('full year')`** will show: January, February, March, April, May, June, July, August, September, October, November, December

**Using `'full year'`** will show: Full Year (total only)

## Other Detail Level Options

### Quarterly Breakdowns

If you want quarterly breakdowns instead of monthly:

- Change Period from `'full year'` to `children('full year')` or specific quarters like `'Q1'`, `'Q2'`, etc.

### Department Breakdowns

If you want department-level breakdowns:

- Add Department dimension to the report mapping
- Use `children('All Departments')` or `bottomlevel('All Departments')` to show all departments

### Account Breakdowns

If you want account-level breakdowns:

- Add Account dimension to the report mapping
- Use `children('Total Revenue')` or `bottomlevel('Total Revenue')` to show all revenue accounts

## Editing Existing Report Prompts

If you need to modify an existing Report Prompt:

1. **Navigate to Vena Copilot → Builder → Select AI Model → Prompt Library Tab**
2. **Find the Report Prompt** you want to edit
3. **Select Refine Prompt** from the actions menu
4. **Open the report** in Vena Ad Hoc
5. **Select Modify** to make changes
6. **Update the Period dimension** or other mappings as needed
7. **Select Refresh Data**
8. **Select Vena Copilot** (notification icon)
9. **Select Yes** to save the updated Prompt

## Best Practices

1. **Create Prompts for Common Report Types**: If users frequently request monthly breakdowns, create a Report Prompt for that format
2. **Use Descriptive Prompts**: When creating Prompts, ensure the original query is clear (e.g., "Create a monthly revenue report for 2024")
3. **Test Prompts**: After creating a Prompt, test it by asking a similar question to verify it works correctly
4. **Review Chat Logs**: Periodically review chat logs to identify common report requests that need Prompts
5. **Document Prompt Purpose**: Use clear naming in the Prompt Library so other admins understand what each Prompt does

## Troubleshooting

### Issue: Report Still Shows Full Year After Creating Prompt

**Problem:** You created a Report Prompt but reports still show Full Year totals

**Solution:**
- Verify the Prompt was saved correctly (check Prompt Library)
- Ensure the user's query matches the Prompt query closely
- Check that `bottomlevel('full year')` was used, not just `'full year'`
- Try refining the existing Prompt to ensure changes were saved

### Issue: Prompt Not Matching User Queries

**Problem:** Users ask for monthly reports but the Prompt doesn't apply

**Solution:**
- Ensure the user's query wording is similar to the Prompt query
- Create multiple Prompts for different phrasings (e.g., "monthly revenue report", "revenue by month", "revenue breakdown by month")
- Review chat logs to see how users phrase their requests

### Issue: Report Shows Too Much Detail

**Problem:** Report shows individual months when you want quarterly summaries

**Solution:**
- Modify the Report Prompt to use `children('full year')` instead of `bottomlevel('full year')`
- Or map to specific quarters (Q1, Q2, Q3, Q4) instead of months

## Relationship to Assumed Members

### Important Distinction

- **Assumed Members**: Set defaults for when users don't specify a dimension member (e.g., if Period isn't mentioned, use "Full Year")
- **Report Prompts**: Override defaults and specify exact report formatting, including detail levels

**Key Point:** Report Prompts take precedence over Assumed Members for report formatting. Even if the Period Assumed Member is "Full Year", a Report Prompt can specify monthly breakdowns.

### When Both Are Needed

- **Assumed Member**: Ensures Copilot knows which period to use when not specified
- **Report Prompt**: Ensures the report shows the correct level of detail (monthly vs full year)

## Summary

- **Problem**: Reports show Full Year totals instead of monthly breakdowns
- **Solution**: Create a Report Prompt that changes Period from `'full year'` to `bottomlevel('full year')`
- **Process**: Generate report → Modify in Vena Ad Hoc → Change Period mapping → Refresh Data → Save as Prompt
- **Result**: Future similar report requests will automatically show monthly breakdowns
- **Best Practice**: Create Prompts for common report formats to ensure consistent, detailed reporting

By following this guide, you can ensure that Vena Copilot generates reports with the correct level of detail, providing monthly breakdowns when needed instead of just summary totals.
