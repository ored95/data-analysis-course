#!/usr/bin/env python3

import pandas as pd

c = 'Population change from the previous year, %'

def growing_municipalities(df):
    return df[df[c] > 0.0]

def main():
    df = pd.read_csv('src/municipal.tsv', index_col=0, sep='\t')
    df = df["Akaa":"Kannus"]
    for i in growing_municipalities(df)[c]:
        print('Proportion of growing municipalities: {:.1f}%'.format(i))

if __name__ == "__main__":
    main()
