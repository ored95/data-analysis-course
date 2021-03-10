#!/usr/bin/env python3

import math


def main():
    while True:
        choice = str(input('Choose a shape (triangle, rectangle, circle): '))
        if choice == '':
            break
        elif choice == 'triangle':
            base   = float(input('Give base of the triangle: '))
            height = float(input('Give height of the triangle: '))
            print('The area is {0}'.format(0.5 * base * height))
        elif choice == 'rectangle':
            width = float(input('Give width of the rectangle: '))
            height = float(input('Give height of the rectangle: '))
            print('The area is {0}'.format(width * height))
        elif choice == 'circle':
            radius = float(input('Give radius of the circle: '))
            print('The area is {0}'.format(math.pi * radius ** 2))
        else:
            print('Unknown shape!')

if __name__ == "__main__":
    main()
