#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

def center(a):
    h,w = a.shape[:2]
    return ((h-1)/2, (w-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    h,w = a.shape[:2]
    cx, cy = center(a)
    d = [np.sqrt((i-cx)**2 +(j-cy)**2) for i in range(h) for j in range(w)]
    return np.array(d).reshape(h, w)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range [tmin,tmax]."""
    copy = a.copy()
    if copy.max() > copy.min():
        copy = tmin + (tmax - tmin) * (copy - copy.min()) / (copy.max() - copy.min())
        copy = np.ones(copy.shape) - copy
    else:
        copy = np.ones(copy.shape)
    return copy

def radial_mask(a):
    sample = radial_distance(a)
    return scale(sample)

def radial_fade(a):
    mask = radial_mask(a)
    h, w = mask.shape[:2]
    mask = mask.reshape((h, w, 1))
    return a * mask

def main():
    painting = plt.imread('src/painting.png')
    m = painting.copy()
    _, ax = plt.subplots(3,)
    ax[0].imshow(m)
    ax[1].imshow(radial_mask(m))
    ax[2].imshow(radial_fade(m))
    for x in ax:
        x.set_axis_off()
    plt.show()

if __name__ == "__main__":
    main()
