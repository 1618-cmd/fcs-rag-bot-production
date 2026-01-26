# Fix "Failed to fetch" Login Issue

## Problem
Frontend shows "Failed to fetch" when trying to log in.

## Root Cause
The backend server is not running on port 8000.

## Solution

### Step 1: Start Backend in a Visible Terminal

**Open a NEW terminal window** and run:

```bash
cd "C:\Users\Miles\Desktop\Projects\Vena\FCS RAG Bot Production\backend"
python -m uvicorn src.api.main:app --reload
```

**You should see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 2: If You See Errors

**Common errors and fixes:**

1. **"Module not found"**
   ```bash
   pip install -r requirements.txt
   ```

2. **"Configuration validation failed"**
   - Make sure `backend/.env` exists
   - Should have `ALLOW_FALLBACK_ADMIN_LOGIN=true`

3. **"Address already in use"**
   - Port 8000 is taken
   - Kill the process: `netstat -ano | findstr :8000` then `taskkill /PID <pid> /F`

4. **"Import errors"**
   - Check Python path
   - Make sure you're in the `backend` directory

### Step 3: Verify Backend is Running

In another terminal, test:
```bash
curl http://localhost:8000/api/health
```

Should return: `{"status":"healthy","environment":"development","version":"1.0.0"}`

### Step 4: Try Login Again

1. Go to `http://localhost:3000/login`
2. Email: `admin@example.com`
3. Password: `admin`

## Quick Start Script

I've created `backend/start_backend.bat` - you can double-click it to start the backend.

## Why This Happens

When the backend starts in the background, if there are errors, you can't see them. Starting it in a visible terminal lets you see what's wrong.
