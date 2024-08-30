from pyseccomp import SyscallFilter, ALLOW, Arg, EQ, ERRNO, errno
from subprocess import Popen, PIPE
from re import findall
from sys import stdout, stderr, stdin


def drop_perms():
    filter = SyscallFilter(ERRNO(errno.EPERM))

    filter.add_rule(ALLOW, "write", Arg(0, EQ, stdout.fileno()))
    filter.add_rule(ALLOW, "write", Arg(0, EQ, stderr.fileno()))

    filter.add_rule(ALLOW, "exit")
    filter.add_rule(ALLOW, "read", Arg(0, EQ, stdin.fileno()))
    filter.load()


def execute_input(input: str) -> tuple[bool, bytes]:
    out, err = Popen(
        ["python3", "run_exec.py"],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    ).communicate(input.encode())
    if err:
        return False, err
    out = out.replace(b"\n", b"").replace(b"b'", b"").replace(b"'", b"")
    for i in findall(r"\\x[0-9a-fA-F]{2}", out.decode()):
        out = out.replace(
            bytes(i, encoding="utf-8"), bytes([int(i.replace("\\x", ""), 16)])
        )
    return True, out
