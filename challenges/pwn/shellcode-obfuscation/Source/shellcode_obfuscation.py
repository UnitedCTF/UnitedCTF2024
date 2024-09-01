from typing import List
from subprocess import Popen,PIPE

DEFAULT_MAX_LENGTH = 75
DEFAULT_NUMBER_OF_DIFF_BYTES = 100_000

def execute(
    shellcode_bytes: str,
    restricted_bytes: list[bytes] = [],
    number_of_diff_bytes: int = DEFAULT_NUMBER_OF_DIFF_BYTES,
    max_length=DEFAULT_MAX_LENGTH,
) -> dict[str, str]:
    try:
        b = [int(x,16) for x in filter(lambda c: c != "", shellcode_bytes.strip().split("\\x"))]
        v,s = validate_restricted_bytes(bytes(b), restricted_bytes)       
        if not v:
            return {"error": s} 
        list = []
        for i in b:
            if i not in list:
                list.append(i)
        if len(list) > number_of_diff_bytes:
            return {"error": f"Too many different bytes. Max number of different bytes is {str(number_of_diff_bytes)}"}
        
        if len(b) == 0:
            return {"error": "Invalid input"}
        if len(b) > max_length:
            return {
                "error": f"Input is too long. Max length for bytecode is {str(max_length)} bytes"
            }
        e, o = execute_shellcode(bytes(b))
        return {"res": o} if not e else {"error": e}
    except Exception as e:
        return {"error": e}

def validate_restricted_bytes(
    input: bytes, restricted_bytes: List[bytes]
) -> tuple[bool, str]:
    invalid_found = []
    for i in restricted_bytes:
        if i in input:
            invalid_found.append("\\x{:02x}".format(int(i.hex(), 16)))
    if invalid_found:
        return False, f'Bytes {",".join(invalid_found)} are restricted'
    return True, ""

def execute_shellcode(shellcode: bytes) -> tuple[str, str]:
    hex = shellcode.hex()
    hex_str = "\\x" + '\\x'.join([''.join([hex[i],hex[i + 1]]) for i in range(0,len(hex),2)])
    print(hex_str)
    proc = Popen(["./exec_shellcode",hex_str], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.wait(timeout=5)
    out, err = proc.stdout.read(), proc.stderr.read()
    try:
        return err.decode("latin-1"), out.decode("latin-1")
    except Exception:
        return f"Error decoding output, byte string received:\nout ->{str(out)}\nerr ->{str(err)}", ""


def validate_shellcode_output(out: dict[str,str], expected: str) -> tuple[bool, str]:
    print(out)
    if "error" in out:
        return False, str(out["error"])
    out = str(out["res"])
    if expected in out:
        return True, ""
    return False, f"Expected output was not printed.\n Output:\n {out}"
