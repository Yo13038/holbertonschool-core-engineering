#!/usr/bin/env python3
"""
Module To implement a server that accepts connections ans echoes back
"""


import asyncio
import websockets


async def connection_handler(websocket):
    """function to handle client request"""
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
