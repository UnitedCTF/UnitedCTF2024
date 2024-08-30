import argparse
import asyncio
import json

import websockets
from function import navigation, session

def parse_args():
    parser = argparse.ArgumentParser(description="WebSocket client")
    parser.add_argument('--host', type=str, required=True, help='The host to connect to')
    parser.add_argument('--port', type=int, required=True, help='The port to connect to')
    return parser.parse_args()

async def connect(host, port, session_data):
    uri = f"ws://{host}:{port}/websocket"
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        data = json.loads(response)
        if data["action"] == "welcome":
            print(data["message"])
            session_data.connected = True
            while session_data.connected:
                await navigation.run_navigation(session_data, websocket)
        else:
            print("Failed to connect to the server")
            return
        await websocket.close()


if __name__ == "__main__":
    args = parse_args()
    s = session.Session()
    asyncio.run(connect(args.host, args.port, s))