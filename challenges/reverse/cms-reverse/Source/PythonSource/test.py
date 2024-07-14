# send bytes to tcp server

import socket
import time
import datetime
def send_bytes():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 11954)
    sock.connect(server_address)
    try:
        # Send data
        message = b'\x0C' + (time.time_ns()).to_bytes(8, byteorder='big') + b"cce13886a4e64875800f6ee80d5a7dfa" + int(3708838547).to_bytes(4, byteorder='big')
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

send_bytes()