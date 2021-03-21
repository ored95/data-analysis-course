#!/usr/bin/env python3

import sys

def summary(filename='src/example.txt'):
    try:
        f = open(filename, 'r')
        X = []
        for line in f.readlines():
            try:
                X.append(float(line))
            except ValueError as ev:
                print(ev.args, file=sys.stderr)
                continue
        f.close()

        _sum    = sum(X)
        _avg    = _sum / len(X)
        _stddev = (sum([(x - _avg) ** 2 for x in X]) / (len(X) - 1)) ** 0.5
        del X
        return (_sum, _avg, _stddev)
    except ZeroDivisionError as ez:
        print(ez.args, file=sys.stderr)
    return None     # FileNotFound raised

def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            res = summary(filename)
            if res: 
                print('File: {0} Sum: {1:.6f} Average: {2:.6f} Stddev: {3:.6f}'.format(filename, res[0], res[1], res[2]))
    else:
        print('Command line too short', file=sys.stderr)

if __name__ == "__main__":
    main()
