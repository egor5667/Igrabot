from app import Timecontrol
from datetime import datetime
import DBcontrol

global meetIds
meetIds = []

def sendMeetStart(uidList):
    for i in range(len(uidList)):
        global startTime
        startTime = datetime.now().strftime('%H:%M')
        meetIds.append(DBcontrol.Meets.CreateMeetData(uidList[i],
                                            datetime.now().strftime("%d.%m.%Y"),
                                            datetime.now().strftime("%H:%M")))
        DBcontrol.Achives.meetCount(uidList[i])
    flat_list = [item for sublist in meetIds for item in sublist]
    return flat_list

def sendMeetFin(meetIds, totTime):
    for i in range(len(meetIds)):
        endTime = datetime.now().strftime('%H:%M')
        DBcontrol.Meets.CloseMeetData(meetIds[i], endTime, totTime)













