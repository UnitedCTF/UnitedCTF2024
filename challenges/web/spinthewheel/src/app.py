from functools import wraps
from typing import Dict, List
from flask import Flask, render_template, session
import uuid
import random


PRIZE_VALUES: List[int] = [-1, 5, 0, 10, -1, 20, 0, 0, 2, -1, 3, 0]
FLAG_PRICE: int = 10000


app = Flask(__name__)
app.secret_key = '255da035eddf51f1ecd98487f620a9ff'


def create_session():
    uid = uuid.uuid4()
    session['uid'] = uid
    session['balance'] = 0


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
    return render_template('wheel.html', balance=session['balance'])


@app.post('/spin')
@session_required
def roulette_spin(): 
    wheel_choice = random.randrange(0, len(PRIZE_VALUES))

    if PRIZE_VALUES[wheel_choice] == -1:
        session['balance'] = 0
    else:
        session['balance'] += PRIZE_VALUES[wheel_choice]

    return {'wheel_choice': wheel_choice, 'new_balance': session['balance']}


@app.get('/redeem')
@session_required
def redeem_flag():
    flag = session['balance'] >= FLAG_PRICE
    return render_template('redeem.html', flag=flag)
