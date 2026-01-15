# Keep-Alive Setup for Render

## Problem
Render services can spin down after 15+ minutes of inactivity, causing cold starts (10-25 seconds) for the first user.

## Solution
Use an external service to ping your health endpoint every 5-10 minutes to keep the service warm.

## Recommended Services

### Option 1: UptimeRobot (Free)
1. Go to https://uptimerobot.com/
2. Create a free account
3. Add a new monitor:
   - **Monitor Type**: HTTP(s)
   - **URL**: `https://fcs-rag-bot-production.onrender.com/api/health/warmup`
   - **Monitoring Interval**: 5 minutes
   - **Alert Contacts**: (optional)

### Option 2: cron-job.org (Free)
1. Go to https://cron-job.org/
2. Create a free account
3. Create a new cron job:
   - **URL**: `https://fcs-rag-bot-production.onrender.com/api/health/warmup`
   - **Schedule**: Every 5 minutes (`*/5 * * * *`)
   - **Request Method**: GET

### Option 3: GitHub Actions (Free)
Create `.github/workflows/keep-alive.yml`:
```yaml
name: Keep-Alive
on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 minutes
  workflow_dispatch:

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping health endpoint
        run: |
          curl -f https://fcs-rag-bot-production.onrender.com/api/health/warmup || exit 1
```

## Endpoints Available

- `/api/health` - Basic health check (fast)
- `/api/health/warmup` - Warm-up endpoint (initializes RAG pipeline if needed)
- `/api/health/ready` - Readiness check (verifies dependencies)

## Cost
- **UptimeRobot**: Free (50 monitors)
- **cron-job.org**: Free (unlimited jobs)
- **GitHub Actions**: Free (2000 minutes/month)

## Expected Result
- ✅ No cold starts for users
- ✅ First query responds in ~5 seconds instead of 10-25 seconds
- ✅ Better user experience

## Testing
After setting up keep-alive:
1. Wait 20 minutes
2. Visit https://www.fcs-alex.com/
3. Ask a question - should be fast!
