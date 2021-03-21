#!/usr/bin/env python3
# Note: arr[::-1] - Reverses the array

import numpy as np

def get_rows(a):
    return [np.array(r) for r in a]

def get_columns(a):
    return [np.array(c) for c in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
