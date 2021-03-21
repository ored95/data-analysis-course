#!/usr/bin/env python3

import pandas as pd
import numpy as np

wd = dict(zip('ma ti ke to pe la su'.split(), 'Mon Tue Wed Thu Fri Sat Sun'.split()))
mo = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')['Päivämäärä']
    df = df.str.split(expand=True)
    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df = df.dropna(axis=0, how='all')      # Remove NaN rows
    df['Weekday'] = pd.Series(df['Weekday']).map(wd)
    df['Month']   = pd.Series(df['Month']).map(mo)
    df['Hour']    = pd.Series(df['Hour']).map(lambda x: x[:2])
    df = df.astype({'Day': int, 'Year': int, 'Hour': int})
    return df

def main():
    df = split_date()
    print('Shape:', df.shape)
    print('dtypes:', df.dtypes)
    print('Columns:', df.columns)
    print(df.head())
       
if __name__ == '__main__':
    main()
