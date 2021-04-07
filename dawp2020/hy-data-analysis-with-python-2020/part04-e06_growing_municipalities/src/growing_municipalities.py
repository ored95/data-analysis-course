#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    increasing_population_change = df[df.columns[1]] > 0
    growing_count = df[increasing_population_change].shape[0]
    proportion = growing_count / df.shape[0]
    return proportion

def main():
    df = pd.read_csv('src/municipal.tsv', index_col=0, sep='\t')
    df = df["Akaa":"Kannus"]
    print('Proportion of growing municipalities: {:.1f}%'.format(growing_municipalities(df)))

if __name__ == "__main__":
    main()
