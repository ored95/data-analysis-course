#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

wd = dict(zip('ma ti ke to pe la su'.split(), 'Mon Tue Wed Thu Fri Sat Sun'.split()))
mo = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

def split_date(df):
    df = df.str.split(expand=True)
    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df['Weekday'] = pd.Series(df['Weekday']).map(wd)
    df['Month']   = pd.Series(df['Month']).map(mo)
    df['Hour']    = pd.Series(df['Hour']).map(lambda x: x[:2])
    df = df.astype(dict(zip(df.columns, [object, int, int, int, int])))
    return df

def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')      # Remove NaN cols/rows
    sample  = split_date(df['Päivämäärä'])
    sample['DatetimeIndex'] = pd.to_datetime(sample[["Year", "Month", "Day", "Hour"]])
    df = pd.concat([sample['DatetimeIndex'], df[df.columns[1:]]], axis=1)
    df = df.set_index('DatetimeIndex')
    return df

def commute():
    df = bicycle_timeseries()["2017-08-01":"2017-08-31"]
    print(df)
    # Instruction: 
    # 1. https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.weekday.html
    # 2. https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html
    df['Weekday'] = df.index
    df['Weekday'] = df['Weekday'].dt.weekday + 1
    df = df.groupby('Weekday').sum()
    return df
    
def main():
    df = commute()
    df.plot()
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()

if __name__ == "__main__":
    main()
