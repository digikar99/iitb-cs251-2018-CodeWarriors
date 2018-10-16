#!/usr/bin/python3

import sqlite3

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

cur.execute('''SELECT PLY.player_id,PLY.player_name,
	1.0000000000000000*(SELECT COUNT(BALL_BY_BALL.ball_id) FROM BALL_BY_BALL
			WHERE PLY.player_id=BALL_BY_BALL.striker)/
	(SELECT COUNT(DISTINCT(BALL_BY_BALL.match_id)) FROM BALL_BY_BALL
			WHERE PLY.player_id=BALL_BY_BALL.striker) AS avg_runs
	FROM PLAYER AS PLY 
	WHERE (SELECT COUNT(PLAYER_MATCH.match_id) FROM PLAYER_MATCH
			 WHERE PLAYER_MATCH.player_id=PLY.player_id) <> 0 
			 ORDER BY avg_runs DESC''')

j=cur.fetchall()

if len(j)<=10:
	for i in j:
		print(str(i[0]) + ',' + str(i[1]) +',' + str(i[2]))
else:
	for i in range(9):
		print(str(j[i][0]) + ',' + str(j[i][1]) + ',' + str(j[i][2]))
	i = 9
	while i<len(j) and j[9][2] == j[i][2]:
		print(str(j[i][0]) + ',' + str(j[i][1]) + ',' + str(j[i][2]))
		i+=1
