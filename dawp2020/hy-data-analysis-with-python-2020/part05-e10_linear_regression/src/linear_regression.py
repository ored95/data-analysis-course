#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    np.random.seed(0)
    x1 = np.linspace(1, 10, 10)
    y1 = x1 * 2 - 1 + 9 * np.random.rand()
    s1, i1 = fit_line(x1, y1)
    print('Slope: {}\nIntercept: {}\n'.format(s1, i1))
    plt.plot(x1, y1, 'o')
    x = np.linspace(1, 10, 30)
    y = s1 * x + i1
    plt.plot(x, y, '-')
    plt.show()
    
if __name__ == "__main__":
    main()
