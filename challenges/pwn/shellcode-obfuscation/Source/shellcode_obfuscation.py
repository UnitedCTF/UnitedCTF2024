from typing import List
from subprocess import Popen,PIPE
import pwnlib.tubes.process
#info to give:
# AMD64/x86_64 assembly
# only read,write,exit and sigreturn syscalls allowed
# To get the flag you need to print "Hello World" to stdout
# Restricted bytes are: [RESTRICTED_BYTES]
# Shellcode passed in the format \x00\x01\x02\x03
# Can execute code on the bytes with [int({operations(x)}) for x in bytes] to transform the bytes into a valid shellcode
# Restricted keywords are: [RESTRICTED_KEYWORDS]

BYTES_PLACEHOLDER = "\"BYTES\""
LEVEL1_EXPECTED_OUTPUT = "Hello World"
RESTRICTED_DEFAULT = ["import","=","def","exec","eval","compile","os","global","try","expect","finally","\\"]
def validate_operation(input:str) -> tuple[bool,str]:
    if input.startswith("[") and input.endswith("]"):
        return True,""
    if BYTES_PLACEHOLDER not in input:
        return False,"Input does not contain the placeholder"
    if input.count(BYTES_PLACEHOLDER) > 1:
        return False,"Input contains more than one placeholder"
    return False,'Input is not an array'
    
def validate_allowed_keywords(input:str,restricted_expressions:List[str]=RESTRICTED_DEFAULT) -> tuple[bool,str]:
        for i in restricted_expressions:
            if i in input:
                return False,f'Keyword {i} not allowed in operation'
        return True,""

def validate_restricted_bytes(input:bytes,restricted_bytes:List[bytes]) -> tuple[bool,str]:
    invalid_found = []
    for i in restricted_bytes:
        if i in input:
            invalid_found.append("\\x{:02x}".format(int(i.hex(),16)))
    if invalid_found:    
        return False,f'Bytes {",".join(invalid_found)} are restricted'
    return True,""

def validate_input(operation:str,shellcode_bytes:str,restricted_expressions:List[str]=RESTRICTED_DEFAULT,restricted_bytes:List[bytes]=[],max_length:int=300) -> tuple[bool,str]:
    v,s = validate_operation(operation)
    if not v: return (v,s)
    sb = [x for x in filter(lambda c: c != '',shellcode_bytes.strip().split("\\x"))]  
    if len(sb) > max_length:
        return False,f"Input is too long. Max length is {str(max_length)} bytes"
    v,s = validate_allowed_keywords(operation,restricted_expressions)
    if not v: return (v,s)
    return validate_restricted_bytes(bytes([int(x,16) for x in sb]),restricted_bytes)

def execute_shellcode(shellcode:bytes) -> tuple[str,str]:
    proc = pwnlib.tubes.process.process("./exec_shellcode",stdin=PIPE,stdout=PIPE,stderr=PIPE)
    proc.sendline(str(len(shellcode)))
    out,err = proc.communicate(shellcode)
    return err.decode(),out.decode()
    
def validate_shellcode_output(out:str) -> tuple[bool,str]:
    if "error" in out:
        return False,out["error"]
    out = out["res"]
    if out.strip() == LEVEL1_EXPECTED_OUTPUT:
        return True,""
    return False,f"Expected output was not printed. Output: {out}"