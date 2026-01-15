# AWS Lambda Setup for Event-Based Ingestion

This guide explains how to set up AWS Lambda to automatically trigger ingestion when files are uploaded to S3.

## Overview

When a new document is uploaded to your S3 bucket, Lambda will automatically call your Render API to trigger ingestion, keeping your vector database up-to-date.

## Prerequisites

- AWS account with Lambda access
- S3 bucket created (`fcs-rag-bot-kb-prod`)
- Render API endpoint deployed with `/api/ingest` endpoint
- API key for securing the ingestion endpoint (optional but recommended)

## Step 1: Set Up Ingestion API Key in Render

1. Generate a secure API key (e.g., use a password generator or `openssl rand -hex 32`)
2. Go to Render → Environment Variables
3. Add: `INGESTION_API_KEY=your-generated-api-key-here`
4. Save and redeploy

## Step 2: Create Lambda Function

1. **Go to AWS Lambda Console**: https://console.aws.amazon.com/lambda/
2. **Click "Create function"**
3. **Configure**:
   - **Function name**: `fcs-rag-bot-s3-ingestion-trigger`
   - **Runtime**: Python 3.12
   - **Architecture**: x86_64
   - **Execution role**: Create a new role with basic Lambda permissions
4. **Click "Create function"**

## Step 3: Add Lambda Code

1. **In the Lambda function**, scroll to "Code source"
2. **Delete the default code**
3. **Copy the code from** `scripts/lambda_s3_ingestion_trigger.py`
4. **Paste it into the Lambda editor**
5. **Click "Deploy"**

## Step 4: Configure Lambda Environment Variables

1. **In Lambda function**, go to "Configuration" → "Environment variables"
2. **Add variables**:
   - `RENDER_API_URL`: `https://fcs-rag-bot-production.onrender.com/api/ingest`
   - `INGESTION_API_KEY`: (the same key you set in Render)

## Step 5: Configure Lambda Timeout

1. **Go to "Configuration" → "General configuration"**
2. **Click "Edit"**
3. **Set timeout**: `5 minutes` (300 seconds) - ingestion can take a while
4. **Set memory**: `512 MB` (or more if needed)
5. **Click "Save"**

## Step 6: Set Up S3 Event Notification

1. **Go to S3 Console**: https://console.aws.amazon.com/s3/
2. **Click on your bucket**: `fcs-rag-bot-kb-prod`
3. **Go to "Properties" tab**
4. **Scroll to "Event notifications"**
5. **Click "Create event notification"**
6. **Configure**:
   - **Event name**: `trigger-ingestion-on-upload`
   - **Prefix**: `knowledge_base/` (only trigger for files in this folder)
   - **Suffix**: `.md` (optional: only trigger for markdown files, or leave blank for all)
   - **Event types**: Select "All object create events" (or just "PUT")
   - **Destination**: "Lambda function"
   - **Lambda function**: Select `fcs-rag-bot-s3-ingestion-trigger`
7. **Click "Save changes"**

## Step 7: Grant S3 Permission to Invoke Lambda

1. **Go back to Lambda function**
2. **Go to "Configuration" → "Permissions"**
3. **Click on the execution role** (opens IAM)
4. **Add permission** → "Create inline policy"
5. **Use JSON**:
   ```json
   {
     "Version": "2012-10-17",
   "Statement": [
     {
       "Effect": "Allow",
       "Action": [
         "s3:GetObject"
       ],
       "Resource": "arn:aws:s3:::fcs-rag-bot-kb-prod/*"
     }
   ]
   }
   ```
6. **Save policy**

## Step 8: Test the Setup

1. **Upload a test file** to `s3://fcs-rag-bot-kb-prod/knowledge_base/test.md`
2. **Check Lambda logs**:
   - Go to Lambda → "Monitor" → "View CloudWatch logs"
   - You should see: "Triggering ingestion at..."
3. **Check Render logs**:
   - Go to Render → Logs
   - You should see: "Triggering knowledge base ingestion..."
4. **Test a query** in your RAG bot to verify the new document is searchable

## Troubleshooting

### Lambda timeout
- Increase timeout to 5-10 minutes
- Check if ingestion is taking too long

### 401 Unauthorized
- Verify `INGESTION_API_KEY` matches in both Lambda and Render
- Check the API key is set correctly

### Connection errors
- Verify `RENDER_API_URL` is correct
- Check Render service is running
- Verify Lambda has internet access (default VPC)

### No events triggered
- Check S3 event notification is configured correctly
- Verify Lambda function name matches
- Check CloudWatch logs for errors

## Cost Considerations

- **Lambda**: Free tier includes 1M requests/month, 400,000 GB-seconds
- **S3 notifications**: Free
- **CloudWatch logs**: Free tier includes 5GB/month
- **Render API calls**: Included in your Render plan

## Security Best Practices

1. **Use API key authentication** (required)
2. **Store API key in AWS Secrets Manager** (optional, more secure)
3. **Restrict Lambda execution role** to minimum permissions
4. **Monitor CloudWatch logs** for unauthorized access attempts
5. **Use VPC** if you want to restrict Lambda network access (advanced)

## Next Steps

- Set up CloudWatch alarms for failed ingestions
- Add retry logic for transient failures
- Implement batch processing for multiple file uploads
- Set up monitoring and alerting
