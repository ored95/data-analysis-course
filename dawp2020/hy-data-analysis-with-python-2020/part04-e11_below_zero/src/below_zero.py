#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    c = df[df.columns[-1]] < 0.0
    return len(df[c])

def main():
    print('Number of days below zero: {}'.format(below_zero()))
    
if __name__ == "__main__":
    main()
