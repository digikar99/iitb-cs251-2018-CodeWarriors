import sqlite3
mydb = sqlite3.connect('pokedex.db')
c=mydb.cursor()
#print(c.execute("SELECT * FROM ABILITIES WHERE is_main_series=0").fetchall())
c.execute('''UPDATE ABILITIES SET generation_id = 8 WHERE is_main_series=0''')
#print(c.execute("SELECT * FROM ABILITIES WHERE is_main_series=0").fetchall())
mydb.commit()
mydb.close()
