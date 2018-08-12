#! /usr/bin/python3
import numpy as np
day_data = np.genfromtxt('info_day.csv',delimiter=','\
	,skip_header=1,usecols=range(1,5),unpack=True)
night_data = np.genfromtxt('info_night.csv',delimiter=','\
	,skip_header=1,usecols=range(1,5),unpack=True)
f_day=open('info_day.csv','r')
f_night=open('info_night.csv','r')
words=f_day.readline().split(",")
words= [i.replace('"', '') for i in words]
words= [i.replace('\n', '') for i in words]
ofile=open('info_combine.csv','w')
ofile.write( "\""+ str(words[0]) + "\"")
for i in words[1:]:
	ofile.write( "," + "\"" + str(i) + "(Day)\"" + "," \
		+ "\"" + str(i) + "(Night)\"")
ofile.write("\n")
words=[]
for line in f_day.readlines():
	words.append(line.split(',')[0])
for ind,i in enumerate(words):
	merge_value=[]
	for j in range(4):
		merge_value.append(day_data[j][ind])
		merge_value.append(night_data[j][ind])
	ofile.write(i + ","+ ','.join(map(str,merge_value)) +"\n" )
