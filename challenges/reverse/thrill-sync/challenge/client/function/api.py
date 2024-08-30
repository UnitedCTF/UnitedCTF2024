import json


async def send_message(ws, message):
    if ws.closed:
        print("Connection closed")
        return None
    await ws.send(json.dumps(message))
    response = await ws.recv()
    data = json.loads(response)
    return data


async def login(ws, session, username, password):
    payload = {"action": "login", "username": username, "password": password}
    data = await send_message(ws, payload)
    status = data["status"]
    if status == "success":
        session.token = data["token"]
        return True
    else:
        return False


async def logout(ws, session):
    payload = {"action": "logout", "token": session.token}
    data = await send_message(ws, payload)
    return data["status"] == "success"

async def get_attractions(ws):
    payload = {"action": "attractions"}
    data = await send_message(ws, payload)
    array_attractions = data["attractions"]
    return  array_attractions


async def get_attraction(ws, attraction):
    payload = {"action": "attraction", "attraction": attraction}
    data = await send_message(ws, payload)
    att = data["attraction"]
    return  att


async def get_flags(ws, session):
    payload = {"action": "flags", "token": session.token}
    data = await send_message(ws, payload)
    if data["status"] != "success":
        return None
    flags = data["flags"]
    return flags


async def register(ws, username, password, email):
    payload = {"action": "register", "username": username, "password": password, "email": email}
    data = await send_message(ws, payload)
    return data["status"] == "success"


async def ping(ws):
    payload = {"action": "ping"}
    data = await send_message(ws, payload)
    return data["status"] == "pong"
