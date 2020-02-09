import numpy as np
def getCoordCircle(raduis = 30.0, numPoints = 100):
    x = np.linspace(-raduis, raduis, num=round(numPoints/2))
    y1 = np.sqrt(raduis**2-x**2)
    
    pos_half = np.vstack((x,y1))
    neg_half = np.vstack((x[::-1],-1*y1[::-1]))
    coord = np.hstack((pos_half,neg_half))
    return coord.T
def generateXY(R, N):
    np.savetxt("output/raduis{}_numPoints{}.txt".format(round(R),N),getCoordCircle(R,N),fmt='%1.4f')


