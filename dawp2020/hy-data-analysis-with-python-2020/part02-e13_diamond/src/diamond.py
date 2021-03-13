#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n < 0:
        return None
    _id = np.eye(n, dtype=int)      # identity matrix (diagonal)
    rid = _id[::-1]                 # reversed | create an anti-diagonal matrix
    left    = np.concatenate((rid, _id[1:]), axis=0)
    right   = np.concatenate((_id, rid[1:]), axis=0)
    return np.concatenate((left.T, right.T[1:]), axis=0)

def main():
    print(diamond(1))
    pass

if __name__ == "__main__":
    main()
