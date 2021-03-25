#!/usr/bin/env python3

from os import sep
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

def cycling_weather():
    df1 = split_date_continues()
    df2 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    df = pd.merge(df1, df2, left_on=['Day', 'Month', 'Year'], right_on=['d', 'm', 'Year'])
    df = df.drop(['m', 'd', 'Time', 'Time zone'], axis=1)
    return df

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
