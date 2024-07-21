from pwn import *

remote = remote("127.0.0.1", 1337)

remote.sendline(b"00"*15)
message = bytes.fromhex(remote.readline().decode())

blocks = [message[i:i+16] for i in range(0, len(message)-16, 16)]

missing = set(blocks)
solutions = dict()

zeros = [0]*15
for i in range(127,0,-1):
	joiner = bytes(zeros+[i]+zeros)
	remote.sendline(joiner.hex().encode())
	response = bytes.fromhex(remote.readline().decode())
	chrblock = response[16:32]

	if chrblock in missing:
		missing.remove(chrblock)
		solutions[chrblock] = chr(i)
		print(f"Found {chrblock} -> {chr(i)}")
		if len(missing) == 0:
			break

print("".join([solutions[block] for block in blocks]))

remote.close()
