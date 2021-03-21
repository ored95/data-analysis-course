#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    return '{0} = {1}'.format(' + '.join(map(str, L)), sum(L))

def main():
    print(sum_equation([1, 5, 7]))
    pass

if __name__ == "__main__":
    main()
