import numpy as np
import pandas as pd

DATA_FILE = "./data/scatter-data.csv"


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


print(compute_biggest_gap_coordinates())
