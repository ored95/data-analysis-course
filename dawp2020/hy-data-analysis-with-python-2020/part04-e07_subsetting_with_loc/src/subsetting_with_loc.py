#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', index_col=0, sep='\t')['Akaa':'Äänekoski']
    df = df.loc[:,['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return df

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()
