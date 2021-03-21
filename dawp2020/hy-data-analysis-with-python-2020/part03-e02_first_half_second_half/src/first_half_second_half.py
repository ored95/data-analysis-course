#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    first, second = np.split(a, 2, axis=1)
    # (first version): c = first.sum(axis=1) > second.sum(axis=1)
    c = np.sum(first, axis=1) > np.sum(second, axis=1)
    return a[c]

def main():
    pass

if __name__ == "__main__":
    main()
