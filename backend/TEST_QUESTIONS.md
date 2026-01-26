# Test Questions for Vena API Integration

## Questions That Trigger Vena API (Need Model ID)

These questions will fetch live data from your Vena tenant:

1. **"give me all hierarchies"**
   - Fetches: All dimension members (extracted from intersections)
   - Shows: List of members for each dimension

2. **"what are my dimensions?"**
   - Fetches: Dimension names (extracted from intersections)
   - Shows: List of all dimensions in your model

3. **"show me my account members"**
   - Fetches: Account dimension members
   - Shows: All unique Account values from your data

4. **"what accounts do I have?"**
   - Fetches: Account dimension members
   - Shows: List of your account codes/names

5. **"what's in my model?"**
   - Fetches: Model structure and dimensions
   - Shows: Overview of your data model

6. **"help me build a script for my entities"**
   - Fetches: Entity dimension members
   - Shows: Your entity list for script generation

## Questions That Don't Need Model ID

These work from knowledge base only:

- "How do I write VenaQL?"
- "What is Line Item Details?"
- "Explain Vena Copilot"
- "How do I configure dimensions?"

## How to Test

### Option 1: Via Chat Interface (Frontend)
1. Start your backend: `cd backend && uvicorn src.api.main:app --reload`
2. Start your frontend: `cd frontend && npm run dev`
3. Open chat interface
4. Ask: "give me all hierarchies" (will work but show message about Model ID)
5. Or add Model ID to the question: "give me all hierarchies for model 12345"

### Option 2: Via API Directly
```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "give me all hierarchies",
    "vena_model_id": "YOUR_MODEL_ID"
  }'
```

### Option 3: Test Script
```bash
python backend/test_with_model_id.py YOUR_MODEL_ID
```
