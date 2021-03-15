#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    sepal_length, petal_length = load().T[[0,2]]
    # Hint: Compute this using the scipy.stats.pearsonr function. 
    #       It returns a tuple whose first element is the correlation.
    return scipy.stats.pearsonr(sepal_length, petal_length)[0]

def correlations():
    return np.corrcoef(load().T[[0,1,2,3]])

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
