import numpy as np

array = np.loadtxt('ndArrray.txt')
sec_array = np.ones(shape=(3, 3))
np.savetxt('2array.txt',array*sec_array)