import matplotlib.pyplot as plt
from scipy.ndimage import filters
import skimage
import skimage.filters

brick = skimage.data.brick()
plt.imshow(brick, 'gray')
plt.show()

I = filters.uniform_filter(brick, size=(15, 15))
plt.imshow(I, 'gray')
plt.show()

I = skimage.filters.gaussian(brick, 5)
plt.imshow(I, 'gray')
plt.show()

I = skimage.filters.prewitt(brick)
plt.imshow(I, 'gray')
plt.show()

I = skimage.filters.laplace(brick)
plt.imshow(I, 'gray')
plt.show()