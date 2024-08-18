import argparse
import pickle
import re

import pandas as pd
from pwn import log, remote
from sklearn.preprocessing import PolynomialFeatures

args = argparse.ArgumentParser()
args.add_argument(
    "--brute-force",
    action=argparse.BooleanOptionalAction,
    help="Use the brute-force brute force method or the linear regression model.",
    default=True,
)

args = args.parse_args()

MODEL_FILE = "own_model.pkl"

with open(MODEL_FILE, "rb") as f:
    ai_model = pickle.load(f)
    poly_features = PolynomialFeatures(degree=3)


def get_answer_from_linear_regression(x: int) -> str:
    """Get the answer from the linear regression model."""
    return str(int(ai_model.predict(poly_features.fit_transform([[x]]))[0]))


def get_prediction(x: int) -> str:
    """Get the prediction for the given x."""

    if args.brute_force:
        return get_dummy_brute_force_answer(x)
    return get_answer_from_linear_regression(x)


DATA_FILE = "../data/scatter-data.csv"

# Importing the dataset
dataset = pd.read_csv(DATA_FILE)


def get_dummy_brute_force_answer(x: int) -> str:
    """Get the dummy brute force answer."""

    # Get X and Y columns
    x_values = dataset.iloc[:, 0].values
    y_values = dataset.iloc[:, 1].values

    # Find the value of y for the given x. The value is not in x_values, find the closest value
    closest_x = min(x_values, key=lambda x_val: abs(x_val - x))
    closest_y = y_values[list(x_values).index(closest_x)]

    official_y = get_answer_from_linear_regression(x)
    log.info(
        f"x: {x}, closest_x: {closest_x}, closest_y: {closest_y}, official_y: {official_y}"
    )

    return str(closest_y)


max_loop = 100
r = remote("localhost", ssl=False, port=10000)
for i in range(max_loop):
    data = r.recvuntil(f"/{max_loop}")
    log.info(data.decode())
    line = r.recvuntil(b"what would you predict the output to be?")
    log.info(line.decode())

    # Extract the given x value
    given_x = re.findall("[0-9]+", str(line))[0]
    log.info(f"Given_x {given_x}")

    # Send the guessed y value
    guessed_y = get_prediction(int(given_x))
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
