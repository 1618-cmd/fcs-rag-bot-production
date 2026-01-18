# Trigger Production Ingestion

## Method 1: Using PowerShell (Windows)

```powershell
# Replace YOUR_API_KEY with your actual INGESTION_API_KEY from Render
$apiKey = "YOUR_API_KEY"
Invoke-WebRequest -Uri "https://fcs-rag-bot-production.onrender.com/api/ingest" -Method POST -Headers @{"X-API-Key"=$apiKey}
```

## Method 2: Using curl (if available)

```bash
curl -X POST https://fcs-rag-bot-production.onrender.com/api/ingest \
  -H "X-API-Key: YOUR_API_KEY"
```

## Method 3: If API Key is NOT set in Render

If `INGESTION_API_KEY` is not configured in Render environment variables, you can call without the header:

```powershell
Invoke-WebRequest -Uri "https://fcs-rag-bot-production.onrender.com/api/ingest" -Method POST
```

## Get Your API Key

1. Go to Render Dashboard: https://dashboard.render.com
2. Select your service: `fcs-rag-bot-production`
3. Go to "Environment" tab
4. Look for `INGESTION_API_KEY` variable
5. Copy the value

## Expected Response

```json
{
  "status": "success",
  "message": "Ingestion completed successfully",
  "collection": "fcs-rag-bot-prod",
  "points_count": 12345
}
```

## After Ingestion

1. Wait 1-2 minutes for ingestion to complete
2. Test your VenaQL question again in production
3. The bot should now reference the troubleshooting document
