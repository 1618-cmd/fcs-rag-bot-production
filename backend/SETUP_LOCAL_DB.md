# Setting Up Local Database for Testing

## Option 1: Docker (Easiest)

### Prerequisites
- Docker Desktop installed

### Steps

1. **Start PostgreSQL container:**
   ```bash
   cd backend
   docker-compose -f docker-compose.local.yml up -d
   ```

2. **Update your `.env` file:**
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fcs_rag_bot_local
   ```

3. **Run migration/setup:**
   ```bash
   python scripts/setup_database.py
   ```

4. **Create admin user:**
   ```bash
   python scripts/create_admin_user.py --email admin@example.com --password yourpassword
   ```

5. **Test it:**
   ```bash
   # Start backend
   uvicorn src.api.main:app --reload --port 8000
   
   # Test login
   curl -X POST http://localhost:8000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "yourpassword"}'
   ```

### Stop Database
```bash
docker-compose -f docker-compose.local.yml down
```

### Reset Database (wipe all data)
```bash
docker-compose -f docker-compose.local.yml down -v
docker-compose -f docker-compose.local.yml up -d
```

---

## Option 2: Direct PostgreSQL Install

### Prerequisites
- PostgreSQL 15+ installed locally

### Steps

1. **Create database:**
   ```sql
   CREATE DATABASE fcs_rag_bot_local;
   ```

2. **Update your `.env` file:**
   ```
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/fcs_rag_bot_local
   ```
   (Replace `yourpassword` with your PostgreSQL password)

3. **Run setup:**
   ```bash
   python scripts/setup_database.py
   python scripts/create_admin_user.py --email admin@example.com --password yourpassword
   ```

---

## Option 3: Use Render External URL (Not Recommended)

Only if you want to test against production database (risky):

1. Get External Database URL from Render dashboard
2. Update `.env` with external URL
3. Run setup scripts

**Warning:** This uses your production database. Be careful!

---

## Recommended: Docker

Docker is the easiest and safest option. It gives you:
- ✅ Clean, isolated database
- ✅ Easy reset (just delete container)
- ✅ No installation needed (just Docker)
- ✅ Same PostgreSQL version as production
