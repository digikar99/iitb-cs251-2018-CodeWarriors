#! /usr/bin/python3

import sqlite3
import csv

log_level = 0

conn = sqlite3.connect('ipl.db')
cur = conn.cursor()

to_exec = {
    
    'TEAM': "(team_id int, team_name text, primary key(team_id) )",
    
    'MATCH': "(match_id int, season_year int, team1 int, team2 int, "
    + "battedfirst int, battedsecond int, venue_name text, "
    + "city_name text, country_name text, toss_winner text, "
    + "match_winner text, toss_name text, win_type int, "
    + "man_of_match int, win_margin int, primary key(match_id), "
    + "foreign key (team1) references TEAM(team_id), "
    + "foreign key (team2) references TEAM(team_id), "
    + "foreign key (battedfirst) references TEAM(team_id), "
    + "foreign key (battedsecond) references TEAM(team_id) ) ",

    'PLAYER': "(player_id int, player_name text, dob timestamp, "
    + "batting_hand text, bowling_skill text, country_name text, "
    + "primary key (player_id) )",
    
    'PLAYER_MATCH': "(playermatch_key int, match_id int, "
    + "player_id int, batting_hand text, bowling_skill, "
    + "role_desc text, team_id int, primary key (playermatch_key), "
    + "foreign key (match_id) references MATCH(match_id), "
    + "foreign key (player_id) references PLAYER(player_id), "
    + "foreign key (team_id) references TEAM(team_id) )",

    'BALL_BY_BALL': "(match_id int, innings_no int, over_id int, "
    + "ball_id int, striker_batting_position int, "
    + "runs_scored int, extra_runs int, out_type text, "
    + "striker int, non_striker int, bowler int, "
    + "primary key (match_id, innings_no, over_id, ball_id), "
    + "foreign key (match_id) references MATCH(match_id), "
    + "foreign key (striker) references PLAYER(player_id), "
    + "foreign key (non_striker) references PLAYER(player_id), "
    + "foreign key (bowler) references PLAYER(player_id) )"
}

# NOTE: Maintain consistency between the above in this
# file and insert.py

def create_sql_table(table_name):
    cmd = "CREATE TABLE " + table_name + to_exec[table_name]
    if (log_level>0):
         print("Creating "+ table_name + " in database ipl.db...\n:", cmd)
         print()
    cur.execute(cmd)
        
for key in to_exec:
    create_sql_table(key)

conn.commit()
conn.close()
