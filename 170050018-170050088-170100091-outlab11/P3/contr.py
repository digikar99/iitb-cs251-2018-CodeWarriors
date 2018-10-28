import csv
import matplotlib.pyplot as plt
import numpy as np
import math
r_li=[]
with open('survey_data.csv','r') as csvfile:
	filereader=csv.reader(csvfile)
	head=next(filereader)
	for i in range(len(head)-1):
		r_li.append([0,0,0,0])
	for row in filereader:
		m=row[0]
		row=row[1:]
		for i,j in enumerate(row):
			if j=='Essential':
				r_li[i][0]+=1;
			elif j=='Nice to have':
				r_li[i][1]+=1
			elif j=='Dont care one way or another':
				r_li[i][2]+=1
			elif j=='Utterly useless':
				r_li[i][3]+=1
			else:
				print("error at",m,i,j)


N=len(head)-1

ind = np.arange(N)

pl_list=[]
for i in range(len(r_li[0])):
	a=[]
	for j in (r_li):
		a.append(j[i])
	pl_list.append(a)

def log2(x):
	return math.log(x,2)

def entropy(li):
	total=0;
	for i in li:
		total+=i
	j=0;
	for i in li:
		if(i==0):
			pass
		else:
			j+=(i/total)*log2(i/total)
	if(j==0):
		return j;
	else:
		return -j;

re_list=[]

for j,i in enumerate(r_li):
	re_list.append([head[1+j],entropy(i)])

l2=[];
width=0.50

for i in sorted(re_list,key=lambda x: x[1]):
	l2.append(i)


l3=[]
for i in l2:
	l3.append(i[1])

p1 = plt.bar(ind,l3,width, color='b')
topics=[]

for i in l2:
	topics.append(i[0])
plt.ylabel('entropy')
plt.xlabel('Topics')

plt.xticks(ind, topics,rotation='vertical')

plt.savefig('contr.png',bbox_inches='tight')