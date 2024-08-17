# Файл взаимодействия с БД

import sqlite3

conn = sqlite3.connect('Igrarium.db')
cur = conn.cursor()

cur.execute(
    'CREATE TABLE if NOT EXISTS users (id int,'
    'name varchar(50),'
    'sname varchar(50),'
    'inst varchar(5),'
    'faculty varchar(60),'
    'course int)')
conn.commit()
cur.close()

data = {'name': "fdfdsfdsf", 'sname': '32425425'}


class RegistrDB:
    async def sentID(telegramID):
        cur = conn.cursor()
        cur.execute('INSERT INTO users (TgId) VALUES (?)', (telegramID))
        conn.commit()
        cur.close()

    async def sentName(uid, Uname):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (name) = ? WHERE TgId = ?', (Uname, uid))
        conn.commit()
        cur.close()

    async def sentName(uid, SirName):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (sname) = ? WHERE TgId = ?', (SirName, uid))
        conn.commit()
        cur.close()

    async def sentInstitute(uid, institute):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (inst) = ? WHERE TgId = ?', (institute, uid))
        conn.commit()
        cur.close()

    async def sentFacult(uid, fac):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (faculty) = ? WHERE TgId = ?', (fac, uid))
        conn.commit()
        cur.close()

    async def sentInstitute(uid, course):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (course) = ? WHERE TgId = ?', (int(course), uid))
        conn.commit()
        cur.close()


