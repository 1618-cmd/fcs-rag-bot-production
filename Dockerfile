FROM python:3.11-slim

WORKDIR /app

# Install only essential system dependencies (minimal to avoid timeout)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/ .

# Expose port
EXPOSE 8000

# Use environment variable PORT (Railway provides this)
CMD uvicorn src.api.main:app --host 0.0.0.0 --port ${PORT:-8000}

