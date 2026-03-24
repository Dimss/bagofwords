#!/usr/bin/env python3
"""
Simple SSE Client to test the server
Run with: python3 client.py
"""
import requests
import time

def test_sse_stream():
    """Connect to SSE endpoint and print events"""
    url = "http://localhost:3000/stream"

    print(f"🔌 Connecting to {url}...")
    print("📡 Receiving SSE events:\n")

    start_time = time.time()
    event_count = 0

    try:
        # Stream the response
        response = requests.get(url, stream=True)

        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(f"[{time.time() - start_time:.2f}s] {decoded_line}")

                if decoded_line.startswith('data:'):
                    event_count += 1

                if '[DONE]' in decoded_line:
                    break

    except KeyboardInterrupt:
        print("\n\n⏹️  Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

    total_time = time.time() - start_time
    print(f"\n✅ Done! Received {event_count} events in {total_time:.2f} seconds")


if __name__ == "__main__":
    test_sse_stream()
