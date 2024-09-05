from typing import List
from subprocess import Popen,PIPE

DEFAULT_MAX_LENGTH = 75
DEFAULT_NUMBER_OF_DIFF_BYTES = 100_000

class SIZE_RESTRICTIONS:
    def __init__(self, max_length: int = DEFAULT_MAX_LENGTH, max_diff_bytes: int = DEFAULT_NUMBER_OF_DIFF_BYTES):
        self.max_length = max_length
        self.max_diff_bytes = max_diff_bytes

DEFAULT_SIZE_RESTRICTION = SIZE_RESTRICTIONS()
def execute(
    shellcode_bytes: str,
    restricted_bytes: list[bytes] = [],
    size_restrictions: list[SIZE_RESTRICTIONS] = [DEFAULT_SIZE_RESTRICTION]
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
        bytecode_len = len(b)
        if bytecode_len == 0:
            return {"error": "Invalid input"}
        size_restrictions.sort(key=lambda x: x.max_length)
        valid = False
        for sr in size_restrictions:
            if valid:
                break
            max_length = sr.max_length
            if bytecode_len > max_length:
                continue
            print(bytecode_len, max_length)
            if len(list) > sr.max_diff_bytes:
                return {"error": f"Too many different bytes ({str(len(list))}). Max number of different bytes for shellcode of length {str(max_length)} and more is {str(sr.max_diff_bytes)}"}
            valid = True
        if not valid:
            return {"error": f"Shellcode is too long. Max length is {size_restrictions[-1].max_length}"}
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
    proc = Popen(["./exec_shellcode",hex_str], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.wait(timeout=5)
    out, err = proc.stdout.read(), proc.stderr.read()
    try:
        return err.decode("latin-1"), out.decode("latin-1")
    except Exception:
        return f"Error decoding output, byte string received:\nout ->{str(out)}\nerr ->{str(err)}", ""


def validate_shellcode_output(out: dict[str,str], expected: str) -> tuple[bool, str]:
    if "error" in out:
        return False, str(out["error"])
    out = str(out["res"])
    if expected in out:
        return True, ""
    return False, f"Expected output was not printed.\nOutput:\n{out}"
