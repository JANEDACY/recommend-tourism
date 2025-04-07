from common.getData import *
import random
def getAllTravelByTitle(traveTitleList):
    resultList = []
    for title in traveTitleList:
        for travel in getAllTravelData():
            if title == travel.title:resultList.append(travel)
    return resultList

def getRandomTravel():
    travelList = getAllTravelData()
    maxLen = len(travelList)
    resultList = []
    for i in range(10):
        randomNum = random.randint(0,maxLen)
        resultList.append(travelList[randomNum])
    return resultList