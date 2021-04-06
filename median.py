import sys
import skimage
import skimage.io as io
from skimage import data
from skimage import filters
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
I2= skimage.io.imread('noise.png')
#I2=skimage.color.rgb2gray(I2)
plt.imshow(I2 ,"gray")
plt.show()
print(I2.shape)
print(I2)
print(I2.dtype)
print(np.min(I2) ,np.max(I2) )


def median_filter(data, filter_size=5):
    temp = []
    indexer = filter_size // 2
    window = [
        (i, j)
        for i in range(-indexer, filter_size-indexer)
        for j in range(-indexer, filter_size-indexer)
    ]
    index = len(window) // 2
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = sorted(
                0 if (
                    min(i+a, j+b) < 0
                    or len(data) <= i+a
                    or len(data[0]) <= j+b
                ) else data[i+a][j+b]
                for a, b in window
            )[index]
    return data

plt.imshow(median_filter(I2) ,'gray')
plt.show()