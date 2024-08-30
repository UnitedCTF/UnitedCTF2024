import pyseccomp as seccomp
import subprocess
import re
import sys
def drop_perms():
    # respond with EPERM: operation not permitted so users can tell
    # they're being blocked from doing something
    filter = seccomp.SyscallFilter(seccomp.ERRNO(seccomp.errno.EPERM))

    # allow `write`ing to two already-opened files stdout and stderr
    filter.add_rule(
        seccomp.ALLOW, "write", seccomp.Arg(0, seccomp.EQ, sys.stdout.fileno())
    )
    filter.add_rule(
        seccomp.ALLOW, "write", seccomp.Arg(0, seccomp.EQ, sys.stderr.fileno())
    )

    filter.add_rule(seccomp.ALLOW, "exit")
    filter.add_rule(seccomp.ALLOW, "read", seccomp.Arg(0, seccomp.EQ, sys.stdin.fileno()))
    filter.load()

def execute_input(input:str)->bytes:
    out,err = subprocess.Popen(["python3","run_exec.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(input.encode())
    out = out.replace(b'\n',b'').replace(b'b\'',b'').replace(b'\'',b'')
    for i in re.findall(r'\\x[0-9a-fA-F]{2}',out.decode()):
        out = out.replace(bytes(i,encoding='utf-8'),bytes([int(i.replace("\\x",""),16)]))
    print(out)
    return out if not err else err
