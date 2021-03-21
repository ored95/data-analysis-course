#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    lst = []
    with open(filename, 'r') as f:
        for line in f:
            # a = re.sub(r'(\d+)\s+(\d+)\s+(\d+)\s+(\w+)\n', r'\1\t\2\t\3\t\4', line, 1)
            a = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+([\w,\s]+)\n', line)
            if a:
                lst.append('\t'.join(a[0]))
    return lst


def main():
    pass

if __name__ == "__main__":
    main()
