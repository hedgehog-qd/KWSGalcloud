__all__ = ()
import od
import db
from quart import Blueprint
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import send_file

admin = Blueprint('admin', __name__)


# admin模块
@admin.route('/')
async def alluser():
    allFiles = db.getFileCount()
    banned, normal = db.getUsersAdmin()
    return await render_template('/admin/home.html', allFiles=allFiles, banned=banned, normal=normal)


@admin.route('/users', methods=['GET', 'POST'])
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
    return '1'


@admin.post('/adduser')
async def adduser():
    content = db.getRegisterCode()
    return await render_template('/admin/users.html', content=content)


@admin.route('/banuser')
async def banuser():
    code = (await request.form).get('code')

    content = db.getRegisterCode()
    return await render_template('/admin/users.html', content=content)


@admin.route('/integral')
async def integral():
    return await render_template('/admin/integral.html')


@admin.get("/manualrefresh")
async def read_root():
    stacode = od.refresh()
    if stacode == 0:
        return {"RefreshDatabase": "success"}
    elif stacode == 1:
        return {"failed": "you can't refresh the database toooo many times!"}
    elif stacode == 2:
        return {"error": "something wrong happened"}
