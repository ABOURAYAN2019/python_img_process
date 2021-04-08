from skimage.filters.rank import median
from skimage.morphology import disk, ball
import skimage.metrics
import skimage as ski
import skimage.io as io
import skimage.util as util
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters.rank import minimum, maximum, median


# Chargement d'une image
I = io.imread("https://gitlab.emse.fr/gavet/mooc_ti_data/-/raw/master/jambe.png?inline=false")
plt.imshow(I, 'gray')
plt.show()

# On bruite l'image
J = 255 *util.random_noise(I, mode='s&p', amount=0.1)
J = J.astype(np.uint8)
plt.figure(figsize=(8,8))
plt.imshow(J, 'gray')
plt.show()

def ratio_eqm(I, J, S=5):
    Ifma = fma(J)
    Imed = median(J, disk(S))
    print("Ifmaimage")
    print(  Ifma.shape)
    print("Ifmamed")
    print(Imed.shape)
    eqm_fma = skimage.metrics.mean_squared_error(I, Ifma)
    print(eqm_fma)
    eqm_med = skimage.metrics.mean_squared_error(I, Imed)
    print(eqm_med)
    return eqm_fma / eqm_med


def fma(J, S=5):
    temp = []
    indexer = S // 2
    data_final = []
    data_final = np.zeros((len(J), len(J[0])))
    for i in range(len(J)):

        for j in range(len(J[0])):

            for z in range(S):
                if i + z - indexer < 0 or i + z - indexer > len(J) - 1:
                    for c in range(S):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(J[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(S):
                            temp.append(J[i + z - indexer][j + k - indexer])

            temp.sort()

            zmed = temp[len(temp) // 2]
            Ip = J[i][j]
            zmin = np.min(temp)
            zmax = np.max(temp)
            if Ip == zmin or Ip==zmax :
                data_final[i][j] = zmed

            else:
                data_final[i][j] = J[i][j]
            temp = []

    return data_final.astype('uint8')


print( "ratiofma :  " + str(ratio_eqm(I,J)))