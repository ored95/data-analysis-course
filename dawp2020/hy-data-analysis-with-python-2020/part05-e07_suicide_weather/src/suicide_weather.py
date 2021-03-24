#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',').drop(['year', 'sex', 'age'], axis=1)
    df['suicide fractions'] = np.where(df['population'] == 0, np.nan, df['suicides_no'] / df['population'])
    df = df.groupby('country').mean()
    return df.drop(df.columns[:2], axis=1)

def fix_minus_unicode(s):
    minus = "\u2212"  # unicode minus sign
    return float(s.replace(minus, '-'))

def suicide_weather():
    df1 = suicide_fractions()
    df2 = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col=0, header=0)[0]
    df2[df2.columns[0]] = pd.Series(df2[df2.columns[0]]).apply(fix_minus_unicode)
    df = pd.merge(df1, df2, how='inner', left_index=True, right_index=True)
    correlation = pd.Series(df[df.columns[1]]).corr(pd.Series(df[df.columns[0]]), method='spearman')
    return len(df1), len(df2), len(df), correlation

def main():
    x = suicide_weather()
    text = '''
    Suicide DataFrame has {} rows
    Temperature DataFrame has {} rows
    Common DataFrame has {} rows
    Spearman correlation: {:.6f}
    '''
    print(text.format(x[0], x[1], x[2], x[3]))

if __name__ == "__main__":
    main()
