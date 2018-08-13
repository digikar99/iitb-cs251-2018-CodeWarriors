#!/usr/bin/python3

import numpy

# Numpy functions allowed to be used:
# deg2rad, rad2deg, trigonometric, slice, transpose,
# normalize and stack operations

# No for-loops allowed

def ang_to_vec(ang):
    ang = numpy.array(ang) # if ang is not a numpy array

    # Resize the ang to a Nx1 matrix.
    # Final result will be a 2xN matrix.

    # Resize ang vector/matrix
    n = 0
    if ang.ndim == 1: # if ang is a vector
        n = ang.shape[0]
    elif ang.ndim == 2:
        if ang.shape[0] == 1:
            n = ang.shape[1]
            ang = ang.transpose()
        else: #ang.shape[1] == 1 or both are 1.
            n = ang.shape[0]

    angRad = numpy.deg2rad(ang)
    sinAng = numpy.sin(angRad)
    cosAng = numpy.cos(angRad)
    vec = numpy.stack([cosAng, sinAng])
    vec = vec.reshape(2,n).transpose()
    #print(vec.shape)
    return vec
    
    
def vec_to_ang(vec):
    vec = numpy.array(vec) # if vec is not a numpy array

    # Need vec to be a 2xN matrix
    if vec.shape[1] == 2: # if vec is Nx2, transpose
        vec = vec.transpose()
    #print(vec)

    # ang will be a Nx1 vector
    cosAng = vec[0]
    angRad = numpy.arccos(vec[0])
    ang = numpy.rad2deg(angRad)
    #print(ang.shape)
    #print(ang)
    return ang

#l = numpy.array([0,30,45,60,90,180])
#print(ang_to_vec(l))
#print(vec_to_ang(ang_to_vec(l)))
