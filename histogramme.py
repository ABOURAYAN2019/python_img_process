import sys
import skimage
import skimage.io as io
from skimage import data
from skimage import filters
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
I2= skimage.data.camera()
#I2=skimage.color.rgb2gray(I2)
plt.imshow(I2 ,"gray")
plt.show()
print(I2.shape)
print(I2)
print(I2.dtype)
print(np.min(I2) ,np.max(I2) )

def ajustement_gamma(I, gamma=2):
    J=I/255
    X=np.power(J,gamma)
    X=X*255
    Z=X.astype("uint8")
    return Z


#plt.imshow(ajustement_gamma(I2) ,"gray")
#plt.show()


def ajustement_gamma(I, gamma=2):
    J=I/255
    X=np.power(J,gamma)
    X=X*255
    Z=X.astype("uint8")
    return Z

def ajustement_nonlineaire(I, E=1):
    m = np.average(I)
    epsilon = sys.float_info.epsilon
    B= m/(I+epsilon)
    C=np.power(B,E)
    D=C+1
    F=1/D
    F2=255*F
    return F2

plt.imshow(ajustement_nonlineaire(I2) ,'gray')
plt.show()

