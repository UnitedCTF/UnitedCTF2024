from uvicorn import run
from os import getenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from shellcode_obfuscation import execute, validate_shellcode_output

PORT = int(getenv("PORT", 8000))
LEVEL1_EXPECTED_OUTPUT = "Barbe à papa"
LEVEL2_EXPECTED_OUTPUT = "Manèges"
LEVEL3_EXPECTED_OUTPUT = "UnitedCTF"


class Request(BaseModel):
    shellcode_bytes: str


app = FastAPI()


@app.get("/")
async def root():
    index = open("web/index.html", "r").read()
    return HTMLResponse(content=index, status_code=200)


@app.get("/index.js")
async def index_js():
    return FileResponse(
        path="web/index.js", status_code=200, media_type="application/javascript"
    )


@app.post("/level1")
async def level1(req: Request):
    out = execute(req.shellcode_bytes)
    v, s = validate_shellcode_output(out, LEVEL1_EXPECTED_OUTPUT)
    if not v:
        return {"error": s}
    return {"flag": getenv("FLAG1")}


@app.post("/level2")
async def level2(req: Request):
    out = execute(req.shellcode_bytes, restricted_bytes=[b"\x0f", b"\x05"])
    v, s = validate_shellcode_output(out, LEVEL2_EXPECTED_OUTPUT)
    if not v:
        return {"error": s}
    return {"flag": getenv("FLAG2")}

@app.post("/level3")
async def level3(req: Request):
    out = execute(
        req.shellcode_bytes,
        restricted_bytes=[b"\x0f", b"\x05"],
        number_of_diff_bytes=1000,
        max_length=300
    )
    v, s = validate_shellcode_output(out, LEVEL3_EXPECTED_OUTPUT)
    if not v:
        return {"error": s}
    return {"flag": getenv("FLAG3")}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=PORT)