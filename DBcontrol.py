# Файл взаимодействия с БД

import sqlite3
from turtledemo.penrose import inflatedart

conn = sqlite3.connect('Igrarium.db')
cur = conn.cursor()

# cur.execute(
#     'CREATE TABLE if NOT EXISTS users (TgId int,'
#     'name varchar(50),'
#     'sname varchar(50),'
#     'inst varchar(5),'
#     'faculty varchar(60),'
#     'course int,'
#     'role varchar(10))')
# conn.commit()
# cur.close()

data = {'name': "fdfdsfdsf", 'sname': '32425425'}

class RegistrDB:
    def sentID(telegramID):
        cur = conn.cursor()
        cur.execute('INSERT INTO users (TgId) VALUES (?)', (telegramID,))
        conn.commit()
        cur.close()


    def sentName(uid, Uname):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (name) = ? WHERE TgId = ?', (Uname, uid))
        conn.commit()
        cur.close()


    def sentSName(uid, SirName):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (sname) = ? WHERE TgId = ?', (SirName, uid))
        conn.commit()
        cur.close()


    def sentInstitute(uid, institute):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (inst) = ? WHERE TgId = ?', (institute, uid))
        conn.commit()
        cur.close()


    def sentFacult(uid, fac):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (faculty) = ? WHERE TgId = ?', (fac, uid))
        conn.commit()
        cur.close()


    def sentCourse(uid, course):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (course) = ? WHERE TgId = ?', (int(course), uid))
        conn.commit()
        cur.close()

    def FindID(telegramID):
        cur = conn.cursor()
        inf = cur.execute('SELECT * FROM users WHERE TgId = ? ', (telegramID,))
        if inf.fetchone() is None:
            return False
        else:
            return True

    def sentRoleOnId(uid, role):
        cur = conn.cursor()
        cur.execute('UPDATE users SET (role) = ? WHERE TgId = ?', (str(role), uid))
        conn.commit()
        cur.close()


class Meets:
    def CreateMeetData(uid, dat, tStart):
        cur = conn.cursor()
        cur.execute('INSERT INTO meets (TgId, date, tStart) '
                    'VALUES (?, ?, ?)', (uid, dat, tStart))
        conn.commit()
        exchange = cur.execute('SELECT id FROM meets WHERE TgId = ? AND date = ?', (uid, dat)).fetchall()
        conn.commit()
        cur.close()
        inf = [x[0] for x in exchange]
        return inf

    def CloseMeetData(wrId, tEnd, totTime):
        cur = conn.cursor()
        cur.execute('UPDATE meets SET (tEnd, totTimeSec) = (?, ?) WHERE id = ?', (tEnd, totTime, wrId))
        conn.commit()
        cur.close()




class rassl:
    def getUsersID(role):
        cur = conn.cursor()
        inf = cur.execute('SELECT "TgId", "act" FROM users WHERE role = ?', (role,)).fetchall()
        conn.commit()
        cur.close()
        return inf

    def setActive(uid, act):
        cur = conn.cursor()
        cur.execute('UPDATE users SET act = ? WHERE TgId = ?', (act, uid,))
        conn.commit()
        cur.close()

class Achives:
    def AddAchive(uid, servname):
        cur = conn.cursor()
        cur.execute('INSERT INTO achives (TgId, servName) VALUES (?, ?)', (uid, servname))
        conn.commit()
        cur.close()

    def SerchAchive(uid, ach):
        cur = conn.cursor()
        inf = cur.execute('SELECT * FROM achives WHERE TgId = ?', (uid,)).fetchall()
        conn.commit()
        cur.close()
        k = 0
        res = []
        for k in range(len(inf)):
            res.append(inf[k][2])
            k += 1
        if ach in res:
            return True
        return False

    def coinUpdater(uid, coin):
        cur = conn.cursor()
        curCoin = cur.execute('SELECT coins FROM users WHERE TgId = ?', (uid,)).fetchone()
        conn.commit()
        curCoin += coin
        cur.execute('UPDATE users SET coins = ? WHERE TgId = ?', (curCoin, uid))
        conn.commit()
        cur.close()
        return curCoin

    def meetCount(uid):
        cur = conn.cursor()
        nowMeets = cur.execute('SELECT visits FROM users WHERE TgId = ?', (uid,)).fetchone()[0]
        conn.commit()
        nowMeets += 1
        cur.execute('UPDATE users SET visits = ? WHERE TgId = ?', (nowMeets, uid))
        conn.commit()
        cur.close()
        return nowMeets

    def TechCount(uid):
        cur = conn.cursor()
        nowTech = cur.execute('SELECT Tech FROM users WHERE TgId = ?', (uid,)).fetchone()[0]
        conn.commit()
        nowTech += 1
        cur.execute('UPDATE users SET Tech = ? WHERE TgId = ?', (nowTech, uid))
        conn.commit()
        cur.close()
        return nowTech






class GetData:
    def GetUserInfo(uid):
        cur = conn.cursor()
        cData = cur.execute('SELECT * FROM users WHERE TgId = ?', (uid,)).fetchone()
        inf = {'uid' : cData[0],
               'name' : cData[1],
               'sname' : cData[2],
               'institute' : cData[3],
               'facult' : cData[4],
               'course' : cData[5],
               'role' : cData[6],
               'coins': cData[8],
               'vsit': cData[9],
               'tech': cData[10]}
        conn.commit()
        cur.close()
        return inf


