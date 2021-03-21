#!/usr/bin/env python3

def extract_numbers(s):
    words = [w.strip('"\n()') for w in s.split()]
    numbs = []
    for word in words:
        try:
            _int = int(word)   
            numbs.append(_int)
        except ValueError:
            try:
                _float = float(word)
                numbs.append(_float)
            except ValueError:
                continue
    del words
    return numbs

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
