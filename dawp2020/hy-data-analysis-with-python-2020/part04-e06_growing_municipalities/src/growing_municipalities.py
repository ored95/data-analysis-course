#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    c = "Population change from the previous year, %"
    n = len(df)
    k = sum(df[c] > 0.0)
    return k / n
 
def main():
    df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
    df = df["Akaa":"Kannus"]
    proportion = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {proportion:.1%}")
 
if __name__ == "__main__":
    main()
