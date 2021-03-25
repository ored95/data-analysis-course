#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    bands['Band'] = pd.Series(bands['Band']).str.upper()
    top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    return pd.merge(top40, bands, left_on='Artist', right_on='Band', how='inner', sort=True)

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
