import numpy as np
import skimage as ski
import skimage.io as io
import skimage.util as util
import matplotlib.pyplot as plt

I = io.imread("biplan.png")
print(I.dtype)
print(I.min(), I.max())

I = ski.img_as_float(I)
print(I.dtype)
print(I.min(), I.max())

plt.figure(figsize=(8,8))
plt.imshow(I, "gray")
plt.show()

J = util.random_noise(I, mode="gaussian", var=1)
plt.figure(figsize=(8,8))
plt.imshow(J, "gray")
plt.show()