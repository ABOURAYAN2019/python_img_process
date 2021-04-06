#!/usr/bin/env python
# coding: utf-8

# # Codecast: quantification des informations
# 
# - Diviser par 20 le nombre de couleurs
# 
# <span class="graffiti-highlight graffiti-id_lyp3wo4-id_zp7is16"><i></i><button>Démarrer</button></span>

# In[61]:


import skimage
import matplotlib.pyplot as plt
I = skimage.data.astronaut()
print(I.shape)
J = I[:,: ,2]
plt.imshow(J ,'gray')
plt.show()

