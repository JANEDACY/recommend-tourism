from flask import Flask, session, request, redirect, render_template
import re
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret_key?'
app.permanent_session_lifetime = timedelta(minutes=30)  # **会话有效期30分钟**

# 注册蓝图
from views.user import user
from views.mains import mains
app.register_blueprint(mains.ap)
app.register_blueprint(user.ub)

@app.route('/')
def hello_world():
    return session.clear()

# 没有注册的路由，进入 404 页面
@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')

# **路由守卫：检查会话超时**
@app.before_request
def before_request():
    pat = re.compile(r'^/static')
    if re.search(pat, request.path):
        return
    elif request.path in ['/user/login', '/user/register']:
        return
    elif session.get('user'):
        session.modified = True  # **刷新 session 过期时间**
        return
    return redirect('/user/login')

if __name__ == '__main__':
    app.run()