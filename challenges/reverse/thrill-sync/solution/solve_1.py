import websockets
import json
import asyncio


async def connect(host, port):
    uri = f"ws://{host}:{port}/websocket"
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        data = json.loads(response)
        if data["action"] == "welcome":
            print(data["message"])
            await websocket.send(json.dumps({"action": "login", "username": "ZoeWright", "password": "425kailua"}))
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
    asyncio.run(connect("localhost", 8081))