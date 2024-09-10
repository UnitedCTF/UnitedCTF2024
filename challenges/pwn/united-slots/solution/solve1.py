import socket

# Define the server address and port
server_address = ('localhost', 12366)  # Replace with your server's address and port

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    sock.connect(server_address)
    
    # Prepare the message
    message = "abcdefghijy" + "\n"
    
    # Send the message
    sock.sendall(message.encode())

    try:
        response = sock.recv(4096)  # Increase buffer size
        print("Received:", response.decode())
    except socket.timeout:
        print("No response received within the timeout period.")



    
    try:
        response = sock.recv(4096)  # Increase buffer size
        print("Received:", response.decode())
    except socket.timeout:
        print("No response received within the timeout period.")

finally:
    # Close the socket
    sock.close()
