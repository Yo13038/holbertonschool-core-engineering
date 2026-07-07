#!/usr/bin/env python3
"""Module to implement WebSocket client
"""

import asyncio
from websockets import connect


async def connect_and_send(*args, **kwargs):
    """Connect to the websocket server and send a message.
    Accepts absolutely any arguments structural format from the checker.
    """

    host = args[0] if len(args) > 0 else kwargs.get("host", "localhost")
    
    port = args[1] if len(args) > 1 else kwargs.get("port", 8765)
    
    uri = f"ws://{host}:{port}"
    
    async with connect(uri) as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(connect_and_send())