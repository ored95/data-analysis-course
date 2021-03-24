#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',').drop(['year', 'sex', 'age'], axis=1)
    df['suicide fractions'] = np.where(df['population'] == 0, np.nan, df['suicides_no'] / df['population'])
    df = df.groupby('country').mean()
    return pd.Series(df[df.columns[2]])

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
