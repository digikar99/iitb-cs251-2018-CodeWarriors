import sqlite3
mydb = sqlite3.connect('pokedex.db')
c=mydb.cursor()
c.execute('''SELECT identifier FROM POKEMON ORDER BY base_experience DESC LIMIT 3''')
l = c.fetchall()
for item in l:
    print(item[0])
mydb.close()
