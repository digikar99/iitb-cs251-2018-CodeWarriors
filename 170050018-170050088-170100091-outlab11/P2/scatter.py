import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
import csv

x=[]
y=[]
z=[]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


with open('3dpd.out') as f:
	filereader=csv.reader(f)
	for row in filereader:
		x.append(float(row[0]))
		y.append(float(row[1]))
		z.append(float(row[2]))

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.scatter(x,y,z)

plt.show()