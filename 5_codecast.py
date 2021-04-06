#!/usr/bin/env python
# coding: utf-8

# # Codecast: chargement d'une image
#  
# Ce premier codecast permet de s'initier au chargement, la manipulation et la visualisation des images. Dans un premier temps, une image est chargée. Nous allons afficher le type des données, ainsi que la définition de l'image.
# 
# ## Objectifs
# 
# Après ce premier notebook, vous saurez:
# 
# * Charger et visualiser une image à niveaux de gris et une image en couleurs.
# * Afficher la taille de l'image en pixels, ainsi que le type des données
# * Afficher les différents canaux de couleurs séparément.
# 
# 
# 
# <span class="graffiti-highlight graffiti-id_ozjnshd-id_etaxe89"><i></i><button>Démarrer</button></span>

# In[ ]:


import skimage
import matplotlib.pyplot as plt


# In[ ]:


I = skimage.data.camera()


# In[ ]:


print(I)


# In[ ]:


print(I.shape)


# In[ ]:


plt.imshow(I)
plt.show()


# In[ ]:


plt.imshow(I, 'gray')
plt.show()


# In[ ]:


cat = skimage.data.chelsea()


# In[ ]:


print(cat.shape)


# In[ ]:


print(cat.dtype)


# In[ ]:


plt.imshow(cat)
plt.show()


# In[ ]:


for c in range(3):
    plt.imshow(cat[:,:,c], 'gray')
    plt.show()


# In[ ]:


I = skimage.io.imread('test.jpg')

