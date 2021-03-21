#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', index_col=0, sep='\t')['Akaa':'Äänekoski']
    # choice = (df['Share of Swedish-speakers of the population, %'] > 5) & (df['Share of foreign citizens of the population, %'] > 5)
    choice = (df[df.columns[2]] > 5) & (df[df.columns[3]] > 5)
    df = df[choice]
    df = df.iloc[:,[0,2,3]]
    return df

def main():
    print(swedish_and_foreigners().describe())

if __name__ == "__main__":
    main()
