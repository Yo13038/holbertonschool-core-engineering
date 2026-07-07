#!/usr/bin/env python3
"""
Module to integrate WebSocket communication into a web-facing Python application.
"""


from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    
    return HTMLResponse("<h1>WebSocket App</h1>")

async def websocket_endpoint(websocket):
    
    await websocket.accept()
    
    async for message in websocket.iter_text():
        await websocket.send_text(message)    

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
