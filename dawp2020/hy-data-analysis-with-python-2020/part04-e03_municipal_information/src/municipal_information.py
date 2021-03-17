#!/usr/bin/env python3

from numpy.core.fromnumeric import shape
import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    print('Shape: {},{}'.format(df.shape[0], df.shape[1]))
    print('Columns:')
    for c in df.columns:
        print(c)


if __name__ == "__main__":
    main()
