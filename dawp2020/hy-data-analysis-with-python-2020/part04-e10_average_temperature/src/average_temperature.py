#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    df = df[df['m'] == 7]
    return df.iloc[:,-1].mean()

def main():
    print('Average temperature in July: {:.1f}'.format(average_temperature()))

if __name__ == "__main__":
    main()
