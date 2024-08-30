from fastapi import FastAPI
import uvicorn
import os
from pydantic import BaseModel
from execute_input import execute_input
from shellcode_obfuscation import validate_input,execute_shellcode,RESTRICTED_DEFAULT,validate_shellcode_output

DEFAULT_OPERATION = "[int(x) for x in b\"BYTES\"]"
LEVEL_2_RESTRICTED = RESTRICTED_DEFAULT + ["+","-","^","*","/","%","//"]
DEFAULT_MAX_LENGTH = 100
DEFAULT_MAX_LENGTH_DEOBF = 75
app = FastAPI()

class Request(BaseModel):
    shellcode_bytes:str
    operation:str


@app.post("/level1")
async def level1(req:Request):
    out = execute(DEFAULT_OPERATION,req.shellcode_bytes)
    v,s = validate_shellcode_output(out)
    if not v:
        return {"error":s}
    return {"flag":os.getenv("FLAG1")}

@app.post("/obflevel1")
async def olevel1(req:Request):
    print(req.operation)
    out = execute(req.operation,req.shellcode_bytes,restricted_bytes=[b"\x0f",b"\x05",b"\x31",b"\x89"])
    v,s = validate_shellcode_output(out)
    if not v:
        return {"error":s}
    return {"flag":os.getenv("OBF_FLAG1")}

@app.post("/obflevel2")
async def olevel2(req:Request):
    out = execute(req.operation,req.shellcode_bytes,restricted_bytes=[b"\x0f",b"\x05",b"\x31",b"\x89"],restricted_expr=LEVEL_2_RESTRICTED)
    v,s = validate_shellcode_output(out)
    if not v:
        return {"error":s}
    return {"flag":os.getenv("OBF_FLAG2")}

@app.post("/obflevel3")
async def olevel3(req:Request):
    out = execute(DEFAULT_OPERATION,req.shellcode_bytes,restricted_bytes=[b"\x0f",b"\x05"])
    v,s = validate_shellcode_output(out)
    if not v:
        return {"error":s}
    return {"flag":os.getenv("OBF_FLAG3")}

def execute(operation:str,shellcode_bytes:str,restricted_expr:list[str]=RESTRICTED_DEFAULT,restricted_bytes:list[bytes]=[],max_length=DEFAULT_MAX_LENGTH) -> dict[str,str]:
    code = operation.replace("\"BYTES\"","\"" + shellcode_bytes+"\"")
    v,s = validate_input(operation,shellcode_bytes,restricted_expr,restricted_bytes,max_length)
    if not v:
        return {"error":s}
    try:
        b = execute_input(code)
        if len(b) > DEFAULT_MAX_LENGTH_DEOBF:
            return {"error":f"Input is too long. Max length for deobfuscated bytecode is {str(DEFAULT_MAX_LENGTH_DEOBF)} bytes"}
        e,o = execute_shellcode(b)
        return {"res":o} if not e else {"error":e}
    except Exception as e:
        print(e)
        return {"error":s}

PORT=int(os.getenv("PORT",8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)