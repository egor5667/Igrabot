import sqlite3

conn = sqlite3.connect('Igrarium.db')
cur = conn.cursor()

cur.execute(
    'CREATE TABLE if NOT EXISTS users (id int auto_increment primary key,'
    'name varchar(50),'
    'sname varchar(50),'
    'inst varchar(5),'
    'faculty varchar(60),'
    'course int)')
conn.commit()
cur.close()

data = {'name': "fdfdsfdsf", 'sname': '32425425'}


async def sent_registData(reg):
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, name, inst, faculty, course) VALUES (?, ?, ?, ?, ?)',
                (reg['name'],
                 reg['sname'], reg['inst'], reg['faculty'], reg['course']))
    conn.commit()
    cur.close()
    conn.close()
