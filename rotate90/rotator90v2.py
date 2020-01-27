import glob
import numpy as np

input_list=glob.glob('input/*.txt')

for filename in input_list:
    a = np.loadtxt(filename)
    a90 = np.transpose(np.rot90(a))
    a180 = np.transpose(np.rot90(a90))
    a270 = np.transpose(np.rot90(a180))
    np.savetxt("output90/"+filename[6:], a90)
    np.savetxt("output180/"+filename[6:], a180)
    np.savetxt("output270/"+filename[6:], a270)