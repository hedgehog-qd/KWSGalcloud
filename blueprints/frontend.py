__all__ = ()
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
        return await render_template('search.html', makehtml=addhtml, searchback=searchtext)
    else:
        return await render_template('search.html', makehtml="", searchback="想玩点儿啥gal？")


@frontend.route('/d')
async def detailnull():
    if 'f' and 'n' in request.args:
        froute = str(request.args['f'])
        fname = str(request.args['n'])
        ppfile = db.filedetail(froute, fname)
        return await render_template('detail.html', url=config.redirect_url, makehtml=ppfile, dlub=config.alist_home)
    else:
        return await render_template('404.html')


@frontend.route('/all')
async def broseroot():
    if 'r' in request.args:
        route = str(request.args['r'])
        ppback = db.getppDir(route)
        return await render_template('all.html', url=config.redirect_url, content=ppback)

    else:
        drivehome = db.gethome()
        return await render_template('all.html', url=config.redirect_url, content=drivehome)


@frontend.route('/all/<id>')
async def brosefolder(id):
    pp = db.getppDir(id)
    return await render_template('all.html', url=config.redirect_url, content=pp)
