#!/usr/bin/env python3
import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np

def read_series():
    series  = []
    indexes = []
    while True:
        line = str(input())
        if len(line) == 0:
            break
        try:
            k, v = line.split(maxsplit=1)
            print(line)
            if len(k.strip()) == 0 or len(v.strip()) == 0:
                raise Exception('Invalid line format')
            else:
                indexes.append(k.strip())
                series.append(v.strip())
        except Exception:
            continue
    return pd.Series(series, index=indexes)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
