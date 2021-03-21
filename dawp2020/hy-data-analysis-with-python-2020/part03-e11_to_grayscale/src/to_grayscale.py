#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def fade(image):
    width = image.shape[1]
    m = np.linspace(0, 1, width).reshape(1, width, 1)
    result = image * m  # note that we rely on broadcasting here
    return result

def to_grayscale(img):
    return np.dot(img[...,:3], [0.2126, 0.7152, 0.0722])

def to_red(img):
    img[:,:,1] = 0  # Zero out contribution from green
    img[:,:,2] = 0  # Zero out contribution from blue 
    return img

def to_green(img):
    img[:,:,0] = 0  # Zero out contribution from red
    img[:,:,2] = 0  # Zero out contribution from blue 
    return img

def to_blue(img):
    img[:,:,0] = 0  # Zero out contribution from red
    img[:,:,1] = 0  # Zero out contribution from green
    return img

def main():
    painting = plt.imread('src/painting.png')
    m = to_grayscale(painting.copy())
    plt.imshow(m, cmap=plt.get_cmap('gray'))

    _, ax = plt.subplots(3)
    ax[0].imshow(  to_red(painting.copy()))
    ax[1].imshow(to_green(painting.copy()))
    ax[2].imshow( to_blue(painting.copy()))
    for x in ax:
        x.set_axis_off()
    plt.show()

if __name__ == "__main__":
    main()
