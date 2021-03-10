#!/usr/bin/env python3
import numpy as np
def transform(s1, s2):
    L1 = list(map(int, s1.split()))
    L2 = list(map(int, s2.split()))
    return [x * y for x, y in zip(L1, L2)]

def main():
    pass

if __name__ == "__main__":
    main()
