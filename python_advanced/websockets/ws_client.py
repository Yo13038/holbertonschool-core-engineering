#!/usr/bin/env python3
"""Module to implement WebSocket client
"""

import os
import asyncio
from websockets import connect


async def connect_and_send(host="localhost", port=8765):


    uri = f"ws://{host}:{port}"
    
    async with connect(uri) as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(connect_and_send())