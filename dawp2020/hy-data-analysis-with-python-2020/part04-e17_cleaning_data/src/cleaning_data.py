#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    for col in ['President', 'Vice-president']:
        df[col] = pd.Series(df[col]).str.title().str.replace(r'(\w+)\,\s+(\w+)', r'\2 \1', regex=True)
    df['Start'] = pd.Series(df['Start']).str.split().str[0]
    df.loc[df['Last'] == '-', 'Last'] = np.nan
    df.loc[df['Seasons'] == 'two', 'Seasons'] = 2
    df = df.astype(dict(zip(df.columns, [object, int, float, int, object])))
    return df

def main():
    df = cleaning_data()
    print(df.dtypes)
    print(df)

if __name__ == "__main__":
    main()
