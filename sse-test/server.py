#!/usr/bin/env python3
"""
Simple SSE (Server-Sent Events) Hello World Server
Run with: python3 server.py
Test with: curl http://localhost:8080/stream
"""
import asyncio
import time
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sse_schema import SSEEvent, format_sse_event

app = FastAPI()

# Enable CORS for browser testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def event_generator():
    """Generate SSE events - Hello World example"""
    for i in range(10):
        # Create SSEEvent with structured data
        event = SSEEvent(
            event="message",
            data={
                "message": f"Hello World #{i+1}",
                "count": i+1
            },
            seq=i
        )

        # Format as SSE string
        message = format_sse_event(event)
        print(f"Sending: {event.event} - {event.data}")
        yield message

        # Wait 1 second between messages
        await asyncio.sleep(1)

    # Send completion event
    done_event = SSEEvent(
        event="done",
        data={"status": "complete", "total": 10}
    )
    yield format_sse_event(done_event)


async def create_stream():
    """Create and return SSE stream"""
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable nginx buffering
        }
    )


@app.get("/stream")
async def stream():
    """SSE endpoint that streams Hello World messages"""
    return await create_stream()


@app.get("/")
async def root():
    """Serve the HTML client"""
    return FileResponse("index.html")


@app.get("/api")
async def api_info():
    """API endpoint with instructions"""
    return {
        "message": "SSE Hello World Server",
        "endpoints": {
            "/": "HTML client",
            "/stream": "SSE stream endpoint",
            "/api": "This info endpoint"
        },
        "test": "curl http://localhost:3000/stream"
    }


if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting SSE Hello World Server...")
    print("📡 SSE Stream: http://localhost:3000/stream")
    print("🧪 Test with: curl http://localhost:3000/stream")
    uvicorn.run(app, host="0.0.0.0", port=3000)
