# Running Migration on Render

## Step 1: Open Render Shell

1. In your Render dashboard, go to your **web service** (fcs-rag-bot-production)
2. Click **"Shell"** in the left sidebar (under MANAGE section)
3. This opens a terminal connected to your Render service

## Step 2: Run Migration

In the Render Shell, run:

```bash
cd backend
alembic upgrade head
```

This will create all the database tables.

## Step 3: Create Admin User

Still in Render Shell:

```bash
python -m scripts.create_admin_user --email admin@example.com --password yourpassword
```

Or interactively:
```bash
python -m scripts.create_admin_user
```

## Done!

Your database is now set up and you have an admin user. You can test the API endpoints from your localhost frontend or directly via the Render API.
