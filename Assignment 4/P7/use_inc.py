#!/usr/bin/python3

import sys
import numpy
import inc


in_file = sys.argv[1]
out_file = sys.argv[2]
a2v = int(sys.argv[3])

if a2v == 1:
    try:
        ang = numpy.loadtxt(in_file, dtype='float', delimiter=',')
        #print(ang)
        vec = inc.ang_to_vec(ang)
        numpy.savetxt(out_file, vec, delimiter=',', fmt='%1.6f')
    except:
        exit(1)
elif a2v == 0:
    try:
        vec = numpy.loadtxt(in_file, dtype='float', delimiter=',')
        ang = inc.vec_to_ang(vec)
        numpy.savetxt(out_file, ang, delimiter=',', fmt='%1.2f')
    except:
        exit(1)
