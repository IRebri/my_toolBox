import numpy as np
def my20(*kids):
    rand_A = np.random.randint(0,21, size=(1000,2))
    A_sum_mus = np.zeros((1000,4))
    A_sum_mus[:,:-2] = rand_A
    A_sum_mus[:,2] = A_sum_mus[:,0] + A_sum_mus[:,1]
    A_sum_mus[:,3] = A_sum_mus[:,0] - A_sum_mus[:,1]
    var = A_sum_mus[(A_sum_mus[:,3]>0) & (A_sum_mus[:,2]<20)]

    return var[:20,:]
def one_file(my_name = "Nazar.txt"):
    x = my20().astype(int)
    y = my20().astype(int)
    f = open("{0}".format(my_name), "w+")
    f.write('\t\t\t\t <, =, >    \t\t    <, =, > \n')
    for k in range(20):
        i = x[np.random.randint(20)]
        j = y[np.random.randint(20)]
        f.write('{0} + {1} = \t {2} - {3} = \t {4}    {5}  \t\t {6} - {7}    {8} + {9}  \n'.
                    format(i[0], i[1], j[0], j[1], i[0], i[1], i[0], i[1], j[0], j[1]))
#         f.write('{0} + {1} = \t {3} <> {2}  \t {0} - {1} =\n'.format(int(i[0]), int(i[1]), int(i[2]), int(i[3])))
# for i in x:
    f.close()


for i in range(10):
    one_file("Nazar{}.txt".format(i))