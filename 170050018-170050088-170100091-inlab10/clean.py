import sqlite3

pokeconn = sqlite3.connect('pokedex.db')
pokecur = pokeconn.cursor()

pokecur.execute('''DELETE FROM POKEMON WHERE identifier LIKE "rogue%"''')
pokeconn.commit()
pokecur.close()

