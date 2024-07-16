# send bytes to tcp server
import requests
import socket
import time
import datetime
import base64
def send_bytes():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 11954)
    sock.connect(server_address)
    try:
        # Send data
        message = b'\x01' + (time.time_ns()).to_bytes(8, byteorder='big') + b"cce13886a4e64875800f6ee80d5a7dfa" + int(3708838547).to_bytes(4, byteorder='big')
        print('sending {!r}'.format(message))
        sock.sendall(message)
        # Look for the response 
        while True:
            data = sock.recv(136)

            if data:
                print('received {!r}'.format(data))
                break
            print('received {!r}'.format(data))
    finally:
        print('closing socket')
        sock.close()
def send_bytes2():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 11954)
    sock.connect(server_address)
    try:
        # Send data
        h = requests.get("http://localhost:9860/a5276b40-5acf-44a8-b0d0-56819516145f").text.split('@')
        ts = int(h[1])
        h = h[0]

        t = ts.to_bytes(8, byteorder='big')
        h = bytes([ord(b) ^ t[i % len(t)] for i,b in enumerate(h)])
        s = bytes(base64.b64encode(h).decode() + '@' + str(ts),"utf-8").hex()
        message = b'\x0C' + ts.to_bytes(8, byteorder='big') + b"cce13886a4e64875800f6ee80d5a7dfa" + bytes(s,"utf-8")
        sock.sendall(message)
        while True:
            data = sock.recv(136)
            if data:
                print('received {!r}'.format(data))
                break
            print('received {!r}'.format(data))
    finally:
        print('closing socket')
        sock.close()
send_bytes2()