#!/usr/bin/python3

import csv
import sqlite3 as sq
import os

if os.path.exists('cse_students.sqlite'):
    os.remove('cse_students.sqlite')

row_num = 0
n_students = []
student_type = []
with open('count.csv') as cnt:
    reader = csv.reader(cnt, delimiter=' ', skipinitialspace=True)
    for row in reader:
        if row_num != 0:
            n_students.append(int(row[len(row)-1]))
            student_type.append(' '.join(row[:(len(row)-1)]))
        row_num += 1

#print(n_students)
#print(student_type)

conn = sq.connect('cse_students.sqlite')
cur = conn.cursor()
cur.execute("CREATE TABLE t ([Category Name], [No. of students]);")
for s,n in zip(student_type, n_students):
    cur.execute("INSERT INTO t ([Category Name], [No. of students]) VALUES (?,?)", (s,n))

conn.commit()

cur.execute("SELECT [Category Name], [No. of students] FROM t")

#for row in cur:
#    print('{0}:{1}'.format(row[0],row[1]))

def returnCount(cat_name):
    #q = input("Enter Category Name: ")
    cur.execute("SELECT [No. of students] FROM t WHERE [Category Name]=?", (cat_name,))
    res = cur.fetchall()
    print(res[0][0])

cat_name = input("Enter Category Name: ")
returnCount(cat_name)
conn.close()
