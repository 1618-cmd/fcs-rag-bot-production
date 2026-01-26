# Vena API Endpoints Summary

## Available Endpoints (Vena Public API)

Based on the official Vena API documentation, only these endpoints are available:

### 1. Export Intersections (GET)
**Endpoint:** `GET /models/{modelID}/intersections`

**Description:** Export intersection data from a Vena model. This is the PRIMARY endpoint for reading data.

**Parameters:**
- `filters` (optional): JSON-encoded array of filter objects
  - Example: `[{"field": "Year", "eq": "2023"}]`
- `fields` (optional): Comma-separated list of field names to return
  - Example: `Account,Entity,Period,Value`
- `limit` (optional): Number of records to return (pagination)
- `offset` (optional): Number of records to skip (pagination)

**Example:**
```bash
curl -u {apiUser}:{apiKey} \
  "https://eu1.vena.io/api/public/v1/models/{modelID}/intersections?limit=10" \
  -H "Accept: application/json"
```

### 2. Import Data (POST)
**Endpoint:** `POST /jobs/start-with-data`

**Description:** Import data into a Vena model via ETL template.

**Note:** This is for writing data, not reading. Not used in our RAG integration.

## Endpoints That Do NOT Exist

The following endpoints are **NOT available** in the Vena Public API:

- ❌ `GET /dimensions` - Does not exist
- ❌ `GET /models/{modelID}/dimensions` - Does not exist
- ❌ `GET /models/{modelID}/dimensions/{dimensionName}/members` - Does not exist
- ❌ `GET /templates` - Does not exist
- ❌ `GET /jobs` - Does not exist
- ❌ `GET /models/{modelID}` - Does not exist
- ❌ `GET /models` - Does not exist

## Solution: Extract Data from Intersections

Since most endpoints don't exist, our implementation:

1. **Extracts dimensions** from intersection keys
   - Gets a sample intersection
   - Reads the keys (excluding Value, id, etc.)
   - Returns dimension names

2. **Extracts dimension members** from intersection values
   - Gets intersections filtered to a specific dimension field
   - Extracts unique values for that dimension
   - Returns member names

3. **Infers model structure** from intersection data
   - Analyzes intersection structure
   - Builds model metadata from available data

## Requirements

**Model ID is Required**

Most Vena API operations require a Model ID. Users can find it:

1. Log into Vena
2. Go to Modeler -> Data Model
3. Check the URL - it contains the Model ID
4. Example: `https://eu1.vena.io/modeler/data-model/12345`
   - Model ID: `12345`

## Testing

To test the integration:

```bash
# Test without Model ID (shows limitations)
python backend/test_vena_api_correct.py

# Test with Model ID (full functionality)
python backend/test_vena_api_correct.py YOUR_MODEL_ID
```

## Integration Status

✅ **Working:**
- Intersections endpoint (primary data source)
- Dimension extraction from intersections
- Dimension member extraction from intersections
- Model structure inference
- Smart detection (when to call API)
- LLM-based intent detection
- Caching (Redis)

⚠️ **Limitations:**
- Requires Model ID for most operations
- Dimensions/members extracted from data (not direct API)
- ETL templates/jobs not available via API
- Model listing not available

## References

- Vena API Documentation: https://developers.venasolutions.com/
- API Reference: https://developers.venasolutions.com/reference
- Recipes: https://developers.venasolutions.com/recipes
