#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    tups = []
    with open(filename, 'r') as f:
        for line in f:
            pattern = r'(\d+)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d+)\s+(\d+):(\d+)\s+([a-zA-Z0-9\s_\.\-:]+)\n'
            m = (re.findall(pattern, line))[0]
            tups.append((int(m[0]), str(m[1]), int(m[2]), int(m[3]), int(m[4]), str(m[5])))
    return tups

def main():
    pass

if __name__ == "__main__":
    main()
