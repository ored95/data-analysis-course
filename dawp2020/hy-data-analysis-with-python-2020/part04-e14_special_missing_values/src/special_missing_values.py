#!/usr/bin/env python3

from numpy.core.defchararray import isdigit
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')    
    df = df[(df['LW'] != 'New') & (df['LW'] != 'Re')]
    df = df.astype({'LW': np.int64})
    df = df[df['LW'] < df['Pos']]
    return df

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
