#!/usr/bin/env python3

import sys

def file_count(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        words = [w for line in lines for w in line.split()]
        chars = sum(list(map(len, lines)))
        return len(lines), len(words), chars
    except EnvironmentError:
        print('FileNotFoundError: No such file or directory: {0}'.format(filename), file=sys.stderr)
        return None

def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            res = file_count(filename)
            if res:
                print('{0}\t{1}\t{2}\t{3}'.format(res[0], res[1], res[2], filename))
    else:
        print('Command line too short', file=sys.stderr)

if __name__ == "__main__":
    main()
