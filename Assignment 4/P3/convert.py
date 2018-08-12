#! /usr/bin/python3
import numpy as np
my_data = np.genfromtxt('info_day.csv',delimiter=','\
	,skip_header=1,usecols=range(1,5),unpack=True)
f=open('info_day.csv','r')
words=[]
for line in f.readlines():
	words.append(line.split(',')[0])
words=words[1:]
f.seek(0)
f_row=f.readline()
for i in range(7):
	my_data[0][i]=my_data[0][i]*1.8+32
ofile=open('transformed.csv','w')
ofile.write(f_row)
my_data=my_data.T
for ind,i in enumerate(words):
	ofile.write(i + "," + ','.join(map(str,my_data[ind])) + "\n")
