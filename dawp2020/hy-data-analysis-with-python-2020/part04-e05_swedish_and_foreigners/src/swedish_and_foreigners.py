#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    regions = list(df['Region 2018'])
    begin, end = regions.index('Akaa'), regions.index('Äänekoski')
    df = df.drop(['Region 2018'], axis=1)[begin:end+1]
    df.index = regions[begin:end+1]
    return df

def swedish_and_foreigners():
    df = municipalities_of_finland()
    # choice = (df['Share of Swedish-speakers of the population, %'] > 5) & (df['Share of foreign citizens of the population, %'] > 5)
    choice = (df[df.columns[2]] > 5) & (df[df.columns[3]] > 5)
    df = df[choice]
    df = df.iloc[:,[0,2,3]]
    return df

def main():
    print(swedish_and_foreigners().describe())

if __name__ == "__main__":
    main()
