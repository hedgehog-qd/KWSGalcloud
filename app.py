from flask import Flask, render_template, request, redirect
import pymysql
import config
import db
import getdir
import od

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():  # put application's code here
    return render_template('home.html', appname=config.app_name, appversion=config.app_version, url=config.redirect_url)


@app.route('/s')
def search():
    if 'name' in request.args:
        searchtext = str(request.args['name'])
        print(searchtext)
        addhtml = db.search(searchtext.lower())
        return render_template('search.html', appname=config.app_name, appversion=config.app_version,
                               url=config.redirect_url, makehtml=addhtml, searchback=searchtext)
    else:
        return render_template('search.html', appname=config.app_name, appversion=config.app_version,
                               url=config.redirect_url, makehtml="", searchback="想玩点儿啥gal？")


@app.route('/d')
def detailnull():
    if 'f' and 'n' in request.args:
        froute = str(request.args['f'])
        fname = str(request.args['n'])
        ppfile = db.filedetail(froute,fname)
        return render_template('detail.html', appname=config.app_name, appversion=config.app_version,
                               url=config.redirect_url, makehtml=ppfile, dlub = config.alist_home)
    else:
        return render_template('detailnull.html')

@app.route('/all')
def broseroot():
    if 'r' in request.args:
        route = str(request.args['r'])
        ppback = db.getppDir(route)
        return render_template('all.html', appname=config.app_name, appversion=config.app_version, url=config.redirect_url, content=ppback)

    else:
        drivehome = db.gethome()
        return render_template('all.html', appname=config.app_name, appversion=config.app_version, url=config.redirect_url, content=drivehome)

@app.route('/all/<id>')
def brosefolder(id):
    pp = db.getppDir(id)
    return render_template('all.html', appname=config.app_name, appversion=config.app_version, url=config.redirect_url,
                           content=pp)



@app.get("/manualrefresh")
def read_root():
    stacode = od.refresh()
    if stacode == 0:
        return {"RefreshDatabase": "success"}
    elif stacode == 1:
        return {"failed": "you can't refresh the database toooo many times!"}
    elif stacode == 2:
        return {"error": "something wrong happened"}


if __name__ == '__main__':
    app.run()
