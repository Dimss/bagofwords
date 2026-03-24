#!/bin/bash
# Quick test script for SSE server

echo "🧪 Testing SSE Hello World Server"
echo "=================================="
echo ""

# Check if server is running
if ! curl -s http://localhost:3000/api > /dev/null 2>&1; then
    echo "❌ Server is not running!"
    echo "Please start the server first:"
    echo "  python3 server.py"
    echo "  OR"
    echo "  make run"
    exit 1
fi

echo "✅ Server is running"
echo ""
echo "📡 Testing SSE stream..."
echo ""

# Test the stream (show first 5 events)
curl -N http://localhost:3000/stream 2>/dev/null | head -n 10

echo ""
echo "✅ Test complete!"
