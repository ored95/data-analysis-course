#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

wd = dict(zip('ma ti ke to pe la su'.split(), 'Mon Tue Wed Thu Fri Sat Sun'.split()))
mo = dict(zip('tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu'.split(), range(1,13)))

def split_date(df):
    df = df.str.split(expand=True)
    df = df[df.columns[1:4]]
    df.columns = ['Day', 'Month', 'Year']
    df['Month']   = pd.Series(df['Month']).map(mo)
    df = df.astype(dict(zip(df.columns, [int, int, int])))
    return df

def split_date_continues(station):
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')      # Remove NaN cols/rows
    date = split_date(df['Päivämäärä'])
    df = pd.concat([date, df[station]], axis=1)
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df = df.drop(['Year', 'Month', 'Day'], axis=1)
    df = df.groupby('Date').sum()
    return df['2017-01-01':'2017-12-31']

def cycling_weather(station):
    df1 = split_date_continues(station)
    df1 = df1.reset_index()             # Reset the index of the DataFrame, and use the default one instead

    df2 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    df2 = df2.drop(['m', 'd', 'Time', 'Time zone', 'Year'], axis=1)
    df2 = df2.fillna(method='ffill')    # forward fill the missing values

    df = pd.merge(df1, df2, left_index=True, right_index=True)
    return df

def cycling_weather_continues(station):
    # Clean data
    df = cycling_weather(station)

    # Regression
    model = LinearRegression(fit_intercept=True)
    X = df[df.columns[2:]]
    y = df[station]
    model.fit(X, y)
    return model.coef_, model.score(X, y)
    
def main():
    stations = 'Auroransilta;Eteläesplanadi;Huopalahti (asema);Kaisaniemi/Eläintarhanlahti;Kaivokatu;Kulosaaren silta et.;Kulosaaren silta po. ;Kuusisaarentie;Käpylä, Pohjoisbaana;Lauttasaaren silta eteläpuoli;Merikannontie;Munkkiniemen silta eteläpuoli;Munkkiniemi silta pohjoispuoli;Heperian puisto/Ooppera;Pitkäsilta itäpuoli;Pitkäsilta länsipuoli;Lauttasaaren silta pohjoispuoli;Ratapihantie;Viikintie;Baana'.split(';')
    station = stations[np.random.randint(len(stations))]
    print('Measuring station: {}'.format(station))
    cwc = cycling_weather_continues(station)
    for v, i in zip('precipitation,snow depth,temperature'.split(','), range(3)):
        print('Regression coefficient for variable \'{}\': {:.1f}'.format(v, cwc[0][i]))
    print('Score: {:.2f}'.format(cwc[1]))

if __name__ == '__main__':
    main()
