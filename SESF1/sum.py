import numpy as np
import math


def SF(image,i,j,m,n):
    k = m*n
    rf = image[i*m:(i+1)*m,j*n+1:(j+1)*n]-image[i*m:(i+1)*m,j*n:(j+1)*n-1]
    cf = image[i*m+1:(i+1)*m,j*n:(j+1)*n]-image[i*m:(i+1)*m-1,j*n:(j+1)*n]

    rf = np.square(rf)
    cf = np.square(cf)

    rf = rf.sum()
    cf = cf.sum()

    sf = math.sqrt((rf+cf)/(m*n))
    return sf





