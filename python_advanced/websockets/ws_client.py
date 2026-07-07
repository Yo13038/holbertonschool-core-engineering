#!/usr/bin/env python3
"""WebSocket client that sends one message to the echo server."""
import asyncio
import os
import websockets


async def connect_and_send(uri, message):
    """Send a single message to uri and return the server's response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        return await websocket.recv()


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    message = os.environ.get("WS_MESSAGE", "demo")
    response = asyncio.run(connect_and_send(uri, message))
    print(response, end="")
