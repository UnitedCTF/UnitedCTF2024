import socket


str_operations = { 'plus' : '+',
                'minus' : '-',
                'times' : '*',
                'divided' : '/'}

str_num = { 'zero' : 0,
            'one' : 1,
            'two' : 2,
            'three' : 3,
            'four' : 4,
            'five' : 5,
            'six' : 6,
            'seven' : 7,
            'eight' : 8,
            'nine' : 9,
            'ten' : 10,
            'eleven' : 11,
            'twelve' : 12,
            'thirteen' : 13,
            'fourteen' : 14,
            'fifteen' : 15,
            'sixteen' : 16,
            'seventeen' : 17,
            'eighteen' : 18,
            'nineteen' : 19,
            'twenty' : 20,
            'thirty' : 30,
            'forty' : 40,
            'fifty' : 50,
            'sixty' : 60,
            'seventy' : 70,
            'eighty' : 80,
            'ninety' : 90,
            'hundred' : 100 }


def calculate(n1, op, n2):
    return {
        '+': n1 + n2,
        '-': n1 - n2,
        '*': n1 * n2,
        '/': n1 / n2
    }.get(op, None)
    

def parse_str_to_number(s, is_hundred=False):
    return str_num.get(s, 0) * (100 if is_hundred else 1)


def parse_str_operation(str_op):
    elements = str_op.split()
    n1, n2 = 0, 0
    op = None
    is_n2_found = False
    is_hundred = False

    for el in reversed(elements[:-2]):
        if el == 'by':
            continue
        if el == 'hundred':
            is_hundred = True
            continue

        if el in str_operations:
            op = str_operations[el]
            is_n2_found = True
        else:
            if is_n2_found:
                n1 += parse_str_to_number(el, is_hundred)
            else:
                n2 += parse_str_to_number(el, is_hundred)
            is_hundred = False

    return n1, op, n2
    

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

            n1, op, n2 = parse_str_operation(data_str)
            res = calculate(n1, op, n2)
            if res is not None:
                print(f'{int(res)}\n')
                client_socket.sendall(f'{int(res)}\n'.encode())

    except KeyboardInterrupt:
        print("Connection closed")
    
    client_socket.close()
    print("Connection closed")


receive_from_server('127.0.0.1', 8080)  
