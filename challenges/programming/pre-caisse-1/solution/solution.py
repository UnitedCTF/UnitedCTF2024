import socket

def calculate(n1, op, n2):
    return {
        '+': n1 + n2,
        '-': n1 - n2,
        '*': n1 * n2,
        '/': n1 / n2
    }.get(op, None)


def parse_input(input_str):
    try:
        n1, op, n2, _, __ = input_str.split()
        n1 = int(n1)
        n2 = int(n2)
        return n1, op, n2
    except ValueError:
        return None, None, None


def receive_from_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((host, port))
    
    try:
        while True:
            data = client_socket.recv(1024) 
            if not data:
                continue
            data_str = data.decode()
            print(data_str)

            if 'flag' in data_str:
                break

            n1, op, n2 = parse_input(data_str)
            res = calculate(n1, op, n2)
            if res is not None:
                print(f'{int(res)}\n')
                client_socket.sendall(f'{int(res)}\n'.encode())

    except KeyboardInterrupt:
        print("Connection closed")
    
    client_socket.close()
    print("Connection closed")


receive_from_server('127.0.0.1', 8080)  
