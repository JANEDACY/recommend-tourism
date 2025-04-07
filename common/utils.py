from pymysql import *
import time
conn = connect(host='localhost',port=3306,user='root',password='root',database='flask_lvyou2')
cursor = conn.cursor()

def db(sql,params,type="no_select"):
    params = tuple(params)
    cursor.execute(sql,params)
    # 阻拦每一次的请求
    conn.ping(reconnect=True)
    if type != 'no_select':
        data_list = cursor.fetchall()
        conn.commit()
        return data_list
    else:
        conn.commit()
def getNowTime():
    timeFormat = time.localtime()
    year = timeFormat.tm_year
    mon = timeFormat.tm_mon
    day = timeFormat.tm_mday
    return year, mon, day