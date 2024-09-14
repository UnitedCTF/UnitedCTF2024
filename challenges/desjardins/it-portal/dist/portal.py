#!/usr/bin/env python3

import sys
import time
import base64
import pickle
import socket
import sqlite3
import paramiko
import threading
from paramiko.common import (AUTH_SUCCESSFUL, AUTH_FAILED,
                             OPEN_SUCCEEDED, OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED)

# ANSI
BACKSPACE=b"\x1b[1D"
CLEAR=b"\x1b[H\x1b[2J"

FLAG = b"REDACTED"
DB = "db/portal.db"
HOST_KEY = "keys/portal.key"
MENU = b"""\r\n\
-----------------------\r
|| IT SUPPORT PORTAL ||\r
-----------------------\r
|  1 - Create Ticket  |\r
|  2 - Check Ticket   |\r
|  x - Exit           |\r
-----------------------\r
\r> \
"""

class Ticket():
    STATUS = ['open', 'in progress', 'closed']
    def __init__(self, subject, desc):
        self.subject = subject
        self.desc = desc
        self.status = 'open'


class ITPortal(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return OPEN_SUCCEEDED
        return OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username: str, password: str) -> int:
        con = sqlite3.connect(DB)
        c = con.cursor()

        user = c.execute(
            f'SELECT user_id from users where username LIKE "{username}"'
        ).fetchone()
        if user is None:
            return AUTH_FAILED

        auth = c.execute(
            f'SELECT user_id from users where username == "{username}" and password == "{password}"'
        ).fetchone()
        if auth is not None:
            return AUTH_SUCCESSFUL
        return AUTH_FAILED

    def check_channel_exec_request(self, channel: paramiko.Channel, command: bytes) -> bool:
        return True

    def check_auth_none(self, username: str) -> int:
        return AUTH_FAILED

    def get_allowed_auths(self, username: str) -> str:
        return "password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(
        self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True


def readline(chan: paramiko.Channel) -> bytes:
    data = b""
    while True:
        b = chan.recv(1)
        if b == b"\x7f":
            chan.send(BACKSPACE)
            chan.send(b" ")
            chan.send(BACKSPACE)
            data = data[:len(data)-1]
            continue
        chan.send(b)
        data += b
        if b == b"\n" or b == b"\r":
            break
    return data


def handle(client: socket.socket, server: ITPortal):
    t = paramiko.Transport(client)
    host_key = paramiko.RSAKey(filename=HOST_KEY)
    t.add_server_key(host_key)
    t.start_server(server=server)

    chan = t.accept(20)
    if chan is None:
        print("[!] No channel started, exiting.")
        sys.exit(1)

    while True:
        chan.send(CLEAR) # clear terminal
        chan.send(b"[ " + FLAG + b" ]")
        chan.send(MENU)
        choice = readline(chan).strip(b"\r\n")
        if choice not in [b'1',b'2',b'x']:
            chan.send(b"[!] Bad option.\r\n")
            time.sleep(2)
            continue

        elif choice == b'1':
            chan.send(b"Which project is it related to ? \r\n> ")
            project = readline(chan).decode().strip("\r\n")
            if project == "":
                chan.send(b"[!] Project cannot be empty.\r\n")
                time.sleep(2)
                continue

            chan.send(b"What is the subject ? \r\n> ")
            subject = readline(chan).decode().strip("\r\n")
            if subject == "":
                chan.send(b"[!] Subject cannot be empty.\r\n")
                time.sleep(2)
                continue

            chan.send(b"Please provide a short description of the issue\r\n> ")
            desc = readline(chan).decode().strip("\r\n")
            if desc == "":
                chan.send(b"[!] Desc cannot be empty.\r\n")
                time.sleep(2)
                continue

            create_ticket(project, subject, desc)

        elif choice == b'2':

            chan.send(b"Which project is it related to ? \r\n> ")
            project = readline(chan).decode().strip("\r\n")
            if project == "":
                chan.send(b"[!] Project cannot be empty.\r\n")
                time.sleep(2)
                continue

            ticket = check_tickets(project)
            if ticket is None:
                chan.send(b"[!] Ticket does not exist.\r\n")
                time.sleep(2)
                continue

            chan.send(b"TICKETS\r\n")
            chan.send(b"--------------------\r\n")
            chan.send(ticket.encode())
            chan.send(b"--------------------\r\n")
            chan.send(b"Press any key to go back to menu.\r\n")
            chan.recv(1)

        elif choice == b'x':
            print("[!] Exiting.\r\n")
            break

    chan.close()
    client.close()


def create_ticket(project: str, subject: str, desc: str):
    con = sqlite3.connect(DB)
    c = con.cursor()
    try: 
        t = Ticket(subject, desc)
        t_blob = base64.b64encode(pickle.dumps(t)).decode()
        c.execute(f'INSERT INTO tickets (project, ticket) VALUES ("{project}", "{t_blob}")')
        con.commit()
    finally:
        c.close()
        con.close()


def check_tickets(project: str) -> str|None:
    con = sqlite3.connect(DB)
    c = con.cursor()
    body = ""
    try: 
        tickets  = c.execute("SELECT ticket from tickets where project = (?)", 
                           (project,)).fetchall()
        if len(tickets) == 0:
            return None
        for ticket in tickets:
            if ticket is None:
                continue
            t =  pickle.loads(base64.b64decode(ticket[0]))
            line = f"|   {t.subject} :: {t.status}\r\n"
            body += line
        return body
    except Exception as e:
        print("[!] Err: ", e)
    finally:
        c.close()
        con.close()


def start_server(address: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try: 
        s.bind((address, port))
        portal = ITPortal()

        s.listen(100)

        while True:
            client, addr = s.accept()
            print('[?] Incoming connection from: ', addr)
            t = threading.Thread(target=handle, args=[client, portal])
            t.start()
    finally:
        s.close()


if __name__ == "__main__":
    print('[*] - IT Portal -')
    print('[?] Serving on 0.0.0.0:2020')
    start_server("0.0.0.0", 2020)

