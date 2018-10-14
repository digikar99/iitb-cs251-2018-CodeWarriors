#!/usr/bin/python3

import sqlite3
import sys

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

arguments=sys.argv[1].split("\n")

table_no=int(arguments[0])

TABLES=["TEAM","PLAYER","MATCH","PLAYER_MATCH","BALL_BY_BALL"]

table=TABLES[table_no-1]

values=tuple(arguments[1:])

statement="INSERT INTO " + table + " VALUES " + str(values) 

cur.execute(statement)

mydb.commit()

mydb.close()
