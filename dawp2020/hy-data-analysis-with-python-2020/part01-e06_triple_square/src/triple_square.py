#!/usr/bin/env python3

def triple(x):
    return 3 * x

def square(x):
    return x ** 2

def main():
    for x in range(1, 11):
        x2 = square(x)
        x3 = triple(x)
        if x > 3:
            break
        print("triple({0})=={1} square({0})=={2}".format(x, x3, x2))
        
if __name__ == "__main__":
    main()
