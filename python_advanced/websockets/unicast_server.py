#!/urs/bin/env python3
"""
Module to manage multiple connected client
"""


import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


clients = set()

async def connection_handler(websocket):
    
    clients.add(websocket)
    try:
        async for message in websocket:
                await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    
    finally:
         clients.discard(websocket)

async def main():

    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
        asyncio.run(main())
