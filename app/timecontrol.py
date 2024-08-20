import datetime

def TimeCount(stTime, finTime):
    delta = finTime - stTime
    return delta.total_seconds()

