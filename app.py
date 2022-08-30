from flask import Flask, render_template, request, redirect

import config
import od

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('home.html',appname=config.app_name,appversion=config.app_version,url=config.redirect_url)


@app.route('/s')
def search():
    return render_template('search.html')


@app.route('/s', methods=['POST'])
def research():
    return 0

@app.route('/detail', methods=['POST'])
def detail():
    return 0


if __name__ == '__main__':
    od.connectod()
    app.run()
