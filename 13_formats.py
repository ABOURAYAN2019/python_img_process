#!/usr/bin/env python
# coding: utf-8

# # Formats de fichiers
# 
# Ce codecast permet d'illustrer la perte de qualité lorsque le format d'enregistrement utilisé est le JPEG.
# 
# <span class="graffiti-highlight graffiti-id_nnhwb2k-id_8xc5zhf"><i></i><button>Démarrer</button></span>

# In[ ]:


import skimage
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure
skimage.measure.label

I = skimage.data.camera()
plt.imshow(I, 'gray')
plt.show()


# In[ ]:


skimage.io.imsave('test.jpg', I, quality=31)


# In[ ]:


I2 = skimage.io.imread('test.jpg')


# In[ ]:


plt.figure(figsize=(10, 10))
plt.subplot(121)
plt.imshow(I2, 'gray')

d = np.abs(I-I2)
plt.subplot(122)
plt.imshow(d)

mse = skimage.metrics.mean_squared_error(I, I2)
plt.title('MSE '+ str(mse))
plt.show()


# In[ ]:


skimage.io.imsave('test.png', I)
I2 = skimage.io.imread('test.png')
print(skimage.metrics.mean_squared_error(I, I2))


# In[ ]:




