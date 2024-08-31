from typing import List
from subprocess import PIPE
from pwnlib.tubes.process import process
from execute_input import execute_input

BYTES_PLACEHOLDER = '"BYTES"'
RESTRICTED_DEFAULT = [
    "import",
    "=",
    "def",
    "exec",
    "eval",
    "compile",
    "os",
    "global",
    "try",
    "expect",
    "finally",
    "\\",
]
DEFAULT_MAX_LENGTH = 100
DEFAULT_MAX_LENGTH_DEOBF = 75


def execute(
    operation: str,
    shellcode_bytes: str,
    restricted_expr: list[str] = RESTRICTED_DEFAULT,
    restricted_bytes: list[bytes] = [],
    max_length=DEFAULT_MAX_LENGTH,
) -> dict[str, str]:
    code = operation.replace(BYTES_PLACEHOLDER, '"' + shellcode_bytes + '"')
    v, s = validate_input(
        operation, shellcode_bytes, restricted_expr, restricted_bytes, max_length
    )
    if not v:
        return {"error": s}
    try:
        v, b = execute_input(code)
        if not v:
            return {"error": b}
        if len(b) == 0:
            return {"error": "Invalid input"}
        if len(b) > DEFAULT_MAX_LENGTH_DEOBF:
            return {
                "error": f"Input is too long. Max length for deobfuscated bytecode is {str(DEFAULT_MAX_LENGTH_DEOBF)} bytes"
            }
        e, o = execute_shellcode(b)
        return {"res": o} if not e else {"error": e}
    except Exception as e:
        return {"error": s}


def validate_operation(input: str) -> tuple[bool, str]:
    if not input.startswith("[") or not input.endswith("]"):
        return False, "Input must be a list"
    if BYTES_PLACEHOLDER not in input:
        return False, "Input does not contain the placeholder"
    if input.count(BYTES_PLACEHOLDER) > 1:
        return False, "Input contains more than one placeholder"
    return False, "Input is not an array"


def validate_allowed_keywords(
    input: str, restricted_expressions: List[str] = RESTRICTED_DEFAULT
) -> tuple[bool, str]:
    for i in restricted_expressions:
        if i in input:
            return False, f"Keyword {i} not allowed in operation"
    return True, ""


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


def validate_input(
    operation: str,
    shellcode_bytes: str,
    restricted_expressions: List[str] = RESTRICTED_DEFAULT,
    restricted_bytes: List[bytes] = [],
    max_length: int = 300,
) -> tuple[bool, str]:
    v, s = validate_operation(operation)
    if not v:
        return (v, s)
    sb = [x for x in filter(lambda c: c != "", shellcode_bytes.strip().split("\\x"))]
    if len(sb) > max_length:
        return False, f"Input is too long. Max length is {str(max_length)} bytes"
    v, s = validate_allowed_keywords(operation, restricted_expressions)
    if not v:
        return (v, s)
    try:
        b = [int(x, 16) for x in sb]
        return validate_restricted_bytes(bytes(b), restricted_bytes)
    except ValueError:
        return False, "Byte values must be in the format \\x00"


def execute_shellcode(shellcode: bytes) -> tuple[str, str]:
    proc = process("./exec_shellcode", stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc.sendline(str(len(shellcode)))
    out, err = proc.communicate(shellcode)
    return err.decode(), out.decode()


def validate_shellcode_output(out: str, expected: str) -> tuple[bool, str]:
    if "error" in out:
        return False, out["error"]
    out = out["res"]
    if expected in out:
        return True, ""
    return False, f"Expected output was not printed.\n Output:\n {out}"
