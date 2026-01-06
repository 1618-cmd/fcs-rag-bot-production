# Starting the FastAPI Server

## Quick Start

```bash
cd backend
uvicorn src.api.main:app --reload
```

The server will start at: **http://localhost:8000**

## API Endpoints

- **Root**: http://localhost:8000/
- **API Docs**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/api/health
- **Query Endpoint**: http://localhost:8000/api/query (POST)

## Test the API

### Using curl:
```bash
# Health check
curl http://localhost:8000/api/health

# Query
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Vena?"}'
```

### Using Python:
```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/health")
print(response.json())

# Query
response = requests.post(
    "http://localhost:8000/api/query",
    json={"question": "What is Vena?"}
)
print(response.json())
```

## Production Mode

For production (no auto-reload):
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

