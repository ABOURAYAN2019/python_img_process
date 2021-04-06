import skimage
from skimage import io
from skimage.transform import resize
from skimage import metrics
import numpy as np
import matplotlib.pyplot as plt
I = skimage.data.brick()
J= skimage.data.camera()
X= I/2+J/2
plt.imshow(X , "gray")
plt.show()
print(X.shape)
print(np.min(X))
print(np.max(X))
I2 = I+ 150
plt.imshow(I2 , "gray" ,vmin=0 ,vmax=255)
plt.show()
"""
def imagesize(image):
  print(image.shape)
  a = np.array(image.shape)
  c=np.prod(a)
  return c
print(imagesize(I))




I1 = I[:,:,1]
plt.imshow(I1 ,'gray')
plt.show()
q= 3
I2 = I1//q*q
plt.imshow(I2 ,'gray')
plt.show()

(a ,b)= np.unique(I1, return_counts=True)
(c,d) = np.unique(I2, return_counts=True)
print(len(b))
print(len(d))

#print(imagesize(I))

croitie= skimage.io.imread("https://gitlab.emse.fr/gavet/mooc_ti_data/-/raw/master/croatie.jpg?inline=false")
print(croitie.shape)
#print(imagesize(croitie))
i = 1
limite = 1000000
myimgsize = imagesize(croitie)
#print(myimgsize)

while myimgsize >  limite :
  i = i + 1
  #print("hello im in the boucle")
  #print( "jesuis i" + str(i))
  myshape = (croitie.shape[0]//i,croitie.shape[1]//i)
  #print(myshape)
  image = resize(croitie ,myshape  ,preserve_range=True ,anti_aliasing=False).astype('uint8')
  #print(image.shape)
  myimgsize = imagesize(image)
  print(myimgsize)
  #print(i)

def convertimage (image) :
  print(image.shape)
  rouge = image [:,: ,0]
  vert = image[:,: ,1]
  blue = image [:,: ,2]
  rouge = rouge * 0.2125
  vert = vert* 0.7154
  blue = blue*0.0721
  Gris =   rouge+blue+vert
  Gris =Gris.astype('uint8')
  print(Gris.shape )
  plt.imshow(Gris ,"gray")
  plt.show()
  return Gris

convertimage(I)
"""