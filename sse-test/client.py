#!/usr/bin/env python3
"""
Simple SSE Client to test the server
Run with: python3 client.py
"""
import requests
import time
import json

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

        current_event = {}
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')

                if decoded_line.startswith('event:'):
                    current_event['type'] = decoded_line.split(':', 1)[1].strip()
                elif decoded_line.startswith('data:'):
                    data_str = decoded_line.split(':', 1)[1].strip()
                    try:
                        data = json.loads(data_str)
                        event_count += 1
                        print(f"[{time.time() - start_time:.2f}s] Event: {current_event.get('type', 'message')}")
                        print(f"  Data: {data['data']}")
                        print(f"  Timestamp: {data.get('timestamp', 'N/A')}")
                        print(f"  Seq: {data.get('seq', 'N/A')}")
                        print()

                        if data.get('event') == 'done':
                            break
                    except json.JSONDecodeError:
                        print(f"[{time.time() - start_time:.2f}s] {decoded_line}")
                        if '[DONE]' in decoded_line:
                            break
                    current_event = {}
                elif not decoded_line:
                    # Empty line marks end of event
                    current_event = {}

    except KeyboardInterrupt:
        print("\n\n⏹️  Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

    total_time = time.time() - start_time
    print(f"\n✅ Done! Received {event_count} events in {total_time:.2f} seconds")


if __name__ == "__main__":
    test_sse_stream()
