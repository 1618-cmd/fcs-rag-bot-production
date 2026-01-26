# How to Find Your Vena Model ID

## Quick Steps

1. **Log into Vena**
   - Go to: https://eu1.vena.io (or your hub URL)

2. **Navigate to Modeler**
   - Click on the **Modeler** tab in the top navigation

3. **Go to Data Model**
   - In the left sidebar, click **Data Model**

4. **Check the URL**
   - Look at the browser address bar
   - The URL will look like: `https://eu1.vena.io/modeler/data-model/12345`
   - The **Model ID** is the number at the end: `12345`

## Example

**URL:** `https://eu1.vena.io/modeler/data-model/67890`  
**Model ID:** `67890`

## Testing in RAG Bot

Once you have your Model ID, you can test with questions like:

- "give me all hierarchies"
- "what are my dimensions?"
- "show me my account members"
- "what's in my model?"

The system will automatically fetch live data from your Vena tenant using this Model ID.

## Note

- Each data model in your tenant has its own Model ID
- If you have multiple models, you'll need to use the Model ID for the specific model you want to query
- The Model ID is required for most Vena API operations
