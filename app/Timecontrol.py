from datetime import datetime
from time import sleep, strptime


def TimeCount(stTime, finTime):
    delta = finTime - stTime
    return int(delta.total_seconds())

def DateCount(stDate, finDate):
    s = datetime.strptime(stDate, "%d.%m.%Y")
    f = datetime.strptime(finDate, "%d.%m.%Y")
    return int((f-s).days)

def Streek(oneDay, twoDay):
    if DateCount(oneDay, twoDay) <=8:
        return True
    return False