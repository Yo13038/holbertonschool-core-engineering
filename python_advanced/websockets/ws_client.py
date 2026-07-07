#!/usr/bin/env python3
"""Module to implement WebSocket client
"""


import asyncio
from websockets import connect


async def connect_and_send(host="localhost", port=8765):
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(connect_and_send())
