# Vercel Deployment Guide

## Quick Deploy

1. **Connect GitHub to Vercel:**
   - Go to https://vercel.com
   - Sign in with GitHub
   - Click "Add New Project"
   - Select your repository: `1618-cmd/fcs-rag-bot-production`
   - Set Root Directory: `frontend`

2. **Configure Build Settings:**
   - Framework Preset: Next.js (auto-detected)
   - Build Command: `npm run build` (auto)
   - Output Directory: `.next` (auto)
   - Install Command: `npm install` (auto)

3. **Set Environment Variables:**
   - `NEXT_PUBLIC_API_URL` = Your Railway backend URL
     - Example: `https://your-app.railway.app`
     - Or use Railway's default domain

4. **Deploy!**
   - Click "Deploy"
   - Wait for build to complete
   - Get your live URL!

## Custom Domain (Optional)

1. In Vercel project settings → Domains
2. Add your domain
3. Follow DNS instructions
4. Vercel handles SSL automatically

## Environment Variables

Required:
- `NEXT_PUBLIC_API_URL` - Your backend API URL

Optional:
- None for now

## Troubleshooting

- **Build fails?** Check that `npm run build` works locally
- **API not connecting?** Verify `NEXT_PUBLIC_API_URL` is set correctly
- **CORS errors?** Make sure backend CORS allows your Vercel domain


