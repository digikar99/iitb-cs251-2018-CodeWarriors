import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
import csv

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def colorcode(x,y,z,a,b,c):
	return a*z+b*(x*x+y*y)+c>=0

a=1
b=1
c=-3.5
with open('3dpd.out') as f:
	filereader=csv.reader(f)
	for row in filereader:
		x=float(row[0])
		y=float(row[1])
		z=float(row[2])
		if colorcode(x,y,z,a,b,c):
			ax.scatter(x,y,z,c='r')
		else:
			ax.scatter(x,y,z,c='b')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
