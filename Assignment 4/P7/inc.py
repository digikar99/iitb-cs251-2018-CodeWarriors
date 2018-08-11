#!/usr/bin/python3

import numpy

# Numpy functions allowed to be used:
# deg2rad, rad2deg, trigonometric, slice, transpose,
# normalize and stack operations

# No for-loops allowed

def ang_to_vec(ang):
    angRad = numpy.deg2rad(ang)
    sinAng = numpy.sin(angRad)
    cosAng = numpy.cos(angRad)
    vec = numpy.stack([cosAng, sinAng])
#    print(vec.shape)
    return vec
    
    
def vec_to_ang(vec):
    cosAng = vec[0]
    angRad = numpy.arccos(vec[0])
    ang = numpy.rad2deg(angRad)
    return ang

# l = [0,30,45,60,90,180]
# print(ang_to_vec(l))
# print(vec_to_ang(ang_to_vec(l)))
