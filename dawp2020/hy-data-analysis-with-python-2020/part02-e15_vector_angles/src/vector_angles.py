#!/usr/bin/env python3

import numpy as np
from numpy.core.defchararray import array
import scipy.linalg

def vector_angles(X, Y):
    vxy = np.dot(X, Y.T).diagonal()
    X, Y = np.square(X), np.square(Y)
    vx, vy = np.sqrt(X.sum(axis=1)), np.sqrt(Y.sum(axis=1))
    cos_angles = np.clip(vxy / vx / vy, -1.0, 1.0)
    return np.arccos(cos_angles) * 180. / np.pi

def main():
    print(vector_angles(
        np.array([
            [1, 2, 3],
            [4, 5, 6]
        ]),
        np.array([
            [-1, 2, 3],
            [4, -5, 6]
        ])
    ))

if __name__ == "__main__":
    main()
