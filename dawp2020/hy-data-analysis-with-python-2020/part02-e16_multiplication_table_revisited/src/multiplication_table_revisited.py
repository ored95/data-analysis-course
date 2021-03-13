#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    row = np.arange(n)
    col = np.arange(n).reshape((n,1))
    return row * col

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
