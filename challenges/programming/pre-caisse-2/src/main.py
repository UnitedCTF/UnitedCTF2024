import signal as os_signal
import random as rand

operations = ['+', '-', '*', '/']
str_operations = { '+' : 'plus', 
                '-' : 'minus',
                '*' : 'times',
                '/' : 'divided by'}
str_num = { 0 : 'zero',
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            10 : 'ten',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen',
            20 : 'twenty',
            30 : 'thirty',
            40 : 'forty',
            50 : 'fifty',
            60 : 'sixty',
            70 : 'seventy',
            80 : 'eighty',
            90 : 'ninety',
            100 : 'hundred'}


def compute_operation(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return int(n1 / n2)
    else:
        return None
    

def parse_number_to_string(n):
    if n < 20:
        return str_num[n]
    elif n < 100:
        n_mod = n % 10
        if n_mod == 0:
            return str_num[n]
        return str_num[n - n_mod] + ' ' + str_num[n_mod]
    elif n < 1000:
        res = str_num[n // 100] + ' ' + str_num[100]
        if n % 100 != 0:
            res += ' ' + parse_number_to_string(n % 100)
        return res


def chal():
    count = 0
    while count < 100:
        n1 = rand.randint(1, 999)
        n2 = rand.randint(1, 999)
        op = rand.choice(operations)
        res = compute_operation(op, n1, n2)

        n1_str = parse_number_to_string(n1)
        n2_str = parse_number_to_string(n2)
        op_str = str_operations[op]

        print(f'{n1_str} {op_str} {n2_str} = ?')
        
        try :
            n_in = int(input())
            if n_in == res:
                count += 1
            else:
                count = 0
                print(f'Incorrect! {res}')
        except ValueError:
            print('Invalid input')
            continue

    print('flag-4n0th3rR3w4rdY0uD1d1t0nc3Ag41n')


def timeout(signum, frame):
    print("Connection timed out. It took too long to calculate.")
    exit(0)


if __name__ == '__main__':
    os_signal.signal(os_signal.SIGALRM, timeout)
    os_signal.alarm(10)
    chal()