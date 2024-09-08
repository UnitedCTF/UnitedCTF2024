import signal as os_signal
import random as rand

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


def chal():
    operations = ['+', '-', '*', '/']
    count = 0
    while count < 100:
        n1 = rand.randint(1, 1000)
        n2 = rand.randint(1, 1000)
        op = rand.choice(operations)
        res = compute_operation(op, n1, n2)

        print(f'{n1} {op} {n2} = ?')
        
        try :
            n_in = int(input())
            if n_in == res:
                count += 1
            else:
                count = 0
                print('Incorrect!')
        except ValueError:
            print('Invalid input')
            continue

    print('flag-Th1s1sAR3w4rdF0rY0urGr34tW0rk')


def timeout(signum, frame):
    print("Connection timed out. It took too long to calculate.")
    exit(0)


if __name__ == '__main__':
    os_signal.signal(os_signal.SIGALRM, timeout)
    os_signal.alarm(2)
    chal()