from common.utils import *
from common.data import *

def getAllTravelData():
    travelData = db('select * from travelinfo', [], 'select')
    trs = []
    for i in travelData:
        t = []
        t.append(i[0])
        t.append(i[1])
        t.append(i[2])
        t.append(i[3])
        t.append(i[4])
        t.append(i[5])
        t.append(i[6])
        t.append(i[7])
        t.append(i[8])
        t.append(i[9])
        t.append(i[10])
        t.append(i[11])
        t.append(i[12])
        t.append(i[13])
        t.append(json.loads(i[14]))
        t.append(json.loads(i[15]))
        t.append(i[16])
        t.append(i[17])

        # print(t,'ss')
        # print(tuple(t), 'ss')
        trs.append(tuple(t))

    return trs

def getAllUserData():
    userData = db('select * from user ',[],'select')
    return userData
def getUserDataById():
    userinfo = db('select * from user where id=' + str(id), [], 'select')[0]
    return userinfo
def getTravelCount():
    itemDataList = getAllTravelData()
    print(len(itemDataList))
    return len(itemDataList)
def getUserlCount():
    itemDataList = getAllUserData()
    print(len(itemDataList))
    return len(itemDataList)

def getMaxProvincetravelCount():
    itemDataList=getAllTravelData()
    dataDic = {}
    for i in itemDataList:
        for j in cityList:
            for city in j['city']:
                if city.find(i[5]) != -1:
                    if dataDic.get(j['province'], -1) == -1:
                        dataDic[j['province']] = 1
                    else:
                        dataDic[j['province']] += 1
    maxcount=0
    shengfenname=''
    for key, value in dataDic.items():
        if int(value)>maxcount:
            maxcount=int(value)
            shengfenname=key
    # print(shengfenname,maxcount)
    return shengfenname,maxcount

def getTravelMaxCommentCount():
    itemDataList = getAllTravelData()
    commentsMax = 0
    commentsTitle = ''
    for i in itemDataList:
        if int(i[12]) > commentsMax:
            commentsMax = int(i[12])
            commentsTitle = i[1]
    # print(commentsTitle,commentsMax)
    return commentsTitle,commentsMax
def getChinaMap():
    itemDataList=getAllTravelData()
    dataDic = {}
    for i in itemDataList:
        f=0
        for j in cityList:
            ff = 0
            for city in j['city']:

                if city.find(i[5]) != -1:
                    ff = ff + 1
                    f = 1
                    if dataDic.get(j['province'], -1) == -1:
                        dataDic[j['province']] = 1
                    else:
                        dataDic[j['province']] += 1
            if ff>1:
                print(i[5])
        if f==0:
            print(i[5])

    resutData = []
    a=0
    for key, value in dataDic.items():
        resutData.append({
            'name': key,
            'value': value
        })
        a=a+int(value)
    # print(a)
    # print(resutData)
    return resutData
# getChinaMap()
# getTravelCount()
# getTravelMaxCommentCount()
# getMaxProvincetravelCount()
import  json
def getAllTravelInfoData(province=None):
    if province:
        q="select * from travelinfo where province='"+province+"'"
        # print(q)
        travelList =db(q, [], 'select')
    else:
        travelList =  db('select * from travelinfo', [], 'select')
    trs=[]
    for i in travelList:
        t=[]
        t.append(i[0])
        t.append(i[1])
        t.append(i[2])
        t.append(i[3])
        t.append(i[4])
        t.append(i[5])
        t.append(i[6])
        t.append(i[7])
        t.append( i[8])
        t.append(i[9])
        t.append( i[10])
        t.append( i[11])
        t.append( i[12])
        t.append( i[13])
        t.append( json.loads(i[14]))
        t.append( json.loads(i[15]))
        t.append(i[16])
        t.append(i[17])

        # print(t,'ss')
        # print(tuple(t), 'ss')
        trs.append(tuple(t))

    return trs
# getAllTravelInfoData()


#各城市景点个数
def cityCharDataOne():
    cityDic = {}
    itemDataList=getAllTravelData()
    for travel in itemDataList:
        if cityDic.get(travel[5],-1) == -1:
            cityDic[travel[5]] = 1
        else:
            cityDic[travel[5]] += 1

    return list(cityDic.keys()),list(cityDic.values())
#旅游景点等级情况
def levelCountData():
    cityDic = {}
    itemDataList=getAllTravelData()
    for travel in itemDataList:
        if cityDic.get(travel[2], -1) == -1:
            cityDic[travel[2]] = 1
        else:
            cityDic[travel[2]] += 1
    resultData = []
    for key,value in cityDic.items():
        resultData.append({
            'name':key,
            'value':value
        })
    # print(resultData)
    return resultData
# levelCountData()


#景点价格分析
def getPriceCharDataOne():
    itemDataList=getAllTravelData()
    xData = ['免费','100元以内','200元以内','300元以内','400元以内','500元以内','500元以外']
    yData = [0 for x in range(len(xData))]
    for travel in itemDataList:
        price = float(travel[11])
        if price <= 10:
            yData[0] += 1
        elif price <= 100:
            yData[1] += 1
        elif price <= 200:
            yData[2] += 1
        elif price <= 300:
            yData[3] += 1
        elif price <= 400:
            yData[4] += 1
        elif price <= 500:
            yData[5] += 1
        elif price > 500:
            yData[6] += 1
    # print(xData,yData)
    return xData,yData
