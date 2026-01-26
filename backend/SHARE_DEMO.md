# How to Share the Vena API Demo Page

## Quick Option: Netlify Drop (Recommended - 2 minutes)

1. Go to: https://app.netlify.com/drop
2. Drag and drop the file: `backend/vena_api_demo.html`
3. You'll instantly get a public URL like: `https://random-name-123.netlify.app`
4. Share that URL with your manager!

**No signup required!**

---

## Alternative: Local Server + ngrok

If you want to use ngrok:

1. **Install ngrok:**
   - Download from: https://ngrok.com/download
   - Extract to a folder
   - Sign up for free account at https://dashboard.ngrok.com/signup
   - Get your authtoken from dashboard

2. **Start local server** (already running on port 8000):
   ```bash
   cd backend
   python -m http.server 8000
   ```

3. **In another terminal, run ngrok:**
   ```bash
   ngrok http 8000
   ```

4. **Copy the public URL** (e.g., `https://abc123.ngrok.io`)
   - Access the demo at: `https://abc123.ngrok.io/vena_api_demo.html`

---

## Current Local Access

The demo is currently running locally at:
- **http://localhost:8000/vena_api_demo.html**

(Only accessible on your computer)

---

## File Location

The demo file is at:
- `backend/vena_api_demo.html`

You can also just email this file directly - it's a standalone HTML file that works offline!
