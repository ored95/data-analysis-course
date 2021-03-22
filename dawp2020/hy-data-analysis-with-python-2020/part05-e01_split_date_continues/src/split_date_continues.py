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

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')      # Remove NaN cols/rows
    firstfive  = split_date(df['Päivämäärä'])
    twentyleft = df[df.columns[1:]]
    return pd.concat([firstfive, twentyleft], axis=1)

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
