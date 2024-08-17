import pickle
import re

from pwn import log, remote
from sklearn.preprocessing import PolynomialFeatures

MODEL_FILE = "own_model.pkl"

with open(MODEL_FILE, "rb") as f:
    ai_model = pickle.load(f)
    poly_features = PolynomialFeatures(degree=3)


def get_answer_from_linear_regression(x: int) -> str:
    """Get the answer from the linear regression model."""
    return str(int(ai_model.predict(poly_features.fit_transform([[x]]))[0]))


max_loop = 10
r = remote("localhost", ssl=False, port=10000)
for i in range(max_loop):
    data = r.recvuntil("/10")
    log.info(data.decode())
    line = r.recvuntil(b"what would you predict the output to be?")
    log.info(line.decode())

    # Extract the given x value
    given_x = re.findall("[0-9]+", str(line))[0]
    log.info(f"Given_x {given_x}")

    # Send the guessed y value
    guessed_y = get_answer_from_linear_regression(int(given_x))
    log.info(f"Guessed y: {guessed_y}")
    r.sendline(guessed_y.encode())

    # Get the response
    r.recvline()
    data = r.recvline()
    log.info("Here is the data")
    log.info(data.decode())
    if b"flag-" in data:
        flag = re.findall("flag-[a-zA-Z0-9_]+", data.decode())[0]
        log.info(f"Found the flag {flag}")
