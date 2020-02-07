# AUTOGENERATED! DO NOT EDIT! File to edit: 01_linear_regression.ipynb (unless otherwise specified).

__all__ = ['generate_data', 'gradient_descent']

# Cell
import numpy as np
import pandas as pd
import altair as altair
def generate_data():
    """It generates dummy data."""
    noise = np.random.randn(100,1)
    X = 2 * np.random.rand(100,1)
    y = 5 + 3 * X + noise
    return X,y

# Cell
def gradient_descent(data,w_0_t,w_1_t,learning_rate,num_iterations):
    """Gradient descent implementation, which gets `data`, starting `w_0` and `w_1`, `learning_rate`
    and the number of iterations `num_iterations`"""

    w_0 = 0
    w_1 = 0
    (X,y) = data
    N = len(X)
    w_0_t = 0
    w_1_t = 0
    for t in range(0,num_iterations):
        w_0_deriv = np.zeros((N,N))
        w_1_deriv = np.zeros((N,N))
        w_0_deriv = -2 * (y - (w_0_t + w_1_t * X))
        w_1_deriv = -2 * np.dot(X.T, (y - (w_0_t + w_1_t * X)))
        w0_sum = np.sum(w_0_deriv,axis=0)
        w1_sum = np.sum(w_1_deriv,axis=0)
        w_0 = w_0 - learning_rate * (w0_sum / N)
        w_1 = w_1 - learning_rate * (w1_sum / N)
        w_0_t = w_0
        w_1_t = w_1
    return w_0, w_1