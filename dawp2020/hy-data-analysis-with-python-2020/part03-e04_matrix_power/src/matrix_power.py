#!/usr/bin/env python3

from functools import reduce
import numpy as np

def matrix_power(a, n):
    if n < 0:
        return np.linalg.inv(matrix_power(a, -n))
    elif n == 0:
        return np.eye(a.shape[0])
    else:
        # return a @ matrix_power(a, n-1)
        return reduce(np.matmul, np.array([a, matrix_power(a, n-1)]))

def main():
    return  

if __name__ == "__main__":
    main()
