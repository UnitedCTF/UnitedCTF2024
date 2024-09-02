from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from itertools import chain

KEY = get_random_bytes(16)
FLAG = b"?"

cipher = AES.new(KEY, AES.MODE_ECB)

try:
    while True:
        joiner = bytes.fromhex(input())
        message = joiner.join(bytes([char]) for char in FLAG) + joiner
        padded = pad(message, 16)
        print(cipher.encrypt(padded).hex())
except:
    print("what")
