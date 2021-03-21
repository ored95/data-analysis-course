#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    return df['Snow depth (cm)'].max()

def main():
    print('Max snow depth: {:.1f}'.format(snow_depth()))

if __name__ == "__main__":
    main()
