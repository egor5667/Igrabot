from datetime import datetime
from time import sleep


def TimeCount(stTime, finTime):
    delta = finTime - stTime
    return int(delta.total_seconds())


