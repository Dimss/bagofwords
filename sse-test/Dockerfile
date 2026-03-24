FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY server.py .
COPY index.html .

# Expose port
EXPOSE 3000

# Run the server with uvicorn and multiple workers
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000", "--workers", "4"]
