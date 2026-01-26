# Vena API Recipes

## Overview

This document contains practical code examples and recipes for using the Vena API. These recipes demonstrate common use cases, best practices, and working code snippets for integrating with Vena's Import and Export APIs.

**Source:** https://developers.venasolutions.com/recipes

## Export API Recipes

### Basic Export Request

Export intersection data from a Vena model using the Export API.

**Endpoint:**
```
GET https://{hub}.vena.io/api/public/v1/models/{modelID}/intersections
```

**Authentication:**
- HTTP Basic Auth
- Username: apiUser
- Password: apiKey

**Example Request:**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections" \
  -H "Accept: application/json"
```

### Filtered Export

Export data with filters to retrieve specific intersections.

**Example: Filter by Year**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections?filters=[{\"field\":\"Year\",\"eq\":\"2023\"}]" \
  -H "Accept: application/json"
```

**Example: Multiple Filters**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections?filters=[{\"field\":\"Year\",\"eq\":\"2023\"},{\"field\":\"Entity\",\"eq\":\"Entity1\"}]" \
  -H "Accept: application/json"
```

**Important Notes:**
- Filters parameter must be lowercase: `filters` (not `FILTERS`)
- Filters must be JSON-encoded
- Field names are case-sensitive

### Export Specific Fields

Limit the response to specific fields only.

**Example:**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections?fields=Account,Entity,Period,Value" \
  -H "Accept: application/json"
```

### Export with Pagination

Handle large datasets using pagination parameters.

**Example:**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections?limit=100&offset=0" \
  -H "Accept: application/json"
```

## Python Examples

### Basic Export with Python

```python
import requests
import json

# Vena API credentials
api_user = "your-api-user"
api_key = "your-api-key"
hub = "eu1"  # or us1, us2, etc.
model_id = "your-model-id"

# Base URL
base_url = f"https://{hub}.vena.io/api/public/v1"

# Export intersections
url = f"{base_url}/models/{model_id}/intersections"
response = requests.get(
    url,
    auth=(api_user, api_key),
    headers={"Accept": "application/json"}
)

if response.status_code == 200:
    data = response.json()
    print(f"Retrieved {len(data)} intersections")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### Export with Filters (Python)

```python
import requests
import json

api_user = "your-api-user"
api_key = "your-api-key"
hub = "eu1"
model_id = "your-model-id"
base_url = f"https://{hub}.vena.io/api/public/v1"

# Define filters
filters = [
    {"field": "Year", "eq": "2023"},
    {"field": "Entity", "eq": "Entity1"}
]

# Build URL with filters
url = f"{base_url}/models/{model_id}/intersections"
params = {
    "filters": json.dumps(filters)
}

response = requests.get(
    url,
    auth=(api_user, api_key),
    params=params,
    headers={"Accept": "application/json"}
)

if response.status_code == 200:
    data = response.json()
    print(f"Retrieved {len(data)} filtered intersections")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### Export All Data with Pagination (Python)

```python
import requests
import json

api_user = "your-api-user"
api_key = "your-api-key"
hub = "eu1"
model_id = "your-model-id"
base_url = f"https://{hub}.vena.io/api/public/v1"

all_data = []
limit = 100
offset = 0

while True:
    url = f"{base_url}/models/{model_id}/intersections"
    params = {
        "limit": limit,
        "offset": offset
    }
    
    response = requests.get(
        url,
        auth=(api_user, api_key),
        params=params,
        headers={"Accept": "application/json"}
    )
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break
    
    data = response.json()
    
    if not data or len(data) == 0:
        break
    
    all_data.extend(data)
    offset += limit
    
    # If we got fewer than limit, we've reached the end
    if len(data) < limit:
        break

print(f"Retrieved {len(all_data)} total intersections")
```

## Import API Recipes

### Basic Import Request

Import data into a Vena model using the Import API.

**Endpoint:**
```
POST https://{hub}.vena.io/api/public/v1/jobs/start-with-data
```

**Example Request:**
```bash
curl -u {apiUser}:{apiKey} \
  -X POST \
  "https://eu1.vena.io/api/public/v1/jobs/start-with-data" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "templateId": "your-template-id",
    "data": [
      {
        "Account": "4000",
        "Entity": "Entity1",
        "Period": "2023-01",
        "Value": 1000
      }
    ]
  }'
```

### Import with Python

```python
import requests
import json

api_user = "your-api-user"
api_key = "your-api-key"
hub = "eu1"
base_url = f"https://{hub}.vena.io/api/public/v1"

# Import data
url = f"{base_url}/jobs/start-with-data"

payload = {
    "templateId": "your-template-id",
    "data": [
        {
            "Account": "4000",
            "Entity": "Entity1",
            "Period": "2023-01",
            "Value": 1000
        },
        {
            "Account": "4100",
            "Entity": "Entity1",
            "Period": "2023-01",
            "Value": 2000
        }
    ]
}

response = requests.post(
    url,
    auth=(api_user, api_key),
    json=payload,
    headers={"Accept": "application/json"}
)

if response.status_code == 200:
    result = response.json()
    print(f"Import job started: {result.get('jobId')}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

## Common Use Cases

### FX Conversion Script Generation

Use exported data to generate FX conversion scripts.

**Workflow:**
1. Export Account hierarchy from Vena
2. Identify accounts that need FX conversion
3. Generate VenaQL script using actual account codes

**Example:**
```python
# 1. Export Account dimension
accounts = export_dimension_members("Account", model_id)

# 2. Filter revenue accounts
revenue_accounts = [acc for acc in accounts if acc.get("type") == "Revenue"]

# 3. Generate FX script
script = generate_fx_script(revenue_accounts, target_currency="USD")
```

### Data Validation

Export and validate data before import.

```python
# Export existing data
existing_data = export_intersections(model_id, filters=[{"field": "Year", "eq": "2023"}])

# Validate new data against existing
def validate_data(new_data, existing_data):
    errors = []
    for record in new_data:
        # Check for duplicates
        if record in existing_data:
            errors.append(f"Duplicate record: {record}")
        # Validate required fields
        if not record.get("Account") or not record.get("Value"):
            errors.append(f"Missing required fields: {record}")
    return errors
```

### Bulk Data Export

Export large datasets efficiently.

```python
def export_all_data(model_id, filters=None):
    """Export all data with automatic pagination."""
    all_data = []
    limit = 1000
    offset = 0
    
    while True:
        params = {"limit": limit, "offset": offset}
        if filters:
            params["filters"] = json.dumps(filters)
        
        response = requests.get(
            f"{base_url}/models/{model_id}/intersections",
            auth=(api_user, api_key),
            params=params,
            headers={"Accept": "application/json"}
        )
        
        if response.status_code != 200:
            break
        
        data = response.json()
        if not data:
            break
        
        all_data.extend(data)
        offset += limit
        
        if len(data) < limit:
            break
    
    return all_data
```

## Error Handling

### Handle Common Errors

```python
def safe_api_call(url, method="GET", **kwargs):
    """Make API call with error handling."""
    try:
        if method == "GET":
            response = requests.get(url, **kwargs)
        elif method == "POST":
            response = requests.post(url, **kwargs)
        
        if response.status_code == 200:
            return {"success": True, "data": response.json()}
        elif response.status_code == 401:
            return {"success": False, "error": "Authentication failed. Check apiUser and apiKey."}
        elif response.status_code == 403:
            return {"success": False, "error": "Permission denied. Check API token permissions."}
        elif response.status_code == 404:
            return {"success": False, "error": "Endpoint not found. Check model ID and endpoint URL."}
        else:
            return {"success": False, "error": f"API error {response.status_code}: {response.text}"}
    
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Request failed: {str(e)}"}
```

## Best Practices

### 1. Always Use Filters When Possible

Filtering reduces response size and improves performance.

```python
# Good: Filtered request
filters = [{"field": "Year", "eq": "2023"}]
data = export_intersections(model_id, filters=filters)

# Avoid: Fetching all data then filtering
all_data = export_intersections(model_id)
filtered = [d for d in all_data if d["Year"] == "2023"]
```

### 2. Implement Caching

Cache frequently accessed data to reduce API calls.

```python
from functools import lru_cache
import time

cache = {}
cache_ttl = 3600  # 1 hour

def get_cached_dimensions(model_id):
    cache_key = f"dimensions_{model_id}"
    if cache_key in cache:
        cached_time, data = cache[cache_key]
        if time.time() - cached_time < cache_ttl:
            return data
    
    # Fetch from API
    data = export_dimensions(model_id)
    cache[cache_key] = (time.time(), data)
    return data
```

### 3. Handle Rate Limits

Implement retry logic for rate-limited requests.

```python
import time

def api_call_with_retry(url, max_retries=3, **kwargs):
    for attempt in range(max_retries):
        response = requests.get(url, **kwargs)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:  # Too Many Requests
            wait_time = 2 ** attempt  # Exponential backoff
            time.sleep(wait_time)
            continue
        else:
            raise Exception(f"API error: {response.status_code}")
    
    raise Exception("Max retries exceeded")
```

### 4. Validate Data Before Import

Always validate data structure before importing.

```python
def validate_import_data(data, required_fields):
    """Validate data structure before import."""
    errors = []
    for i, record in enumerate(data):
        for field in required_fields:
            if field not in record:
                errors.append(f"Record {i}: Missing required field '{field}'")
        if not isinstance(record.get("Value"), (int, float)):
            errors.append(f"Record {i}: Value must be numeric")
    return errors
```

## Integration with RAG Bot

### Using API Data in Script Generation

When generating VenaQL scripts, use live API data for accuracy:

```python
# 1. Fetch Account hierarchy from Vena
accounts = get_dimension_members("Account", model_id)

# 2. Identify relevant accounts
revenue_accounts = [acc["code"] for acc in accounts if acc.get("type") == "Revenue"]

# 3. Generate script with actual account codes
script = f"""
Scope {{
  {', '.join([f'[Account.{code}]' for code in revenue_accounts])},
  [Entity.Homelink],
  [Measure.Value]
}}
@this = [Measure.Value].Sum()
"""
```

## References

- Vena API Documentation: https://developers.venasolutions.com/
- API Reference: https://developers.venasolutions.com/reference
- Recipes: https://developers.venasolutions.com/recipes
- Troubleshooting Guide: https://developers.venasolutions.com/docs/vena-api-troubleshooting-guide
