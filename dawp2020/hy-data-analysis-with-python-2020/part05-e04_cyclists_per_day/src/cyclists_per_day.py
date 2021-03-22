#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

mo = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

def split_date(df):
    df = df.str.split(expand=True).drop([0, 4], axis=1)
    df.columns = ['Day', 'Month', 'Year']
    df['Month'] = pd.Series(df['Month']).map(mo)
    df = df.astype(dict(zip(df.columns, [int, int, int])))
    return df
    
def cyclists_per_day():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')      # Remove NaN cols/rows
    
    ymd     = split_date(df['Päivämäärä'])
    regions = df[df.columns[1:]]
    df = pd.concat([ymd, regions], axis=1)
    
    df = df.groupby(['Year', 'Month', 'Day']).sum()
    return df    

def main():
    # Get dataframe with MultiIndex
    cyclist = cyclists_per_day()
    
    # Select from MultiIndex by Level
    # c = (cyclist.index.get_level_values('Year') == 2017) & (cyclist.index.get_level_values('Month') == 8)  
    # data = cyclist[c]
    data = cyclist.loc[(2017, 8), :]

    # Display chart
    data.plot()
    plt.xlim(1, 31)
    plt.show()

if __name__ == "__main__":
    main()
