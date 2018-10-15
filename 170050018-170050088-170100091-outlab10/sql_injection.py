#!/usr/bin/python3

import sqlite3
import sys

log_level = 0

TABLE = {1:'TEAM', 2:'PLAYER', 3:'MATCH'}
FNAME = {1: 'team_name', 2:'player_name', 3:'match_id'}
table = TABLE[int(sys.argv[1])]
field_name = FNAME[int(sys.argv[1])]

if (log_level>0) and not (sys.argv[2]=='1' or sys.argv[1]=='0'):
    print("Second argument is not 0 or 1:", sys.argv[2], file=sys.stderr)

conn = sqlite3.connect('ipl.db')
cur = conn.cursor()

def executeVulnerably():
    cur.execute("DELETE FROM " + table + " WHERE " + field_name
                + " = '" + sys.argv[3] + "'")


def executeWithCheck():
    cur.execute("delete from " + table + " where " + field_name + " = (?)", (sys.argv[3],))

executeVulnerably() if sys.argv[2]=='0' else executeWithCheck()

conn.commit()
conn.close()
