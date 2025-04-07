from flask import Flask,session,render_template,redirect,Blueprint,request
from common.utils import db
from common.errorResponse import errorResponse
from werkzeug.security import generate_password_hash,check_password_hash
import time
ub = Blueprint('user',__name__,url_prefix='/user',template_folder='templates')
@ub.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        users = db("SELECT * FROM user WHERE username=%s", [request.form['username']], 'select')

        if not users:
            return errorResponse('账号或密码错误')

        user = users[0]
        stored_hashed_password = user[2]  # 获取数据库中存储的哈希密码

        # 使用 `check_password_hash` 进行密码验证
        if not check_password_hash(stored_hashed_password, request.form['password']):
            return errorResponse('账号或密码错误')

        userinfo = {
            'id': user[0],
            'username': user[1],
            'sex': user[3],
            'address': user[4],
            'textarea': user[5],
            'createTime': user[6],
        }
        session['user'] = userinfo
        session.permanent = True  # 让 session 受 `app.permanent_session_lifetime` 控制

        return redirect('/mains/home')
    # else:
        #     def filter_fn(user):
        #         return request.form['username'] in user and request.form['password'] in user and request.form['role'] in user
        #     users = db('select * from user', [], 'select')
        #     login_success = list(filter(filter_fn, users))
        #     if not len(login_success): return errorResponse('账号或密码错误')
        #
        #     userone = db(f"select * from user where username={request.form['username']} and password={request.form['password']}", [], 'select')
        #     print(userone[0])
        #     session['username'] = request.form['username']
        #     session['users'] = userone[0]
        #
        #     return redirect('/student/home')

@ub.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if request.form['password'] != request.form['checkPassword']:
            return errorResponse('两次密码不符合')
        def filter_fn(user):
            return request.form['username'] in user

        users = db('select * from user',[],'select')
        filter_list = list(filter(filter_fn,users))


        if len(filter_list):
            return errorResponse('该用户名已被注册')
        else:
            print(request.form['radio'] + 'sssssssssssssss')
            sex='男'
            if request.form['radio']=='option2':
                sex='女'
                # 使用 `generate_password_hash` 进行密码哈希
            hashed_password = generate_password_hash(request.form['password'])
            time_tuple = time.localtime(time.time())
            db('''
                insert into user(username,password,sex,address,textarea,createTime) values(%s,%s,%s,%s,%s,%s)
            ''',[request.form['username'],hashed_password,sex,request.form['address'],request.form['textarea'],str(time_tuple[0]) + '-' + str(time_tuple[1]) + '-' + str(time_tuple[2])])

        return redirect('/user/login')

@ub.route('/logout')
def logout():
        session.clear()
        return redirect('/user/login')



