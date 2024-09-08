from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from itertools import chain

KEY = get_random_bytes(16)
MESSAGE = get_random_bytes(64)
FLAG = "?"

try:
    cipher = AES.new(KEY, AES.MODE_ECB)

    joiner = bytes.fromhex(input())
    joined = joiner.join(bytes([byte]) for byte in MESSAGE) + joiner
    padded = pad(joined, 16)
    print(cipher.encrypt(padded).hex())

    guess = bytes.fromhex(input())
    if guess == MESSAGE:
        print(FLAG)
    else:
        print("no")
except:
    print("what")
