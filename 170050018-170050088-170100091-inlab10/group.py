import sqlite3
mydb = sqlite3.connect('pokedex.db')
c=mydb.cursor()
c.execute('''SELECT identifier, species_id, height, weight, base_experience,
order1, is_default
 FROM POKEMON
 GROUP BY species_id​​
 LIMIT 3
''')
