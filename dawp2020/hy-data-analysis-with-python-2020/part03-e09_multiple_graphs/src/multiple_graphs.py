#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    x1, y1 = np.array([2,4,6,7]), np.array([4,3,5,1])
    x2, y2 = np.array([1,2,3,4]), np.array([4,2,3,1])
    # Same as: plt.plot(x1, y1, 'g', x2, y2, 'r')
    plt.plot(x1, y1, 'g')
    plt.plot(x2, y2, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('part03-e09')
    plt.show()

if __name__ == "__main__":
    main()
