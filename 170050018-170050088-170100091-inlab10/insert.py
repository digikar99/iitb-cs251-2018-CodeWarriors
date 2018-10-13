import sqlite3
import csv

pokeconn = sqlite3.connect('pokedex.db')
pokecur = pokeconn.cursor()

with open('pokemon.csv') as poke, \
     open('abilities.csv') as abil, \
     open('pokemon_abilities.csv') as pabil:
    reader1 = csv.reader(poke)
    reader2 = csv.reader(abil)
    reader3 = csv.reader(pabil)
    next(reader1)
    next(reader2)
    next(reader3)
    for row in reader1:
        pokecur.execute('''INSERT INTO POKEMON VALUES
        ({0}, '{1}', {2}, {3}, {4}, {5}, {6}, {7})'''\
                        .format(row[0], row[1], row[2],\
                                row[3], row[4], row[5],\
                                row[6], row[7]))
    for row in reader2:
        pokecur.execute('''INSERT INTO ABILITIES VALUES
        ({0}, '{1}', {2}, {3})'''\
                        .format(row[0], row[1], row[2],\
                                row[3]))
    for row in reader3:
        pokecur.execute('''INSERT INTO POKEMON_ABILITIES VALUES
        ({0}, {1}, {2}, {3})'''.format(row[0], row[1], row[2],row[3]))

    pokeconn.commit()

pokecur.close()
    

