
import numpy as np

a = np.loadtxt('test1.txt')
np.savetxt('test__.txt', np.transpose(np.rot90(a)))