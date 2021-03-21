#!/usr/bin/env python3
# Hint: The enumerate(L) function call can be thought to be equivalent to zip(range(len(L)), L).

def find_matching(L, pattern):
    return [i for i, _ in enumerate(L) if pattern in L[i]]

def main():
    pass

if __name__ == "__main__":
    main()
