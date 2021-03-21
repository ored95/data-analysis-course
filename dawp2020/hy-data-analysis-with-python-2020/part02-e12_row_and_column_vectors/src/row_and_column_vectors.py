#!/usr/bin/env python3

import numpy as np
from numpy.core.fromnumeric import reshape

def get_row_vectors(a):
    return [np.array(r.reshape(1, len(r))) for r in a]

def get_column_vectors(a):
    return [np.array(c.reshape(len(c), 1)) for c in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
