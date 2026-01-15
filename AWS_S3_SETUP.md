# AWS S3 Setup Guide for Knowledge Base

## Overview

This guide explains how to set up AWS S3 to host your knowledge base documents instead of using the local filesystem or GitHub.

## Prerequisites

- AWS account (you have one with $100 credits and 182 days remaining)
- AWS S3 bucket created
- AWS credentials (Access Key ID and Secret Access Key)

## Step 1: Create S3 Bucket

1. **Log into AWS Console**: https://console.aws.amazon.com/
2. **Navigate to S3**: Search for "S3" in the services menu
3. **Create Bucket**:
   - Click "Create bucket"
   - **Bucket name**: Choose a unique name (e.g., `fcs-rag-bot-kb-dev` for development, `fcs-rag-bot-kb-prod` for production)
   - **Region**: Choose your preferred region (e.g., `eu-north-1` for Stockholm, or `us-east-1`)
   - **Block Public Access**: Keep default settings (block all public access)
   - Click "Create bucket"

## Step 2: Upload Documents to S3

### Option A: AWS Console (Manual Upload)

1. **Open your bucket** in S3 console
2. **Click "Upload"**
3. **Drag and drop** your knowledge base files or folders
4. **Click "Upload"**

### Option B: AWS CLI (Recommended for bulk upload)

```bash
# Install AWS CLI if not already installed
# Windows: Download from https://aws.amazon.com/cli/
# Mac: brew install awscli

# Configure AWS credentials
aws configure

# Upload entire knowledge_base folder
aws s3 sync knowledge_base/ s3://your-bucket-name/knowledge_base/ --region eu-north-1
```

## Step 3: Create AWS IAM User (for API Access)

1. **Navigate to IAM**: Search for "IAM" in AWS console
2. **Create User**:
   - Click "Users" → "Create user"
   - **User name**: `fcs-rag-bot-s3-access`
   - Click "Next"
3. **Attach Policy**:
   - Select "Attach policies directly"
   - Search for and select: **AmazonS3ReadOnlyAccess** (or create custom policy with read-only access to your specific bucket)
   - Click "Next" → "Create user"
4. **Create Access Keys**:
   - Click on the user you just created
   - Go to "Security credentials" tab
   - Click "Create access key"
   - Select "Application running outside AWS"
   - Click "Next" → "Create access key"
   - **IMPORTANT**: Copy both the Access Key ID and Secret Access Key (you won't see the secret again!)

## Step 4: Configure Environment Variables

Add these to your `.env` file (or Render environment variables for production):

```bash
# Enable S3
USE_S3=true

# AWS Credentials
AWS_ACCESS_KEY_ID=your-access-key-id-here
AWS_SECRET_ACCESS_KEY=your-secret-access-key-here
AWS_REGION=eu-north-1  # or your bucket's region

# S3 Bucket Configuration
S3_BUCKET_NAME=your-bucket-name
S3_PREFIX=knowledge_base/  # Optional: if documents are in a folder
```

## Step 5: Install Dependencies

The `boto3` package is already added to `requirements.txt`. Install it:

```bash
cd backend
pip install -r requirements.txt
```

## Step 6: Test S3 Connection

Run the ingestion script to test:

```bash
# From project root
python -m backend.src.core.ingestion
```

You should see:
```
Loading documents from S3: s3://your-bucket-name/knowledge_base/
Found X documents in S3
```

## Troubleshooting

### Error: "boto3 is not installed"
**Solution**: Install boto3: `pip install boto3`

### Error: "Access Denied" or "403 Forbidden"
**Solution**: 
- Check that your AWS credentials are correct
- Verify the IAM user has S3 read permissions
- Ensure the bucket name is correct

### Error: "Bucket does not exist"
**Solution**:
- Verify the bucket name in `S3_BUCKET_NAME`
- Check that the bucket is in the correct region (match `AWS_REGION`)

### Error: "No documents found"
**Solution**:
- Verify documents are uploaded to S3
- Check the `S3_PREFIX` matches your folder structure
- Ensure file extensions are `.md`, `.txt`, or `.pdf`

## Switching Between Local and S3

### Use Local Filesystem (Default)
```bash
USE_S3=false
# Or simply don't set USE_S3 (defaults to false)
```

### Use S3
```bash
USE_S3=true
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=eu-north-1
S3_BUCKET_NAME=your-bucket-name
```

## Cost Considerations

With your AWS Free Tier:
- **5 GB storage** (free for 12 months)
- **20,000 GET requests/month** (free for 12 months)
- Your knowledge base (~672 documents) should fit comfortably within free tier

After free tier:
- Storage: ~$0.023 per GB/month
- Requests: ~$0.0004 per 1,000 GET requests
- Estimated cost: **< $1/month** for typical knowledge base usage

## Next Steps

1. ✅ Create S3 bucket
2. ✅ Upload documents
3. ✅ Create IAM user and access keys
4. ✅ Configure environment variables
5. ✅ Test ingestion
6. ✅ Deploy to production (update Render environment variables)

## Production Deployment

When ready for production:

1. **Create production bucket**: `fcs-rag-bot-kb-prod`
2. **Upload production documents** to S3
3. **Update Render environment variables**:
   - Go to Render dashboard → Your service → Environment
   - Add all S3-related environment variables
   - Set `USE_S3=true`
4. **Run ingestion** in production (or it will run automatically on next deployment)

## Auto-Ingestion (Future Enhancement)

For automatic ingestion when new documents are uploaded to S3:

1. Set up AWS Lambda function
2. Configure S3 event trigger (on object creation)
3. Lambda calls your ingestion API endpoint
4. Documents are automatically ingested into Qdrant

This can be implemented later if needed.
