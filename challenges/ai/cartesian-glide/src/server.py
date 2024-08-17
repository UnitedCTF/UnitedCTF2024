import os
import pickle
import random
import re
import time

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

from template import (
    BAD_ANSWER_MESSAGE,
    CORRECT_ANSWER_MESSAGE,
    FIRST_CORRECT_ANSWER_MESSAGE,
    GAME_INTRODUCTION,
    INVALID_INPUT_MESSAGE,
    SECOND_CORRECT_ANSWER_MESSAGE,
    TIMEOUT_MESSAGE,
)

REGEX_VALIDATION = "[0-9]+"
TIMEOUT = 1

# Importing the dataset
dataset = pd.read_csv("./data/scatter-data.csv")

# Splitting the dataset into X and y
X = dataset.iloc[:, 0].values.reshape(-1, 1)
y = dataset.iloc[:, 1].values

# Get the min and max value of X
x_min = int(np.min(X))
x_max = int(np.max(X))

poly_features = PolynomialFeatures(degree=3)


with open("model.pkl", "rb") as f:
    ai_model = pickle.load(f)


def parse_numbers(input_value: str) -> int:
    """Parse a string to only accept numbers."""
    if not re.match(REGEX_VALIDATION, input_value):
        return None
    return int(input_value)


def generate_random_number() -> int:
    """Generate a random number between min and max."""
    return np.random.choice(X.flatten())


def validate_prediction(user_prediction: int, target: int) -> bool:
    """Validate that the user's prediction is within a 5% error margin of the target."""

    return abs(user_prediction - target) <= 0.05 * target


# Start the game
print(GAME_INTRODUCTION)

for i in range(10):
    print(f"Round {i + 1}/10")
    # Generate a random number
    random_number = generate_random_number()

    # Ask the user for their prediction
    time_before, response = time.time(), parse_numbers(
        input(
            f"If I give you {random_number}, what would you predict the output to be? "
        )
    )

    # Check if the user's response is within the time limit
    if time.time() - time_before >= TIMEOUT:
        print(TIMEOUT_MESSAGE)
        exit()

    # Check if the user provided a valid response
    if response is None:
        print(INVALID_INPUT_MESSAGE)
        exit()

    prediction = int(
        ai_model.predict(poly_features.fit_transform([[random_number]]))[0]
    )

    if validate_prediction(response, prediction):
        if i == 0:
            print(FIRST_CORRECT_ANSWER_MESSAGE.format(flag=os.getenv("FLAG1")))
        elif i == 9:
            print(SECOND_CORRECT_ANSWER_MESSAGE.format(flag=os.getenv("FLAG2")))
        else:
            print(CORRECT_ANSWER_MESSAGE)
    else:
        # Randomly modify the prediction by plus or minus 5%
        modified_prediction = int(random.uniform(prediction * 0.95, prediction * 1.05))
        print(BAD_ANSWER_MESSAGE.format(answer=modified_prediction))
        exit()
