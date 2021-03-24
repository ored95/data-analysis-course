#!/usr/bin/env python3

import pandas as pd

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

def main():
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()
