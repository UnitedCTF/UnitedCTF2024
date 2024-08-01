from functools import wraps
from typing import Dict, List
from flask import Flask, render_template, session
import uuid
import time
import random


SPIN_INTERVAL: int = 7 * 24 * 60 * 60
PRIZE_VALUES: List[int] = [0, 5, 0, 10, 0, 7, 0, 0, 2, 0, -30, 0]
FLAG_PRICE: int = 1000


app = Flask(__name__)
app.secret_key = '255da035eddf51f1ecd98487f620a9ff'

database: Dict[str, int] = {}


def create_session():
    uid = uuid.uuid4()
    session['uid'] = uid
    session['last_spin'] = 0
    database[uid] = 0


def session_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('uid') is None:
            create_session()
        return f(*args, **kwargs)
    return decorated_function


@app.get('/')
@session_required
def roulette_view():
    uid = session['uid']   
    can_spin = time.time() - session['last_spin'] >= SPIN_INTERVAL
    balance = database[uid]
    return render_template('wheel.html', can_spin=can_spin, balance=balance)


@app.post('/spin')
@session_required
def roulette_spin():
    if time.time() - session['last_spin'] < SPIN_INTERVAL:
        return {'error': 'spin_already_used'}, 400

    uid = session['uid']    
    wheel_choice = random.randrange(0, len(PRIZE_VALUES))

    balance = database[uid]
    balance += PRIZE_VALUES[wheel_choice]
    database[uid] = balance

    session['last_spin'] = time.time()

    return {'wheel_choice': wheel_choice, 'new_balance': database[uid]}


@app.get('/redeem')
@session_required
def redeem_flag():
    uid = session['uid']
    balance = database[uid]

    flag = balance >= 1000
    return render_template('redeem.html', flag=flag)
