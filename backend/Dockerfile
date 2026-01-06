FROM python:3.11-slim

WORKDIR /app

# Install build dependencies (needed for some Python packages)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Remove build dependencies to reduce image size
RUN apt-get purge -y gcc g++ && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy application
COPY . .

# Run the app
CMD uvicorn src.api.main:app --host 0.0.0.0 --port ${PORT:-8000}
