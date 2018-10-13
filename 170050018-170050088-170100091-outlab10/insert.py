#!/usr/bin/python3

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

# NOTE: Maintain consistency between the above in this
# file and create_table.py

def insert_table(file_name, table_name):
    with open(file_name, 'r') as f:
        r = csv.reader(f)
        header = next(r)
        init_cmd = "INSERT INTO " + table_name + " VALUES "
        arg_list = []
        for row in r:
            temp = []
            for i in range(len(header)):
                # gto - get type of
                if gto(header[i]) == 'int':
                    temp.append(str(row[i]))
                else: # gto is 'text'
                    temp.append("'"+str(row[i])+"'")
            # arg_list.append(", ".join(temp))
            # if (log_level > 1):
              #  print(temp)
            to_exec = init_cmd + "(" + ", ".join(temp) + ")"
            if (log_level > 1):
                print("Executing", to_exec)
            cur.execute(to_exec)
        conn.commit()

for fname in ['team', 'player','match','player_match','ball_by_ball']:
    insert_table(fname+".csv", fname.upper())
conn.commit()
conn.close()
        
