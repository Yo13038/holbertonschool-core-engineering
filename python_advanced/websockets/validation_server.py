#!/usr/bin/env python3
"""
Module add basic message validation to a server
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

async def connection_handler(websocket):
    
    async for message in websocket:
        
        try:
            not_empty_message = message.strip()

            if not_empty_message:
                await websocket.send(f"OK:{message}")
            else:
                await websocket.send("ERR:EMPTY")
        except ConnectionClosed:
            pass

async def main():

    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    try:
       asyncio.run(main())
    except KeyboardInterrupt:
       pass
