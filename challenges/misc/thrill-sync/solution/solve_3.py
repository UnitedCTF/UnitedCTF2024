import websockets
import json
import asyncio
import sqlite3
import argparse

def read_tokens():
    db = sqlite3.connect("thrill-sync.db")
    sql = "SELECT token,user_id FROM tokens"
    hashes = db.execute(sql).fetchall()
    db.close()
    return hashes


async def connect(host, port):
    uri = f"ws://{host}:{port}/websocket"
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        data = json.loads(response)
        if data["action"] == "welcome":
            print(data["message"])
            tokens = read_tokens()
            for token in tokens:
                await websocket.send(json.dumps({"action": "flags", "token": token[0]}))
                response = await websocket.recv()
                data = json.loads(response)
                if data["status"] == "success":
                    if len(data["flags"]) > 0:
                        print(token, data["flags"])
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