import csv
import matplotlib.pyplot as plt
import numpy as np
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

p1 = plt.bar(ind, pl_list[0],color='r')
p2 = plt.bar(ind, pl_list[1],bottom=pl_list[0],color='b')
p3 = plt.bar(ind, pl_list[2],bottom=np.array(pl_list[1])+np.array(pl_list[0]),color='g')
p4 = plt.bar(ind, pl_list[3],bottom=np.array(pl_list[1])+np.array(pl_list[0])\
 + np.array(pl_list[2]) , color='c')


topics=[]

for i in head[1:]:
	topics.append(i)

plt.xticks(ind, topics,rotation='vertical')
plt.legend((p1[0], p2[0],p3[0],p4[0]), ('Essential', 'Nice to have'\
	,'Dont care one way or another','Utterly useless'))
plt.ylabel('Opinions')
plt.xlabel('Topics')
plt.savefig('hists.png',bbox_inches='tight')
