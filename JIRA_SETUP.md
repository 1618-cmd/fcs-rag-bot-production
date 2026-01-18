# Jira Integration Setup Guide

This guide explains how to configure the FCS RAG Bot to create Jira tickets when users need additional support.

## Overview

The Jira integration allows users to create support tickets directly from the chat interface when:
- The bot cannot answer their question
- They need additional help beyond what the bot provides
- They want to escalate an issue

## Prerequisites

1. **Jira Account**: You need access to a Jira instance (cloud or server)
2. **Jira Project**: A project where tickets will be created (e.g., "SUPPORT")
3. **API Token**: A Jira API token for authentication

## Step 1: Get Your Jira API Token

1. Go to: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **"Create API token"**
3. Give it a label (e.g., "FCS RAG Bot")
4. Copy the token (you'll only see it once!)

## Step 2: Configure Environment Variables

Add these to your `.env` file (or Render environment variables):

```bash
# Jira Configuration
JIRA_SERVER_URL=https://yourcompany.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_API_TOKEN=your-api-token-from-step-1
JIRA_PROJECT_KEY=SUPPORT
JIRA_ISSUE_TYPE=Task
JIRA_LABELS=rag-bot,support
```

### Configuration Details

- **JIRA_SERVER_URL**: Your Jira instance URL (e.g., `https://yourcompany.atlassian.net`)
- **JIRA_EMAIL**: The email address of your Jira account
- **JIRA_API_TOKEN**: The API token you created in Step 1
- **JIRA_PROJECT_KEY**: The project key where tickets will be created (e.g., "SUPPORT", "HELP")
- **JIRA_ISSUE_TYPE**: The type of issue to create (e.g., "Task", "Bug", "Story")
- **JIRA_LABELS**: Comma-separated labels to add to tickets (e.g., "rag-bot,support,auto-created")

## Step 3: Verify Jira Permissions

Ensure your Jira account has:
- **Create Issues** permission in the target project
- **Add Comments** permission (if you plan to add webhook responses later)
- **Browse Projects** permission

## Step 4: Test the Integration

### Backend Test

1. Check if Jira is configured:
   ```bash
   curl https://fcs-rag-bot-production.onrender.com/api/jira/status
   ```

   Should return:
   ```json
   {
     "configured": true,
     "server_url": "https://yourcompany.atlassian.net",
     "project_key": "SUPPORT",
     "issue_type": "Task"
   }
   ```

### Frontend Test

1. Go to your frontend: https://www.fcs-alex.com
2. Ask a question in the chat
3. After receiving a response, click **"Create Jira Ticket"** button
4. The button should change to **"View Jira Ticket"** with a link

## How It Works

### User Flow

1. User asks a question in the chat
2. Bot responds with an answer
3. User clicks **"Create Jira Ticket"** button (if Jira is configured)
4. Ticket is created in Jira with:
   - **Title**: User's question (truncated to 255 chars)
   - **Description**: 
     - User's question
     - Bot's response
     - Knowledge base sources used
     - Auto-generated footer
   - **Labels**: As configured (e.g., "rag-bot", "support")
   - **Issue Type**: As configured (e.g., "Task")
5. User sees a link to the created ticket

### Ticket Format

The ticket description includes:

```
h2. User Question
[The user's original question]

h2. Bot Response
[The bot's answer]

h2. Knowledge Base Sources
* Source 1
* Source 2
...

---
_This ticket was automatically created by the FCS RAG Bot._
```

## API Endpoints

### Create Ticket

**POST** `/api/jira/create-ticket`

Request:
```json
{
  "question": "How do I configure Line Item Details?",
  "bot_response": "To configure Line Item Details...",
  "sources": [
    {"name": "Vena Copilot/Line Item Details Guide.md"}
  ],
  "user_context": "Optional additional context"
}
```

Response:
```json
{
  "success": true,
  "ticket_key": "SUPPORT-123",
  "ticket_url": "https://yourcompany.atlassian.net/browse/SUPPORT-123"
}
```

### Check Status

**GET** `/api/jira/status`

Response:
```json
{
  "configured": true,
  "server_url": "https://yourcompany.atlassian.net",
  "project_key": "SUPPORT",
  "issue_type": "Task"
}
```

## Troubleshooting

### "Jira not configured" Error

- Check that all required environment variables are set
- Verify the variables are loaded (check Render logs)
- Ensure no typos in variable names

### "Failed to create Jira ticket" Error

- Verify your Jira API token is correct
- Check that your email matches your Jira account
- Ensure you have permission to create issues in the project
- Check the project key is correct (case-sensitive)

### Button Not Showing

- Check that Jira is configured (use `/api/jira/status` endpoint)
- Verify frontend can reach the backend API
- Check browser console for errors

## Next Steps

Once basic ticket creation is working, you can:

1. **Add Webhooks**: Configure Jira to send webhooks to your bot when tickets are created/updated
2. **Auto-Response**: Have the bot automatically analyze tickets and post suggested answers
3. **Ticket Linking**: Link related tickets together based on similar questions

## Security Notes

- **API Token**: Keep your Jira API token secure - never commit it to git
- **Permissions**: Use a service account with minimal required permissions
- **Rate Limiting**: Consider adding rate limiting to prevent abuse
- **Validation**: The bot validates webhook signatures (when webhooks are added)

## Support

If you encounter issues:
1. Check the backend logs in Render
2. Verify Jira API token is valid
3. Test Jira API access directly using the Jira Python library
4. Check Jira project permissions
