import config
import requests
import json
import pymysql
import db
from urllib.parse import urlencode

# import onedrivesdk

import db

"""
def connectod():
    redirect_uri = config.redirect_url
    client_secret = config.client_secret
    client_id = config.client_id
    api_base_url = 'https://api.onedrive.com/v1.0/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)

    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')

    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    """


def request_data():
    params = {
        "path": config.alist_path,
        "password": config.alist_passwd,
    }
    req = requests.post(config.alist_url, data=params)  # 请求连接
    req_json = req.json()  # 获取数据
    return req_json


def refreshdb():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    jsonn = request_data()
    cursor = db.cursor()
    print(jsonn)
    print(" ")
    json_str = json.dumps(jsonn)
    data2 = json.loads(json_str)
    print(data2['message'])
    print(" ")
    filesea = data2['data']
    for i in filesea:
        print('filename :' + i['name'])
        print('uplink: ' + i['path'])
        print('size: ' + str(i['size']))
        pp = 0
        if (i['type'] == 1):
            pp = 1
            print('type: ' + '1')
        else:
            pp = 0
            print('type: ' + '0')
        print('dlink: ' + i['path'] + '/' + i['name'])
        params1 = {'': i['name']}
        downloadsafe = urlencode(params1)[1:]
        if checkexist(downloadsafe, str(i['size'])) == 1:
            sql = "INSERT into files set name=\"" + i['name'] + "\",uplink=\"" + i['path'] + "\",size=" + str(
                i['size']) + \
                  ",ftype=" + str(pp) + ",id=0,safename=\"0\"" + ",Dllink=\"" + i['path'] + '/' + i[
                      'name'] + "\",safedownload=\"" + str(downloadsafe) + "\";"
            cursor.execute(sql)
            db.commit()
        else:
            continue

    print('done')
    return 0


def refresh():
    p = db.verifyRefreshDate()
    if p == False:
        print("date Error: you can't refresh the database toooo many times!")
        return 1
    else:
        code = refreshdb()
        if code == 0:
            print("successfully refreshed the database!")
            db.updateRefreshDate()
            return 0
        else:
            return 2


def checkexist(safename, size):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    cursor = db.cursor()
    print("successfully connected to the database!")
    sql = 'SELECT count(*) FROM files WHERE safename="' + str(safename) + '"AND size=' + size + ';'
    cursor.execute(sql)
    ava = cursor.fetchone()[0]
    if ava != 0:  # 该文件已经存在无需重复添加
        return 0
    return 1

# connectod()
