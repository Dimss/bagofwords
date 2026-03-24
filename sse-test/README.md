# SSE Hello World Server

Simple Server-Sent Events (SSE) example in Python.

## Quick Start with Docker (Recommended)

```bash
# Build and run with Makefile
make run

# View logs
make logs

# Test the stream
make test
```

Server will be available at `http://localhost:3000`

## Run Locally (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Start the SSE server
python3 server.py
```

Server will start at `http://localhost:3000`

## Test SSE Stream

### Option 1: Using Python Client
```bash
python3 client.py
```

### Option 2: Using curl
```bash
curl http://localhost:3000/stream
```

### Option 3: Using Browser
Open in your browser:
```
http://localhost:3000/stream
```

## Expected Output

The server will stream 10 "Hello World" messages, one per second:

```
data: Hello World #1 at 2026-03-24T10:30:00.123456

data: Hello World #2 at 2026-03-24T10:30:01.234567

data: Hello World #3 at 2026-03-24T10:30:02.345678

...

data: [DONE]
```

## Endpoints

- `GET /` - Server info
- `GET /stream` - SSE stream endpoint

## SSE Format

Server-Sent Events use a simple text format:
```
data: <message content>

```

Each event ends with two newlines (`\n\n`).

## Docker Commands (using Makefile)

```bash
make help      # Show all available commands
make build     # Build Docker image
make run       # Start container
make stop      # Stop container
make logs      # View logs
make test      # Test SSE endpoint
make clean     # Remove container and image
```

## Manual Docker Commands

```bash
# Build image
docker build -t sse-hello-world .

# Run container
docker run -d -p 3000:3000 --name sse-server sse-hello-world

# View logs
docker logs -f sse-server

# Stop and remove
docker stop sse-server && docker rm sse-server
```

## Features

- ✅ Async streaming with FastAPI
- ✅ Proper SSE headers (Cache-Control, X-Accel-Buffering)
- ✅ Timestamp on each event
- ✅ Graceful completion with [DONE] marker
- ✅ Works with curl, browser, and Python client
- ✅ Docker support with Makefile
