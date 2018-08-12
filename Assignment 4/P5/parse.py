#! /usr/bin/python3
import json

file1=open('infinity_stones.json','r')
data=json.load(file1)
file1.close()

file2=open("infinity_stones.csv","w")
file2.write("| Stone Name | Stone Color | Containment Unit | \n")
for ele in data["Infinity Stones"]:
   file2.write("| "+ele["Stone Name"]+" | "+ele["Stone Color"]+" | "+ele["Containment Unit"]+" |"+"\n" )
