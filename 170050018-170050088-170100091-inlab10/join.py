#!/usr/bin/python3
import sqlite3

mydb=sqlite3.connect('pokedex.db')

cur=mydb.cursor()

cur.execute('''SELECT POKEMON_ABILITIES.pokemon_id,POKEMON_ABILITIES.ability_id,
	POKEMON.identifier,ABILITIES.identifier
	FROM POKEMON_ABILITIES
	INNER JOIN POKEMON ON POKEMON.id=POKEMON_ABILITIES.pokemon_id
	INNER JOIN ABILITIES ON ABILITIES.id=POKEMON_ABILITIES.ability_id
	ORDER BY POKEMON.identifier''')
dict={}
for i in cur.fetchall():
	if i[2] in dict.keys():
		dict[i[2]]=str(i[3])+','
	else:
		dict[i[2]]=str(i[3])+','

for k in sorted(dict):
	print(str(k) + '=[' + dict[k][:-1] + ']')

