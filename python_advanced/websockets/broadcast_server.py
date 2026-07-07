#!/usr/bin/env python3
"""
Module that give a response to all from the server
"""


import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

clients = set()


async def connection_handler(websocket):
    clients.add(websocket)

    try:
        async for message in websocket:
            broadcast = f"B:{message}"

            if clients:
                await asyncio.gather(
                    *[client.send(broadcast) for client in clients]
                )

    except ConnectionClosed:
        pass
    finally:
        clients.discard(websocket)


async def main():
    """Main entry point to start the broadcast server.
    """
    async with websockets.serve(connection_handler, "0.0.0.0", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
