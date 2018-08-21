#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests

start_link = "https://www.cse.iitb.ac.in/page222"
full_pg = requests.get(start_link)
soupified_pg = bs(full_pg.text, 'lxml')
links = soupified_pg.select('div.mpart')[0].find_all('a')

n_students = []
student_type = []

for a in links:
    full_link = start_link + a.get('href')
    sub_pg = requests.get(full_link)
    sp_pg = bs(sub_pg.text, 'lxml')
    mpart = sp_pg.select('div.mpart')[0]
    n_students.append(int(len(mpart.find_all('a')) / 2))
    student_type.append(a.text)

with open('count.csv', 'w') as cnt:
    cnt.write('{0:20}{1}\n'.format('Category Name', 'No. of students'))
    for s,n in zip(student_type, n_students):
        cnt.write('{0:20}{1}\n'.format(s,str(n)))


    


