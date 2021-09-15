import numpy as np

# Eliminar todos los elementos que correspondan al valor indicado #############
array1 = np.array([10,40,20,40,30,40,50])
valorE = np.array([40])
arrayE = np.setdiff1d(array1,valorE)
print(arrayE)

arrayw = np.array([12,40,20,40,12,40,50,80,12,24,12,7])
valorw = np.array([12])
arrayT = np.setdiff1d(arrayw,valorw)
print(arrayT)

