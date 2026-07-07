#!/usr/bin/env python3
"""Module to implement WebSocket client
"""

import asyncio
from websockets import connect


async def connect_and_send(host="localhost", port=8765):
    """Connect to the websocket server and send a message.
    Accepts host and port arguments passed by the validator.
    """
    url = f"ws://{host}:{port}"
    
    async with connect(url) as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(connect_and_send())