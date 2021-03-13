#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = np.square(a)
    va = a.sum(axis=1)      # row sum
    return np.sqrt(va)
    
def main():
    print(vector_lengths(np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ])))

if __name__ == "__main__":
    main()
