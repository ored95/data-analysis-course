#!/usr/bin/env python3

import pandas as pd
import numpy as np
def municipalities_of_finland():
    # df = pd.read_csv('src/municipal.tsv', sep='\t')
    # regions = list(df['Region 2018'])
    # begin, end = regions.index('Akaa'), regions.index('Äänekoski')
    # df = df.drop(['Region 2018'], axis=1)[begin:end+1]
    # df.index = regions[begin:end+1]
    df = pd.read_csv('src/municipal.tsv', index_col=0, sep='\t')
    return df['Akaa':'Äänekoski']
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
