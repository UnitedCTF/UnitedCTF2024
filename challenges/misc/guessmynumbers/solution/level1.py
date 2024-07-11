from pwn import *

r = remote('guessmynumbers.c.unitedctf.ca', ssl=True, port=443)

def rotate_logical_right(val):
    b = val & 1
    return (val >> 1) | (b << 31)

# Level 1
log.info('Level 1')
r.recvuntil(b'Niveau 1: ')
sequence = eval(r.recvline())

start = sequence[0]
step = sequence[1] - start

new_sequence = [start + step * i for i in range(20)]

assert sequence == new_sequence[:10]
r.sendline(','.join([str(x) for x in new_sequence[10:]]).encode())

# Level 2
log.info('Level 2')
r.recvuntil(b'Niveau 2: ')
sequence = eval(r.recvline())

start = sequence[0]
step1 = sequence[1] - sequence[0]
step2 = sequence[1] - sequence[2]

new_sequence = [start]
for i in range(19):
    match i % 3:
        case 0:
            new_sequence.append(new_sequence[-1] + step1)
        case 1:
            new_sequence.append(new_sequence[-1] - step2)
        case 2:
            new_sequence.append(new_sequence[-1] * 10)

assert sequence == new_sequence[:10]
r.sendline(','.join([str(x) for x in new_sequence[10:]]).encode())

# Level 3
log.info('Level 3')
r.recvuntil(b'Niveau 3: ')
sequence = eval(r.recvline())

start = sequence[0]

new_sequence = [start]
for i in range(19):
    new_sequence.append(rotate_logical_right(new_sequence[-1]))

assert sequence == new_sequence[:10]
r.sendline(','.join([str(x) for x in new_sequence[10:]]).encode())

# Win
resp = r.recvall().decode()
print(resp)