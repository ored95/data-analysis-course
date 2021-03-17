#!/usr/bin/env python3

from numpy.core.defchararray import index
import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    print(inverse_series(pd.Series([1, 2, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])))

if __name__ == "__main__":
    main()
