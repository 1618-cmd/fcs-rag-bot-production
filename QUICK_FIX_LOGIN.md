# Quick Fix: Can't Login

## Problem
Frontend loads but login doesn't work.

## Solution

### Step 1: Start the Backend Server

Open a **new terminal** and run:

```bash
cd backend
uvicorn src.api.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 2: Enable Fallback Admin Login

The login needs either:
- A database user (if database is set up), OR
- Fallback admin credentials (for testing)

**Option A: Enable Fallback Login (Easiest)**

Add to `backend/.env`:
```bash
ALLOW_FALLBACK_ADMIN_LOGIN=true
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin
JWT_SECRET_KEY=your-secret-key-change-in-production
```

**Option B: Create Admin User in Database**

If you have a database set up:
```bash
cd backend
python scripts/create_admin_user.py
```

### Step 3: Try Logging In

Use these credentials:
- **Email:** `admin@example.com`
- **Password:** `admin`

### Step 4: Check Browser Console

Open browser DevTools (F12) → Console tab
Look for errors like:
- `Failed to fetch` → Backend not running
- `401 Unauthorized` → Wrong credentials
- `CORS error` → Backend CORS not configured

### Common Issues

**"Failed to fetch" or "Network error"**
- Backend not running → Start with Step 1
- Wrong API URL → Check `NEXT_PUBLIC_API_URL` in frontend `.env`

**"Invalid email or password"**
- Fallback login not enabled → Add `ALLOW_FALLBACK_ADMIN_LOGIN=true` to backend `.env`
- Wrong credentials → Use `admin@example.com` / `admin`

**"CORS error"**
- Backend CORS not allowing frontend → Check `FRONTEND_URL` in backend `.env`
