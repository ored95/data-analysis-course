#!/usr/bin/env python3

def main():
    print('\n'.join(['({0}, {1})'.format(i, j) for j in range(1, 5) for i in range(1, 5) if i + j == 5]))

if __name__ == "__main__":
    main()
