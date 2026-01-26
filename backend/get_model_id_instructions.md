# How to Get Your Vena Model ID

## Quick Method (Recommended)

1. **Open your browser** and go to: https://eu1.vena.io
2. **Log in** with your Vena credentials
3. **Click the "Modeler" tab** (top navigation)
4. **Click "Data Model"** in the left sidebar
5. **Look at the URL** in your browser address bar
6. **The Model ID is the number at the end**

### Example:
- **URL:** `https://eu1.vena.io/modeler/data-model/12345`
- **Model ID:** `12345`

## Test Your Model ID

Once you have a Model ID, test it with:

```bash
cd backend
python find_model_id.py <YOUR_MODEL_ID>
```

Example:
```bash
python find_model_id.py 12345
```

If the Model ID is valid, the script will:
- Confirm it's valid
- Show you the dimensions in your model
- Provide instructions on how to use it

## Alternative: Check Browser Developer Tools

If you can't see the Model ID in the URL:

1. Open your browser's Developer Tools (F12)
2. Go to the Network tab
3. Navigate to Modeler -> Data Model
4. Look for API calls - the Model ID might be in the request URLs or response data

## Using Model ID in RAG Bot

Once you have your Model ID, you can:

1. **Add it to your query** in the chat interface (if we add a Model ID input field)
2. **Or set it in your .env file** as `VENA_MODEL_ID=12345` (if we add this feature)
3. **Or pass it in the API request** as `vena_model_id` parameter

## Note

- Each data model in your tenant has its own Model ID
- If you have multiple models, use the Model ID for the specific model you want to query
- The Model ID is required for most Vena API operations
