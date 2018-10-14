#!/usr/bin/python3

import sqlite3

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

cur.execute('''SELECT PLAYER.player_id ,PLAYER.player_name,
            (SELECT COUNT(*) FROM BALL_BY_BALL 
                WHERE BALL_BY_BALL.runs_scored=6 AND PLAYER.player_id=BALL_BY_BALL.striker) AS count1,
            (SELECT COUNT(*) FROM BALL_BY_BALL WHERE PLAYER.player_id=BALL_BY_BALL.striker) AS count2,
                1.00000000000000000*(SELECT COUNT(*) FROM BALL_BY_BALL WHERE BALL_BY_BALL.runs_scored=6 
                        AND PLAYER.player_id=BALL_BY_BALL.striker)/
                (SELECT COUNT(*) FROM BALL_BY_BALL WHERE PLAYER.player_id=BALL_BY_BALL.striker) AS fraction
                FROM PLAYER ORDER BY fraction DESC''')

for i in cur.fetchall():
    for j in i[:-1]:
        print(j,end=',')
    print(i[-1])
