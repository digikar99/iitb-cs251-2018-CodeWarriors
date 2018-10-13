 
import sqlite3
import csv

conn = sqlite3.connect('pokedex.db')
pokeconn = conn.cursor()

pokeconn.execute('''CREATE TABLE POKEMON
(id int, identifier varchar(50), species_id int, height int, weight int, base_experience int, order1 int, is_default int)''')

pokeconn.execute('''CREATE TABLE ABILITIES
(id int, identifier int, generation_id int, is_main_series int)''')

pokeconn.execute('''CREATE TABLE POKEMON_ABILITIES
(pokemon_id int, ability_id int, is_hidden int, slot int)''')

conn.commit()
conn.close()

