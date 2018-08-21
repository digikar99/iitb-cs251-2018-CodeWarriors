#! /usr/bin/python3
with open("employees.txt","r") as f:
    for line in f:
        temp=line.split(" ",1)[0]
        print(temp[3:]+temp[0:3])
