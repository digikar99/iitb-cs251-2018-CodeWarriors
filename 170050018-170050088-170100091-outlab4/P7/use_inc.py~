#!/usr/bin/python3

import sys
import numpy
import inc


in_file = sys.argv[1]
out_file = sys.argv[2]
a2v = int(sys.argv[3])

if a2v == 1:
    try:
        ang = numpy.loadtxt(in_file, delimiter=',')
        #print(ang)
        vec = inc.ang_to_vec(ang)
        #print("Saving ",vec,"...")
        numpy.savetxt(out_file, vec, delimiter=',')
    except:
        exit(1)
elif a2v == 0:
    try:
        vec = numpy.loadtxt(in_file, delimiter=',')
        ang = inc.vec_to_ang(vec)
        numpy.savetxt(out_file, ang, delimiter=',')
    except:
        exit(1)
