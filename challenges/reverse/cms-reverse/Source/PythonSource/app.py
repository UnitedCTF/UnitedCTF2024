from fastapi import FastAPI,Response,Form
import uvicorn
from typing import Annotated
import base64
from hashlib import sha256
import time
app = FastAPI(docs_url=None, redoc_url=None)

SERVER_ID = "cce13886a4e64875800f6ee80d5a7dfa"
FLAG3 = "FLAG3"
FLAG4 = "FLAG4"
FLAG5 = "FLAG5"
TIME_BUFFER_NS = 1_000_000_000
@app.get("/74ba5d54-a5a7-4390-a1a1-4fdde2e66a05")
def getHash():
    return Response(sha256(bytes(SERVER_ID,"utf-8")).hexdigest(), media_type="text/plain")

@app.get("/a5276b40-5acf-44a8-b0d0-56819516145f")
def getHash2():
    t = str(time.time_ns())
    return Response(sha256(bytes(SERVER_ID + t,"utf-8")).hexdigest() + '@' + t, media_type="text/plain")

@app.post("/61209e4d-3da2-42e8-a2aa-e1d5f281854b")
def validateFlag3(timestamp: Annotated[str, Form()], key: Annotated[str, Form()]):
    try:
        if int(timestamp) < time.time_ns() - TIME_BUFFER_NS:
            return Response("Invalid timestamp", media_type="text/plain", status_code=400)
        kbytes = base64.b64decode(key)
        key = int(timestamp).to_bytes(8, byteorder='big')
        kbytes = bytes([b ^ key[i % len(key)] for i,b in enumerate(kbytes)])
        serv_id = base64.b64decode(kbytes)
        if serv_id != bytes(SERVER_ID,"utf-8"):
            return Response("Invalid key", media_type="text/plain", status_code=400)
        return Response(FLAG3, media_type="text/plain")
    except:
        return Response("Bad request", media_type="text/plain", status_code=400)

@app.post("/9f18010c-c4e9-47a9-8545-ffda55cd03cc")
def validateFlag4(timestamp: Annotated[str, Form()], key: Annotated[str, Form()]):
    try:
        if int(timestamp) < time.time_ns() - TIME_BUFFER_NS:
            return Response("Invalid timestamp", media_type="text/plain", status_code=400)
        kbytes = base64.b64decode(key)
        key = int(timestamp).to_bytes(8, byteorder='big')
        kbytes = bytes([b ^ key[i % len(key)] for i,b in enumerate(kbytes)])
        serv_id = base64.b64decode(kbytes)
        if serv_id != bytes(SERVER_ID,"utf-8"):
            return Response("Invalid key", media_type="text/plain", status_code=400)
        return Response(FLAG4, media_type="text/plain")
    except:
        return Response("Bad request", media_type="text/plain", status_code=400)


@app.post("/8af81be4-f251-4996-9688-3c074891fb00")
def validateFlag5(timestamp: Annotated[str, Form()], key: Annotated[str, Form()]):
    try:
        if int(timestamp) < time.time_ns() - TIME_BUFFER_NS:
            return Response("Invalid timestamp", media_type="text/plain", status_code=400)
        kbytes = base64.b64decode(key)
        key = bytes(SERVER_ID,"utf-8")
        kbytes = bytes([b ^ key[i % len(key)] for i,b in enumerate(kbytes)])
        kbytes = base64.b64decode(kbytes)
        key = int(timestamp).to_bytes(8, byteorder='little')
        kbytes = bytes([b ^ key[i % len(key)] for i,b in enumerate(kbytes)])
        serv_id = base64.b64decode(kbytes)
        serv_id = serv_id.decode().split("@")
        cln = serv_id[1]
        serv_id = serv_id[0]
        if serv_id != SERVER_ID:
            return Response("Invalid key", media_type="text/plain", status_code=400)
        if not validateCLN(cln,timestamp):
            return Response("Invalid CLN", media_type="text/plain", status_code=400)
        return Response(FLAG5, media_type="text/plain")
    except:
        print("error")
        return Response("Bad request", media_type="text/plain", status_code=400)

def validateCLN(cln,timestamp):
    try:
        cln = bytes.fromhex(cln).decode()
        scln = cln.split("@")
        b64 = scln[0]
        ts = int(scln[1])
        key = int(ts).to_bytes(8, byteorder='big')
        kbytes = base64.b64decode(b64)

        kbytes = bytes([b ^ key[i % len(key)] for i,b in enumerate(kbytes)]).decode()
        if int(timestamp) < time.time_ns() - TIME_BUFFER_NS:
            return False
        return sha256(bytes(SERVER_ID + str(ts),"utf-8")).hexdigest() == kbytes
    except:
        return False


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9860)