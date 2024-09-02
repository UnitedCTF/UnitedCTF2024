from pwn import *
from itertools import chain

remote = remote("127.0.0.1", 1337)

zeros = [0]*15
known_blocks = chain.from_iterable([i]+zeros for i in range(256))
remote.sendline((bytes(zeros) + bytes(known_blocks)).hex().encode())

message = bytes.fromhex(remote.readline().decode())
blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]

solutions = {blocks[i+1]:i for i in range(256)}
solved = bytes([solutions[block] for block in blocks[:-256:257]])

remote.sendline(solved.hex().encode())
print(remote.recv().decode())

remote.close()
