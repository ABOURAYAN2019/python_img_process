import skimage
from skimage import io
from skimage import metrics
import numpy as np
import matplotlib.pyplot as plt
I = skimage.io.imread("imrane.jpg")
skimage.io.imsave("imranebt.jpg" ,I ,quality=31)
I2=skimage.io.imread("imranebt.jpg")
print(I2.shape)
print(I.shape)
plt.imshow(I2,'gray')

plt.figure(figsize=(10, 10))
plt.subplot(121)
plt.imshow(I2, 'gray')

d = np.abs(I-I2)
plt.subplot(122)
plt.imshow(d)

mse = skimage.metrics.mean_squared_error(I, I2)
plt.title('MSE '+ str(mse))
plt.show()