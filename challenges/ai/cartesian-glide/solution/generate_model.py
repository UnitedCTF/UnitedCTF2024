import pickle
import re

from pwn import log, remote
from sklearn.preprocessing import PolynomialFeatures

DATA_FILE = "extracted_data_from_challenge.csv"
MODEL_FILE = "own_model.pkl"

log.info("Let's collect data")

with open(DATA_FILE, "a") as f:

    for i in range(1):
        r = remote("localhost", ssl=False, port=10000)

        data = r.recvuntil(
            b"""Don't blame me if your coaster ends up being a straight line. Your call.\n\n"""
        )
        log.info(data)
        line = r.recv()
        print(line)

        # Extract the given x value
        given_x = re.findall("[0-9]+", str(line))[0]
        print(given_x)
        r.sendline(b"12")

        data = r.recvuntil("I'm starting to regret giving you this easy job.")
        print(data)
        expected_output = re.findall("[0-9]+", str(data))
        print(expected_output[0])
        r.close()

        f.write(f"{given_x},{expected_output[0]}\n")

# Create a Polynomial regression on the dataset
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Importing the dataset
dataset = pd.read_csv(DATA_FILE)

# Splitting the dataset into X and y
X = dataset.iloc[:, 0].values.reshape(-1, 1)
y = dataset.iloc[:, 1].values

# Plot the data
plt.scatter(X, y, color="blue", label="Data")
X_max = int(np.max(X))
Y_max = int(np.max(y))
plt.axis([0, X_max, 0, Y_max])

# Create polynomial features
poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X.reshape(-1, 1))

# Fit the polynomial features to the linear regression model
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

y_pred = poly_reg.predict(X_poly)

# Evaluate the model
mse = mean_squared_error(y, y_pred)

# save that regression model to a file
with open(MODEL_FILE, "wb") as f:
    pickle.dump(poly_reg, f)

print("Mean Squared Error:", mse)
plt.savefig("extracted_data_plot.png")
