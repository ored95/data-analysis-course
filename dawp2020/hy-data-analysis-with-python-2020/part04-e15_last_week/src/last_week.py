#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    
    # clean dataframe
    df = df[(df['LW'] != 'New') & (df['LW'] != 'Re')]
    df = df.astype({'LW': np.int64})
    
    # append unknown songs to top40 of last week
    nan_rows = set(range(1, 41)) - set(df['LW'])
    for id in nan_rows:
        df = df.append({'LW': id}, ignore_index=True)

    # redefine last week WoC
    df['WoC'] = df['WoC'] - 1
    
    # reconfig index of our dataframe
    df.index = range(1, 41)
    
    # remember that peakpos = min(pos, lw, peakpos)
    # if the peakpos is equal to current pos and lower than the 
    # last week pos, then the last week peakpos is undefined.
    # otherwise, the peakpos is not changed.
    for i in range(1, 41):
        if df.loc[i, 'Peak Pos'] != np.nan:
            if df.loc[i, 'Peak Pos'] == df.loc[i, 'Pos'] and df.loc[i, 'Peak Pos'] < df.loc[i, 'LW']:
                df.loc[i, 'Peak Pos'] = np.nan
    
    # update last week dataframe
    df['Pos'] = df['LW']
    df.loc[:,'LW'] = np.nan
    
    # Correct pos by ascending
    df = df.sort_values(by=['Pos'])
    df.index = range(1, 41)     # reset index
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()
