import sqlite3

conn = sqlite3.connect('Igrarium.db')
cur = conn.cursor()

cur.execute('CREATE TALE if NOT EXISTS users (id int auto_increment primary key, name varchar(50), password varchar(50))')
conn.commit()
cur.close()
conn.close()

async def sent_registData():
    pass
