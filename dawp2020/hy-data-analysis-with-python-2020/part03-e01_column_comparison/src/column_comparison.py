#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    b = a.T
    c = b[1] > b[-2]
    return a[c.T]
    
def main():
    pass

if __name__ == "__main__":
    main()