# getPriceCharDataOne()
#景点销量分析
def getSaleCountData():
    itemDataList=getAllTravelData()

    xData = [str(x * 300) + '份以内' for x in range(1,15)]
    yData = [0 for x in range(len(xData))]
    for travel in itemDataList:
        saleCount = float(travel[4])
        for x in range(1,15):
            count = x * 300
            if saleCount <= count:
                yData[x - 1] += 1
                break

    return xData,yData
#景点折扣
def getZheKouData():
    startDic = {}
    itemDataList=getAllTravelData()
    for travel in itemDataList:
        if startDic.get(travel[3], -1) == -1:
            startDic[travel[3]] = 1
        else:
            startDic[travel[3]] += 1
    resultData = []
    legendData = []
    for key, value in startDic.items():
        legendData.append( key+'折')
        resultData.append({
            'name': key+'折',
            'value': value
        })
    # print(resultData)
    return legendData,resultData


# getZheKouData()

import  datetime
def getAllCommentsData():

    itemDataList=getAllTravelData()
    commentsList = []
    for travel in itemDataList:
        # print(travel[15])
        for comment in travel[15]:
            commentsList.append(comment)
    # print(commentsList)
    return commentsList

def getCommentstime():
    itemDataList=getAllCommentsData()

    # print(itemDataList)
    xData = []
    def get_list(date):
        return datetime.datetime.strptime(date,'%Y-%m-%d').timestamp()
    for comment in itemDataList:
        xData.append(comment['date'])
    xData = list(set(xData))
    xData = list(sorted(xData,key=lambda x: get_list(x),reverse=True))
    yData = [0 for x in range(len(xData))]
    for comment in itemDataList:
        for index,date in enumerate(xData):
            if comment['date'] == date:
                yData[index] += 1
    # print(xData)
    # print(yData)
    return xData,yData


getCommentstime()


def getCommentstnum():
    travelList = getAllTravelData()
    xData = [str(x * 1000) + '条以内' for x in range(1, 200)]
    yData = [0 for x in range(len(xData))]
    for travel in travelList:
        saleCount = int(travel[12])
        # print(saleCount)
        for x in range(1, 200):
            count = x * 1000
            if saleCount <= count:
                yData[x - 1] += 1
                break
    # print(xData)
    # print(yData)
    return xData, yData


getCommentstnum()






def getTravelById(id):
    q='select * from travelinfo where id='+str(id)
    # print(q)
    travel =  db(q,[],'select')
    i=travel[0]
    t = []
    t.append(i[0])
    t.append(i[1])
    t.append(i[2])
    t.append(i[3])
    t.append(i[4])
    t.append(i[5])
    t.append(i[6])
    t.append(i[7])
    t.append(i[8])
    t.append(i[9])
    t.append(i[10])
    t.append(i[11])
    t.append(i[12])
    t.append(i[13])
    t.append(json.loads(i[14]))
    t.append(json.loads(i[15]))
    t.append(i[16])
    t.append(i[17])

    return t
def addCommentss(commentData):
    # 'author': author,
    # 'content': content,
    # 'date': date,
    # 'score': score
    # authorId
    print(commentData['userInfo'])

    print(commentData['userInfo']['username'])
    print(commentData['userInfo']['id'])
    print(commentData['rate'])
    print(commentData['content'])

    year,month,day = getNowTime()
    travelInfo = commentData['travelInfo']
    f=0
    t=-1
    jj={}
    for index,j in enumerate(travelInfo[15]):
        print(index,j)
        if 'userId' in j:
            if  j['userId']==commentData['userInfo']['id']:

                jj={
                    'author': commentData['userInfo']['username'],
                    'score': commentData['rate'],
                    'content': commentData['content'],
                    'date': str(year) + '-' + str(month) + '-' + str(day),
                    'userId': commentData['userInfo']['id'],
                }
                t=index
                f=1
                break
    print(jj)
    if t!=-1:
        travelInfo[15][t]=jj
    print(travelInfo[15])
    if f==0:
        travelInfo[15].append({
            'author':commentData['userInfo']['username'],
            'score':commentData['rate'],
            'content':commentData['content'],
            'date':str(year) + '-' + str(month) + '-' + str(day),
            'userId':commentData['userInfo']['id'],
        })
    commentsdata = json.dumps(travelInfo[15])
    q="update travelinfo set comments = '"+commentsdata+" 'where id = "+str(travelInfo[0])
    print(q)
    db(q, [], 'no_select')



def updatePerson(persondata):
    username = persondata['username']
    password = persondata['password']
    sex = persondata['sex']
    address = persondata['address']
    textarea = persondata['textarea']
    q="update user set username = '"+username+"',password='"+password+"',sex='" +sex +"',address='" +address+"',textarea='" +textarea+"'where id = "+str( persondata['id'])
    print(q)
    db(q, [], 'no_select')



