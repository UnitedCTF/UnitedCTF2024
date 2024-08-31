# Script use to create a Polynomial regression on the dataset

import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Importing the dataset
dataset = pd.read_csv("./data/scatter-data.csv")

# Splitting the dataset into X and y
X = dataset.iloc[:, 0].values.reshape(-1, 1)
y = dataset.iloc[:, 1].values

plt.scatter(X, y, color="blue", label="Data")

colors = [
    "red",
    "green",
    "purple",
    "orange",
    "black",
    "yellow",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
]

min_mse = -1
min_degree = 0
X_max = int(np.max(X))
Y_max = int(np.max(y))
plt.axis([0, X_max, 0, Y_max])
for degree in range(1, 4):
    # Create polynomial features
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X.reshape(-1, 1))

    # Fit the polynomial features to the linear regression model
    poly_reg = LinearRegression()
    poly_reg.fit(X_poly, y)

    y_pred = poly_reg.predict(X_poly)

    # Evaluate the model
    mse = mean_squared_error(y, y_pred)
    if mse < min_mse or min_mse == -1:
        min_mse = mse
        min_degree = degree
        # save that regression model to a file
        with open("model.pkl", "wb") as f:
            pickle.dump(poly_reg, f)

    print("Mean Squared Error:", mse)

    # Visualize the polynomial regression curve
    plt.plot(
        X,
        poly_reg.predict(X_poly),
        color=colors[degree],
        label=f"Degree {degree} Polynomial Regression",
    )

plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Degree {degree} Polynomial Regression")
plt.legend()
plt.savefig("polynomial-regression.png")
# plt.show()
print(
    f"Minimum Mean Squared Error: {min_mse} for Degree {min_degree} Polynomial Regression"
)

# Get the min and max value of X
X_min = int(np.min(X))
X_max = int(np.max(X))

plt.clf()
plt.cla()
plt.axis([0, X_max, 0, Y_max])
import random

for i in range(250):
    random_value = random.randrange(X_min, X_max)
    X_new = np.array([[random_value]])
    X_new_poly = poly_features.transform(X_new)
    y_new = poly_reg.predict(X_new_poly)
    # randomize the value by adding some noise
    y_new = y_new + random.uniform(-25, 25)
    plt.scatter(X_new, y_new, color="red")

plt.savefig("polynomial-regression-predictions.png")
plt.show()
