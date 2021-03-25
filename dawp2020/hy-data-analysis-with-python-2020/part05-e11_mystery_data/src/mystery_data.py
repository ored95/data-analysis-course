#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    model = LinearRegression(fit_intercept=False)
    X = df[df.columns[:-1]]
    Y = df[df.columns[-1]]
    model.fit(X, Y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(5):
        print('Coefficient of X{} is {}'.format(i+1, coefficients[i]))

if __name__ == "__main__":
    main()
