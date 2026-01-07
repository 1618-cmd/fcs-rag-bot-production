# FCS RAG Bot - Frontend

Polished, minimal Next.js frontend for the FCS RAG Bot.

<!-- Updated: Force Vercel to use Next.js framework preset -->

## Features

- ✨ Beautiful, minimal chat interface
- 🎨 Polished UI with smooth animations
- 📚 Source citations display
- ⚡ Real-time responses
- 🔄 Loading states and error handling

## Setup

```bash
# Install dependencies
npm install

# Create environment file
cp .env.local.example .env.local
# Edit .env.local with your API URL

# Run development server
npm run dev
```

Visit http://localhost:3000

## Configuration

Set `NEXT_PUBLIC_API_URL` in `.env.local`:
- Local: `http://localhost:8000`
- Production: Your Railway backend URL

## Build for Production

```bash
npm run build
npm start
```

## Deploy to Vercel

1. Connect your GitHub repo to Vercel
2. Set environment variable: `NEXT_PUBLIC_API_URL`
3. Deploy!
