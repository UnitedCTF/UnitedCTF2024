import os
import pickle
import random
import re
import time

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

from template import (
    BAD_ANSWER_MESSAGE_WITH_CLUE,
    BAD_ANSWER_MESSAGE_WITHOUT_CLUE,
    CORRECT_ANSWER_MESSAGE,
    FIRST_CORRECT_ANSWER_MESSAGE,
    GAME_INTRODUCTION,
    INVALID_INPUT_MESSAGE,
    SECOND_CORRECT_ANSWER_MESSAGE,
    TIMEOUT_MESSAGE,
)

REGEX_VALIDATION = "[0-9]+"
DATA_FILE = "./data/scatter-data.csv"
TIMEOUT = 1
EASY_ROUND_COUNT = 5


def parse_numbers(input_value: str) -> int:
    """Parse a string to only accept numbers."""

    if not re.match(REGEX_VALIDATION, input_value):
        return None
    return int(input_value)


def compute_biggest_gap_coordinates() -> tuple[int, int]:
    # Importing the dataset
    dataset = pd.read_csv(DATA_FILE)

    # Find the biggest gap in the X axis
    x_values = dataset.iloc[:, 0].values
    sorted_x_values = np.sort(x_values)
    biggest_gap = np.max(np.diff(sorted_x_values))

    # Find the indices of the biggest gap in the X axis
    biggest_gap_indices = np.where(np.diff(sorted_x_values) == biggest_gap)[0]

    # Get the x coordinates of the biggest gap
    gap_start = sorted_x_values[biggest_gap_indices]

    # Get the end of the gap
    gap_end = gap_start[-1] + biggest_gap

    return int(gap_start), int(gap_end)


def generate_random_number(round_number: int) -> int:
    """Generate a random number based on the round."""

    if round_number >= EASY_ROUND_COUNT:
        return np.random.randint(gap_start, gap_end)
    return np.random.choice(X.flatten())


def get_bad_answer_message(prediction: int, round_number: int) -> str:
    """Generate a bad answer message for the user."""

    if round_number >= EASY_ROUND_COUNT:
        return BAD_ANSWER_MESSAGE_WITHOUT_CLUE
    return BAD_ANSWER_MESSAGE_WITH_CLUE.format(answer=prediction)


def validate_prediction(user_prediction: int, target: int) -> bool:
    """Validate that the user's prediction is within a 5% error margin of the target."""

    return abs(user_prediction - target) <= 0.05 * target


# Importing the dataset
dataset = pd.read_csv(DATA_FILE)

# Splitting the dataset into X and y
X = dataset.iloc[:, 0].values.reshape(-1, 1)
y = dataset.iloc[:, 1].values

# Get the min and max value of X
x_min = int(np.min(X))
x_max = int(np.max(X))

# Polynomial features
poly_features = PolynomialFeatures(degree=3)


with open("model.pkl", "rb") as f:
    ai_model = pickle.load(f)

gap_start, gap_end = compute_biggest_gap_coordinates()

# Start the game
print(GAME_INTRODUCTION)
number_of_rounds = 100

for i in range(number_of_rounds):
    round_number = i + 1
    print(f"Round {round_number}/{number_of_rounds}")
    # Generate a random number
    random_number = generate_random_number(round_number)

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
        elif i == number_of_rounds - 1:
            print(SECOND_CORRECT_ANSWER_MESSAGE.format(flag=os.getenv("FLAG2")))
        else:
            print(CORRECT_ANSWER_MESSAGE)
    else:

        # Randomly modify the prediction by plus or minus 5%
        modified_prediction = int(random.uniform(prediction * 0.95, prediction * 1.05))

        print(get_bad_answer_message(modified_prediction, round_number))
        exit()
