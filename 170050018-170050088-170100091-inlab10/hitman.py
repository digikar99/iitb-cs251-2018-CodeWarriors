#!/usr/bin/python3

import sqlite3
import sys

mydb=sqlite3.connect('ipl.db')

cur=mydb.cursor()

cur.execute('SELECT PLAYER.player_id , PLAYER.player_name , count(BALL_BY_BALL.runs_scored) AS count1 , \
	(SELECT COUNT(*) FROM BALL_BY_BALL WHERE PLAYER.player_id=BALL_BY_BALL.striker) AS count2 , count1*1.0/NULLIF(count2,0) AS fraction \
	WHERE BALL_BY_BALL.runs_scored=6 \
	GROUP BY PLAYER.player_id ORDER BY fraction DESC')
