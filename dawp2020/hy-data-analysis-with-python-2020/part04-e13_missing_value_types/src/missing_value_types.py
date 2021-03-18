#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state    = pd.Series(np.array(['United Kingdom',  'Finland',   'USA', 'Sweden',    'Germany', 'Russia']), name='State')
    yearOfIndependence = np.array([          np.nan,       1917,    1776,     1523,       np.nan,     1992], dtype=np.float64)
    president          = np.array([          np.nan, 'Niinistö', 'Trump',   np.nan, 'Steinmeier',  'Putin'], dtype=object)
    return pd.DataFrame({'Year of independence': yearOfIndependence, 'President': president}, index=state)
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
