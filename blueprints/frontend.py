__all__ = ()

from functools import wraps
from blueprints.utils import flash
from quart import Blueprint
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import send_file
import pymysql
import config
import db
import getdir

frontend = Blueprint('frontend', __name__)


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not session:
            return await flash('error', 'You must be logged in to access that page.', 'login')
        if not session['email']:
            return await flash('error', 'You must be logged in to access that page.', 'login')
        return await func(*args, **kwargs)

    return wrapper


@frontend.route('/home')
@frontend.route('/')
async def index():  # put application's code here
    return await render_template('home.html')


@frontend.route('/s')
async def search():
    if 'name' in request.args:
        searchtext = str(request.args['name'])
        print(searchtext)
        addhtml = db.search(searchtext.lower())
        return await render_template('search2.html', makehtml=addhtml, searchback=searchtext)
    else:
        return await render_template('search2.html', makehtml="", searchback="想玩点儿啥gal？")


@frontend.route('/d')
@login_required
async def detailnull():
    if 'f' and 'n' in request.args:
        froute = str(request.args['f'])
        print(froute)
        fname = str(request.args['n'])
        print(fname)
        ppfile = db.filedetail(froute, fname)
        print(ppfile)
        print(session['email'])
        user_integral = db.getuserintegral(session['email'])
        return await render_template('detail.html', url=config.redirect_url, makehtml=ppfile, dlub=config.alist_home,
                                     user_integral=user_integral)
    else:
        return await render_template('404.html')


@frontend.route('/all')
async def broseroot():
    if 'r' in request.args:
        route = str(request.args['r'])
        if route[:2] == '//':
            route = route[1:]
        ppback = db.getppDir(route)
        return await render_template('all.html', url=config.redirect_url, content=ppback)
    else:
        drivehome = db.gethome()
        return await render_template('all.html', url=config.redirect_url, content=drivehome)


@frontend.route('/all/<id>')
async def brosefolder(id):
    pp = db.getppDir(id)
    return await render_template('all.html', url=config.redirect_url, content=pp)


@frontend.route('/register', methods=['GET', "POST"])
async def register():
    if request.method == 'GET':
        return await render_template('register.html')
    email = (await request.form).get('email')
    uname = (await request.form).get('username')
    passwd = (await request.form).get('passwd')
    code = (await request.form).get('code')
    print(email, uname, passwd, code)
    if email == '' or uname == '' or passwd == '' or code == '':
        return await flash('error', '您需要填写所有信息', 'register')
    stat = db.register(email, uname, passwd, code)
    if stat == 0:
        return await flash('success', '注册成功，在这里登录', 'login')
    if stat == 1:
        return await flash('error', '该邮箱已注册，请直接登录或联系管理员', 'login')
    if stat == 2:
        return await flash('error', '激活码已经过期或不可用', 'register')
    if stat == 3:
        return await flash('error', '激活码不存在', 'register')


@frontend.route('/login', methods=['GET', "POST"])
async def login():
    if request.method == 'GET':
        return await render_template('login.html')
    user = (await request.form).get('email')
    pwd = (await request.form).get('password')
    print(user)
    print(pwd)
    stat = db.checklogin(str(user), str(pwd))
    if stat == 0:
        username, is_admin, is_ban, avatar, uid = db.getuserdata(user)
        print(is_ban)
        print(is_admin)
        print(username)
        print(avatar)
        print(uid)
        if is_ban == 1:
            return await flash('ban', 'Your account has been banned, contact administrator for more information',
                               'login')
        else:
            session['username'] = username
            session['email'] = user
            session['is_admin'] = is_admin
            session['avatar'] = avatar
            session['uid'] = uid
            return await flash('success', '成功登录!', 'home')
    else:
        if stat == 1:
            return await flash('error', 'Password Incorrect', 'login')
        else:
            return await flash('error', 'User does not exist', 'login')


@frontend.route('/forgetpw')
async def forgetpw():
    return await render_template('forgetpw.html')


@frontend.route('/recoverpw')
async def recoverpw():
    return await render_template('recoverpw.html')


@frontend.route('/terms')
async def terms():
    return await render_template('terms.html')


@frontend.route('/logout')
async def logout_():
    del session['username']
    del session['email']
    del session['is_admin']
    del session['avatar']
    return await flash('success', '成功登出!', 'login')


"""
请求下载：
/dl?name=...&route=...&redirect=...
"""


@frontend.route('/dl')
@login_required
async def downloadredirect():
    if 'route' and 'name' in request.args:
        froute = str(request.args['route'])
        fname = str(request.args['name'])
        ppfile = db.filedetail(froute, fname)
        print(session['email'])
        user_integral = db.getuserintegral(session['email'])[0]
        if user_integral < ppfile[0][7]:
            return await flash('error', '积分不足！', 'home')
        downURL = db.downloadredirect(froute, fname, session['email'])
        return await render_template('downloadredirect.html', url=downURL)
    else:
        return await render_template('404.html')
