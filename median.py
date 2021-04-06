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
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

plt.imshow(median_filter(I2) ,'gray')
plt.show()