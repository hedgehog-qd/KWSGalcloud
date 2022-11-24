__all__ = ()
import od
import db
from quart import Blueprint
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import send_file
from blueprints.utils import flash
from functools import wraps


admin = Blueprint('admin', __name__)


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not session:
            return await flash('error', 'You must be logged in to access that page.', 'login')
        if session['is_admin'] != 1:
            return await flash('error', '您没有权限', 'login')
        return await func(*args, **kwargs)

    return wrapper


# admin模块
@admin.route('/')
@login_required
async def alluser():
    allFiles = db.getFileCount()
    banned, normal = db.getUsersAdmin()
    return await render_template('/admin/home.html', allFiles=allFiles, banned=banned, normal=normal)


@admin.route('/users', methods=['GET', 'POST'])
@login_required
async def users():
    if request.method == 'GET':
        content = db.getRegisterCode()
        banned, normal = db.getUsersAdmin()
        print(content)
        return await render_template('/admin/users.html', content=content, banned=banned, normal=normal)
    statto = (await request.form).get('statto')
    codeto = (await request.form).get('codeto')
    print(statto)
    print(codeto)
    stat = db.setRegisterCode(statto, codeto)
    if stat == 0:
        return '1'
    else:
        return '0'


@admin.post('/adduser')
@login_required
async def adduser():
    code = (await request.form).get('code')
    stat = db.addUserCode(code)
    content = db.getRegisterCode()
    banned, normal = db.getUsersAdmin()
    if stat == 1:
        return await render_template('/admin/users.html', content=content, banned=banned, normal=normal, flash='该邀请码已存在!', status='error')
    content = db.getRegisterCode()
    return await render_template('/admin/users.html', content=content, banned=banned, normal=normal, flash='OK!', status='success')


@admin.post('/banuser')
@login_required
async def banuser():
    uid = (await request.form).get('ban')
    content = db.getRegisterCode()
    banned, normal = db.getUsersAdmin()
    stat = db.banUser(uid)
    if stat == 1:
        return await render_template('/admin/users.html', content=content, banned=banned, normal=normal, flash='用户不存在!', status='error')
    banned, normal = db.getUsersAdmin()
    return await render_template('/admin/users.html', content=content, banned=banned, normal=normal, flash='OK!', status='success')


@admin.route('/integral', methods=['GET', 'POST'])
@login_required
async def integral():
    allInte, banInte, avaInte, avaCodeInte, usedCodeInte = db.getIntegralInf()
    content = db.getInteCodeInf()
    if request.method == 'GET':
        return await render_template('/admin/integral.html', content=content, allInte=allInte, banInte=banInte, avaInte=avaInte, avaCodeInte=avaCodeInte, usedCodeInte=usedCodeInte)
    code = (await request.form).get('code')
    worth = (await request.form).get('worth')
    stat = db.changeIntegral(code, worth)
    if stat == 1:
        return await render_template('/admin/integral.html', content=content, allInte=allInte, banInte=banInte, avaInte=avaInte, avaCodeInte=avaCodeInte, usedCodeInte=usedCodeInte, flash='积分值无效!', status='error')
    if stat == 2:
        return await render_template('/admin/integral.html', content=content, allInte=allInte, banInte=banInte, avaInte=avaInte, avaCodeInte=avaCodeInte, usedCodeInte=usedCodeInte, flash='该兑换码已存在!', status='error')
    if stat == 0:
        allInte, banInte, avaInte, avaCodeInte, usedCodeInte = db.getIntegralInf()
        content = db.getInteCodeInf()
        return await render_template('/admin/integral.html', content=content, allInte=allInte, banInte=banInte, avaInte=avaInte, avaCodeInte=avaCodeInte, usedCodeInte=usedCodeInte, flash='OK!', status='success')


@admin.get("/manualrefresh")
async def read_root():
    stacode = od.refresh()
    if stacode == 0:
        return {"RefreshDatabase": "success"}
    elif stacode == 1:
        return {"failed": "you can't refresh the database toooo many times!"}
    elif stacode == 2:
        return {"error": "something wrong happened"}
