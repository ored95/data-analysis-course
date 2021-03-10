#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    if a != 0:
        d = b ** 2 - 4 * a * c
        x = -b / 2 / a
        if d == 0:
            return x, x
        elif d > 0:
            y = math.sqrt(d) / 2 / a
            return x - y, x + y
    return False

def main():
    pass

if __name__ == "__main__":
    main()
