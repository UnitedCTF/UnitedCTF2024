from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import subprocess
import re
import os

PORT = int(os.getenv('PORT', 8000))

LEVEL1_EXPECTED_OUTPUT = 'Barbe à papa'
LEVEL2_EXPECTED_OUTPUT = 'Popcorn'
LEVEL3_EXPECTED_OUTPUT = 'Manèges'
LEVEL4_EXPECTED_OUTPUT = 'UnitedCTF'

BYTES_REGEX = r'\\x[\da-fA-F]+'
DEFAULT_MAX_LENGTH = 75
EXECUTION_TIMEOUT = 3


def format_bytes(bts: list[int]) -> str:
    return ''.join(['\\x{:02x}'.format(b) for b in bts])

def execute_shellcode(shellcode: str) -> tuple[int, str, str]:
    proc = subprocess.Popen(['./exec_shellcode', shellcode], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        proc.wait(timeout=EXECUTION_TIMEOUT)
    except Exception:
        return '', f'Execution timed out after {EXECUTION_TIMEOUT} seconds.'
    out, err = proc.stdout.read(), proc.stderr.read()
    try:
        return proc.returncode, out.decode('latin-1'), err.decode('latin-1')
    except Exception:
        return proc.returncode, str(out), str(err)


class Request(BaseModel):
    shellcode_bytes: str

app = FastAPI()


@app.get('/')
async def root():
    return FileResponse(path='web/index.html', status_code=200, media_type='text/html')

@app.get('/index.js')
async def index_js():
    return FileResponse(path='web/index.js', status_code=200, media_type='application/javascript')

@app.post('/level1')
async def level1(req: Request):
    shellcode = req.shellcode_bytes
    shellcode_len = len(req.shellcode_bytes) // 4

    if not re.match(BYTES_REGEX, shellcode):
        return {'error': 'Invalid input.'}
    if shellcode_len > DEFAULT_MAX_LENGTH:
        return {'error': f'Shellcode is too long, max length is {DEFAULT_MAX_LENGTH} bytes.'}

    ret, out, err = execute_shellcode(shellcode)
    if LEVEL1_EXPECTED_OUTPUT not in out:
        return {'error': f'Output did not contain "{LEVEL1_EXPECTED_OUTPUT}".\nRETURN CODE: {ret}\nSTDOUT:\n{out}\nSTDERR:\n{err}'}

    return {'flag': os.getenv('FLAG1')}

@app.post('/level2')
async def level2(req: Request):
    shellcode = req.shellcode_bytes
    shellcode_len = len(req.shellcode_bytes) // 4

    if not re.match(BYTES_REGEX, shellcode):
        return {'error': 'Invalid input.'}
    if shellcode_len > DEFAULT_MAX_LENGTH:
        return {'error': f'Shellcode is too long, max length is {DEFAULT_MAX_LENGTH} bytes.'}
    
    shellcode_bytes = set(bytes.fromhex(shellcode.replace('\\x', '')))
    restricted_bytes = shellcode_bytes & {0x05, 0x0f}
    if restricted_bytes:
        return {'error': f'Restricted bytes were found in your shellcode: {format_bytes(restricted_bytes)}.'}

    ret, out, err = execute_shellcode(shellcode)
    if LEVEL2_EXPECTED_OUTPUT not in out:
        return {'error': f'Output did not contain "{LEVEL2_EXPECTED_OUTPUT}".\nRETURN CODE: {ret}\nSTDOUT:\n{out}\nSTDERR:\n{err}'}

    return {'flag': os.getenv('FLAG2')}

@app.post('/level3')
async def level3(req: Request):
    shellcode = req.shellcode_bytes
    shellcode_len = len(req.shellcode_bytes) // 4

    if not re.match(BYTES_REGEX, shellcode):
        return {"error": 'Invalid input.'}
    if shellcode_len > DEFAULT_MAX_LENGTH:
        return {'error': f'Shellcode is too long, max length is {DEFAULT_MAX_LENGTH} bytes.'}
    
    shellcode_bytes = set(bytes.fromhex(shellcode.replace('\\x', '')))
    restricted_bytes = shellcode_bytes & (set(range(0x00, 0x0f+1)) | {0x31, 0x89})
    if restricted_bytes:
        return {'error': f'Restricted bytes were found in your shellcode: {format_bytes(restricted_bytes)}.'}

    ret, out, err = execute_shellcode(shellcode)
    if LEVEL3_EXPECTED_OUTPUT not in out:
        return {'error': f'Output did not contain "{LEVEL3_EXPECTED_OUTPUT}".\nRETURN CODE: {ret}\nSTDOUT:\n{out}\nSTDERR:\n{err}'}

    return {'flag': os.getenv('FLAG3')}

@app.post('/level4')
async def level4(req: Request):
    shellcode = req.shellcode_bytes
    shellcode_len = len(req.shellcode_bytes) // 4

    if not re.match(BYTES_REGEX, shellcode):
        return {"error": 'Invalid input.'}

    shellcode_bytes = set(bytes.fromhex(shellcode.replace('\\x', '')))
    restricted_bytes = shellcode_bytes & {0x05, 0x0f}
    if restricted_bytes:
        return {'error': f'Restricted bytes were found in your shellcode: {format_bytes(restricted_bytes)}.'}

    if (len(shellcode_bytes) > 15 or shellcode_len > 600) and (len(shellcode_bytes) > 20 or shellcode_len > 300):
        return {'error': f'Your shellcode did not respect either of the sets of restrictions: {len(shellcode)} bytes long, {len(shellcode_bytes)} distinct bytes.'}

    ret, out, err = execute_shellcode(shellcode)
    if LEVEL4_EXPECTED_OUTPUT not in out:
        return {'error': f'Output did not contain "{LEVEL4_EXPECTED_OUTPUT}".\nRETURN CODE: {ret}\nSTDOUT:\n{out}\nSTDERR:\n{err}'}

    return {'flag': os.getenv('FLAG4')}


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=PORT)