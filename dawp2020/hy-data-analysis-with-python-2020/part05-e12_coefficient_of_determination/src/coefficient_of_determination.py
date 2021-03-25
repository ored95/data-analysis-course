#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pandas.core.algorithms import mode
from sklearn import linear_model

def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    model = linear_model.LinearRegression(fit_intercept=True)
    X = df[df.columns[:-1]]
    Y = df[df.columns[-1]]
    scores = []
    model.fit(X, Y)
    scores.append(model.score(X, Y))
    for x in df.columns[:-1]:
        X = df[x].to_numpy()
        model.fit(X[:, np.newaxis], Y)
        scores.append(model.score(X[:, np.newaxis], Y))
    return scores
    
def main():
    scores = coefficient_of_determination()
    print('R2-score with feature(s) X: ', scores[0])
    for i, s in enumerate(scores):
        print('R2-score with feature(s) X{}: {:.4f}'.format(i, s))

if __name__ == "__main__":
    main()