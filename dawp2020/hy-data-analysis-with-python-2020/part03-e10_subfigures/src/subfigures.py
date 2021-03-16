#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    _, ax = plt.subplots(1, 2)
    ax[0].plot(a.T[0], a.T[1])
    ax[1].scatter(a.T[0], a.T[1], c=a.T[2], s=a.T[3])
    plt.show()

def main():
    # Note: if input array looks like
    # a = numpy.array([
    #     [1,  2, 'r', 2.],
    #     [3,  4, 'g', 2.],
    #     [5, 19, 'b', 3.],
    #     [6,  4, 'r', 1.],
    #     [8,  1, 'y', 2.]
    # ])
    # then each sublists in array a will have ALL str-type items.
    # Calling function subfigures() will cause an error below:
    # https://stackoverflow.com/questions/42013903/typeerror-ufunc-multiply-did-not-contain-a-loop-with-signature-matching-types
    subfigures(np.array([
        [1,  2, 255, 2.],
        [3,  4,   0, 2.],
        [5, 19, 127, 3.],
        [6,  4,  43, 1.],
        [8,  1, 133, 2.]
    ]))

if __name__ == "__main__":
    main()
