import websockets
import json
import asyncio
import argparse

async def connect(host, port):
    uri = f"ws://{host}:{port}/websocket"
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        data = json.loads(response)
        if data["action"] == "welcome":
            print(data["message"])
            await websocket.send(json.dumps({"action": "login", "username": "EthanClark", "password": "mz586Ostt0"}))
            response = await websocket.recv()
            data = json.loads(response)
        
            await websocket.send(json.dumps({"action": "flags", "token": data["token"]}))
            response = await websocket.recv()
            data = json.loads(response)
            print(data["flags"])

        else:
            print("Failed to connect to the server")
            return
        await websocket.close()


if __name__ == "__main__":
    argsparse = argparse.ArgumentParser(description="WebSocket client")
    argsparse.add_argument('--host', type=str, required=True, help='The host to connect to')
    argsparse.add_argument('--port', type=int, required=True, help='The port to connect to')
    args = argsparse.parse_args()

    asyncio.run(connect(args.host, args.port))