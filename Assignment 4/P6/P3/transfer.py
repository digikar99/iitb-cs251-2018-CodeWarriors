#! /usr/bin/python3
import random
import json
A=random.sample(range(1,1000),100)
def search_low(team,dict):
	low=-1
	for i in A:
		if dict[i]['team']==team:
			if dict[i]['loyalty'] < low or low ==-1:
				low=i
	return low
from string import ascii_uppercase
B=ascii_uppercase
B=list(B)
B=B[:10]
total_transfer=0
dict_j={}
for i in range(0,100):
	dict_j[A[i]]={
	'team' : B[i%10],
	'loyalty' : random.randint(1,10)
	}
f=open("players.json","w")
f.write(json.dumps(dict_j))
f.close()
f=open("players.json","r+")
new_dict=json.load(f)
new_dict=dict_j
g=open("transfer.txt","r")
print("Transfer Complete")
for i in g.readlines():
	i=i.split()
	try:
		if i[0] in B:
			if int(i[1]) in new_dict:
				if int(new_dict[int(i[1])]['loyalty']) > 7:
					raise ValueError("Try another transfer(Player Too Loyal)")
				else:
					j=search_low(i[0],new_dict)
					temp=new_dict[j]['loyalty']
					if not new_dict[int(i[1])]['team']==i[0]:
						total_transfer+=1
						new_dict[j]={
						'team' : new_dict[int(i[1])]['team'],
						'loyalty' : temp
						}
						temp = new_dict[int(i[1])]['loyalty']
						new_dict[int(i[1])]={
						'team' : str(i[0]),
						'loyalty' : temp
						}
			else:
				raise ValueError("Try another transfer(Wrong Player Number)")
		else:
			raise ZeroDivisionError()
	except ValueError as e:
		print(e)
	except ZeroDivisionError:
		print("Try another transfer(Wrong Team Name)")
print("Total Transfers = " + str(total_transfer))
f.seek(0)
f.write(json.dumps(new_dict))
f.close()