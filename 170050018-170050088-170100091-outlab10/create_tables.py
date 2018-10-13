#! /usr/bin/python3

import sqlite3
import csv

log_level = 1

conn = sqlite3.connect('ipl.db')
cur = conn.cursor()

typeof = dict()
typeof['dob'] = 'timestamp'
typeof['bowling_skill'] = 'text'
typeof['win_type'] = 'text'
typeof['batting_hand'] = 'text'
typeof['role_desc'] = 'text'
typeof['out_type'] = 'text'
typeof['toss_winner'] = 'text'
typeof['match_winner'] = 'text'

def gto(field_name): # get_type_of
    if field_name in typeof:
        return typeof[field_name]
    elif 'name' in field_name:
        return 'text'
    else:
        return 'int'

def create_sql_table(file_name, table_name):
    with open(file_name, 'r') as f:
        r = csv.reader(f)
        header = next(r)
        l = len(header)
        init_cmd = "CREATE TABLE " + table_name
        arg_list = []
        for fname in header:
            # fname - field name
            # gto - get_type_of
            arg_list.append(fname + " " + gto(fname))
        to_exec = init_cmd + "(" + ", ".join(arg_list) + ")"
        if (log_level>0):
            print("Executing "+ to_exec + " on database ipl.db...")
        cur.execute(to_exec)
        
for fname in ['team', 'player','match','player_match','ball_by_ball']:
    create_sql_table(fname+".csv", fname.upper())
conn.commit()
conn.close()
