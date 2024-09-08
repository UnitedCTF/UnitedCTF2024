from pwn import *

r = remote('localhost', port=10000)

CATEGORIES = [
    set("😢🥲😥😭😰😵🤕🤬😡🤢😫🤮💀"),
    set("😀😁🤣😄😎😆😋😍🤗😏😜😌🤪"),
    set("🥸🤡👽👻📎👺🤖🙊🦐🦭🦔💅🗿")
]

for _ in range(10):
    parks = []

    r.recvuntil(b'es.\n\n')
    for _ in range(100):
        emotions = set(r.recvline().decode().strip()[4:].replace(' ', ''))
        parks.append(emotions)

    flag_park = [i+1 for i, park in enumerate(parks) if all([cat & park for cat in CATEGORIES])]

    r.recvuntil(b'> ')
    r.sendline(str(flag_park[0]).encode())

r.interactive()