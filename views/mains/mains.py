from flask import Flask,session,render_template,redirect,Blueprint,request
from common.getData import *
from common.recommdation import *
from common.getRecommendationData import *

import time
# from utils.errorResponse import errorResponse
ap = Blueprint('mains',__name__,url_prefix='/mains',template_folder='templates')
@ap.route('/home')
def home():
    userInfo = session.get('user')
    mapData = getChinaMap()
    travelCountData = getTravelCount()
    userCountData = getUserlCount()

    commentsTitle,commentsMax = getTravelMaxCommentCount()
    shengfenname,maxcount = getMaxProvincetravelCount()



    return render_template('index.html', userInfo=userInfo,mapData=mapData
                           , travelCountData=travelCountData,commentsTitle=commentsTitle
                           , commentsMax=commentsMax,shengfenname=shengfenname
                           , maxcount=maxcount,userCountData=userCountData)

@ap.route('/datatable')
def datatable():
    userInfo = session.get('user')
    tableData=getAllTravelInfoData()
    return render_template('tableData.html',
                           userInfo=userInfo,
                           talbeData=tableData,

                           )
@ap.route('/city')
def city():
    userInfo = session.get('user')
    xData, yData =cityCharDataOne()
    return render_template('city.html',
                           userInfo=userInfo,
                           xData=xData,
                           yData=yData,
                           )
@ap.route('/level')
def level():
    userInfo = session.get('user')
    levelData =levelCountData()
    return render_template('level.html',
                           userInfo=userInfo,
                           levelData=levelData,
                           )


@ap.route('/price')
def price():
    userInfo = session.get('user')
    xData,yData=getPriceCharDataOne()
    legendData,zhekouData=getZheKouData()

    # legend2Data priceData
    return render_template('price.html',
                           userInfo=userInfo,
                           xData=xData,
                           yData=yData,
                           zhekouData=zhekouData,legendData=legendData,
                           )
@ap.route('/rate')
def rate():
    userInfo = session.get('user')
    talbeData=getAllTravelInfoData()
    return render_template('tableData.html',
                           userInfo=userInfo,
                           talbeData=talbeData,

                           )
@ap.route('/sale')
def sale():
    userInfo = session.get('user')
    xData,yData=getSaleCountData()
    return render_template('tableData.html',
                           userInfo=userInfo,
                           xData=xData,
                           yData=yData,
                           )
@ap.route('/hot')
def hot():
    userInfo = session.get('user')
    talbeData=getAllTravelInfoData()
    return render_template('tableData.html',
                           userInfo=userInfo,
                           talbeData=talbeData,

                           )
@ap.route('/commentdata')
def commentdata():
    userInfo = session.get('user')
    xData, yData =getCommentstime()
    x2Data, y2Data =getCommentstnum()

    return render_template('commentdata.html',
                           userInfo=userInfo,
                           xData=xData,
                           yData=yData,
                           x2Data=x2Data,
                           y2Data=y2Data,
                           )



@ap.route('/addComments/<id>/',methods=['GET','POST'])
def addComments(id):
    userInfo = session.get('user')
    travelInfo =getTravelById(id)
    if request.method == 'POST':
        print('POSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOST')
        addCommentss({
            'id':int(id),
            'rate':int(request.form['rate']),
            'content':request.form['content'],
            'userInfo':userInfo,
            'travelInfo':travelInfo
        })
        return redirect('/mains/datatable')
    return render_template('addComments.html',
                           userInfo=userInfo,
                           travelInfo=travelInfo,
                           id=id
)
@ap.route('/recommendation',methods=['GET','POST'])
def recommendation():
    userInfo = session.get('user')
    try:
        user_ratings = getUser_ratings()
        print(user_ratings)
        recommended_items = user_bases_collaborative_filtering(userInfo['id'], user_ratings)
        print(recommended_items)
        resultDataList =getAllTravelByTitle(recommended_items)
    except:
        resultDataList =getRandomTravel()
    if resultDataList is None:
        resultDataList = getRandomTravel()
    print(resultDataList)

    return render_template('recommendation.html',
                           userInfo=userInfo,
                           resultDataList=resultDataList,
)


@ap.route('/person',methods=['GET','POST'])
def person():
    userInfo = session.get('user')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sex = request.form['sex']
        address = request.form['address']
        textarea = request.form['textarea']
        createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updatePerson({
            'username':username,
            'password':password,
            'sex':sex,
            'address': address,
            'id':userInfo['id'],
            'textarea': textarea,
            'createTime': createTime,
        })
        session['user'] = {
            'username':username,
            'password':password,
            'sex':sex,
            'address': address,
            'id':userInfo['id'],
            'textarea': textarea,
            'createTime': createTime,
        }
        return redirect('/mains/home')
    return render_template('person.html',
                           userInfo=userInfo,
                           )
import  os
import  datetime
basedir = os.path.abspath(os.path.dirname(__file__)).split('views')[0]