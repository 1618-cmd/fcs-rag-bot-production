# Testing Admin Roles Locally

## Quick Setup Guide

### Step 1: Set DATABASE_URL

You have two options:

#### Option A: Use Render Database (Easiest)
1. Go to your Render dashboard
2. Click on your PostgreSQL database service
3. Go to "Connections" tab
4. Copy the "Internal Database URL"
5. Add to your `backend/.env` file:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/database
   ```

#### Option B: Local PostgreSQL
1. Install PostgreSQL locally
2. Create a database:
   ```sql
   CREATE DATABASE vena_rag_bot;
   ```
3. Update `backend/.env`:
   ```
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/vena_rag_bot
   ```

### Step 2: Run Migration

```bash
cd backend
alembic upgrade head
```

This creates the `users`, `tenants`, and `query_logs` tables.

### Step 3: Create First Admin User

```bash
cd backend
python -m scripts.create_admin_user --email admin@example.com --password yourpassword
```

Or interactively:
```bash
python -m scripts.create_admin_user
```

### Step 4: Start Backend

```bash
cd backend
uvicorn src.api.main:app --reload --port 8000
```

### Step 5: Test Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "yourpassword"}'
```

You should get a JWT token back!

### Step 6: Create More Users (via API)

```bash
# Get your token from Step 5, then:
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "role": "viewer",
    "full_name": "Test User"
  }'
```

## Available Roles

- **admin**: Full access (all permissions)
- **modeler**: Can upload, approve documents, view analytics
- **contributor**: Can query and upload documents
- **viewer**: Read-only (can query bot)

## Troubleshooting

### "DATABASE_URL not configured"
- Make sure `DATABASE_URL` is in your `backend/.env` file
- Restart your backend server after adding it

### "could not translate host name"
- Check your `DATABASE_URL` format
- Make sure the database is accessible from your machine

### "User already exists"
- The user was already created
- You can update their role or use a different email
