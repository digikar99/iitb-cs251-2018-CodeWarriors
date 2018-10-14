#!/usr/bin/python3

import sqlite3

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

arguments=list(input())

no_arguments=[2,6,15,7,11]

table_no=int(arguments[0])

for i in range(no_arguments[table_no-1]):
	arguments.append(input())

TABLES=["TEAM","PLAYER","MATCH","PLAYER_MATCH","BALL_BY_BALL"]

table=TABLES[table_no-1]

values=tuple(arguments[1:])

statement="INSERT INTO " + table + " VALUES " + str(values) 

cur.execute(statement)

mydb.commit()

mydb.close()
