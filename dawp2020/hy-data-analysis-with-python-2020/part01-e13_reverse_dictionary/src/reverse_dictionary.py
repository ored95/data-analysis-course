#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    for key, vals in d.items():
        for v in vals:
            if v in rd.keys():
                rd[v] += [key]
            else:
                rd[v] = [key]
            
    return rd

def main():
    pass

if __name__ == "__main__":
    main()
