# How to Start Backend for Login

## Quick Start

**Open a NEW terminal window** and run:

```bash
cd "C:\Users\Miles\Desktop\Projects\Vena\FCS RAG Bot Production\backend"
uvicorn src.api.main:app --reload
```

## What You Should See

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Verify It's Working

Open another terminal and test:
```bash
curl http://localhost:8000/api/health
```

Should return: `{"status":"healthy","environment":"development","version":"1.0.0"}`

## Then Try Login

1. Go to http://localhost:3000/login
2. Email: `admin@example.com`
3. Password: `admin`

## Common Issues

**"Address already in use"**
- Port 8000 is taken
- Kill the process: `netstat -ano | findstr :8000` then `taskkill /PID <pid> /F`

**"Module not found"**
- Install dependencies: `pip install -r requirements.txt`

**"Configuration validation failed"**
- Check `backend/.env` file exists
- Make sure `ALLOW_FALLBACK_ADMIN_LOGIN=true` is set
