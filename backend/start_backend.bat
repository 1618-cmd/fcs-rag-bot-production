@echo off
echo Starting FCS RAG Bot Backend...
echo.

cd /d "%~dp0"

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Copying from env.template...
    copy env.template .env
    echo.
    echo Please edit .env and add your API keys, then run this script again.
    pause
    exit /b 1
)

echo Starting uvicorn server...
echo.
python -m uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000

if errorlevel 1 (
    echo.
    echo ERROR: Backend failed to start!
    echo.
    echo Common issues:
    echo 1. Missing dependencies - Run: pip install -r requirements.txt
    echo 2. Missing .env file - Copy env.template to .env
    echo 3. Port 8000 in use - Close other applications
    echo.
    pause
)
