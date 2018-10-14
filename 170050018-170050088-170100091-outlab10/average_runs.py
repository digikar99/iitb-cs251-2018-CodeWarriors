#!/usr/bin/python3

import sqlite3

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

cur.execute('''SELECT M.venue_name,
            1.00000000000000*(SELECT SUM(runs_scored)
            FROM BALL_BY_BALL,MATCH
            WHERE MATCH.match_id=BALL_BY_BALL.match_id
            AND M.venue_name=MATCH.venue_name) /
            (SELECT COUNT(M.venue_name)) AS count1
            FROM MATCH as M
            WHERE venue_name <> "NULL"
            GROUP BY venue_name ORDER BY count1 DESC''')

for i in cur.fetchall():
    print(str(i[0]) + ','+ str(i[1]))