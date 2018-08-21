#! /usr/bin/python3

import numpy as np
my_data = np.genfromtxt('info_day.csv',delimiter=','\
	,skip_header=1,usecols=range(1,5),unpack=True)
print("\"Field\",\"Mean\",\"Std.Dev\"")
f_row=open('info_day.csv','rU')
read_lines=f_row.readlines()
words=read_lines[0].split(',')
words= [i.replace('"', '') for i in words[1:]]
words= [i.replace('\n', '') for i in words]
for ind,i in enumerate(words):
	print(i + "," + str(np.mean(my_data[ind])) +\
	"," + str(np.std(my_data[ind])) )
