import pymysql
import config
import datetime


def verifyRefreshDate():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = "SELECT * FROM refresh"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    pp = datetime.date.today()
    if pp in data:
        return False
    else:
        return True


def updateRefreshDate():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    pp = datetime.date.today()
    p = pp.strftime("%Y-%m-%d")
    print(p)
    sql = "UPDATE refresh set refresh_date=\'" + str(p) + "\';"
    cursor.execute(sql)
    sql2 = "UPDATE files set safename = lower(name);"
    cursor.execute(sql2)
    db.commit()
    print("refreshed the date")
    return 0


def search(searchtext):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    sql = "SELECT * FROM files;"
    cursor = db.cursor()
    cursor.execute(sql)
    rest = cursor.fetchall()
    result = []
    for i in rest:  # 搜索
        if searchtext in i[6]:
            result.append(i)
    """
    makehtml = "<div class=\"container-fluid\"><div class=\"row\"><div class=\"col-12\"><div class=\"card\"><div class=\"card-header\"><h3 class=\"card-title\">搜索结果</h3></div><div class=\"card-body\"><table id=\"example1\" class=\"table table-bordered table-striped\"><thead><tr><th>文件名/目录名</th><th>类型</th><th>路径</th><th>大小</th></tr></thead><tbody>"
    for j in result:
        makehtml += "<tr>"
        makehtml += "<td><a herf=\"/d"
        makehtml += j[4]+"/"+j[0]
        makehtml += "\">"
        makehtml += j[0]
        makehtml += "</a>"
        makehtml += "</td>"
        makehtml += "<td>"
        if j[3] == 0:
            makehtml += "文件"
        else:
            makehtml += "文件夹"
        makehtml += "</td>"
        makehtml += "<td>"
        makehtml += j[4]
        makehtml += "</td>"
        makehtml += "<td>"
        makehtml += str(j[5])
        makehtml += "</td>"
        makehtml += "</tr>"
    makehtml += "</tbody></table></div></div></div></div></div>"
    """
    return result


def getppDir(route):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    print(route)
    """
    if 'root' in route:
        route = route[4:]
        """
    sql = 'SELECT * FROM files WHERE uplink=' + '\"' + route + '\"'
    cursor.execute(sql)
    rest = cursor.fetchall()

    return rest


def gethome():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = "SELECT * FROM files WHERE uplink='/root';"
    cursor.execute(sql)
    rest = cursor.fetchall()
    return rest


def filedetail(route, name):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT * FROM files WHERE uplink=' + '\"' + route + '\"' + 'AND name=' + '\"' + name + '\"'
    cursor.execute(sql)
    rest = cursor.fetchall()
    return rest


def checklogin(email, pwd):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT passwd FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql)
    a = cursor.fetchone()
    if a is None:
        print("用户不存在！")
        return 2
    else:
        if a[0] != pwd:
            print("密码错误！")
            return 1
        else:
            print("成功登录！")
            return 0


def getuserdata(email):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT username FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql)
    username = cursor.fetchone()
    sql2 = 'SELECT is_admin FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql2)
    is_admin = cursor.fetchone()
    sql3 = 'SELECT is_ban FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql3)
    is_ban = cursor.fetchone()
    sql4 = 'SELECT avatar FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql4)
    avatar = cursor.fetchone()
    sql5 = 'SELECT uid FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql5)
    uid = cursor.fetchone()
    return username[0], is_admin[0], is_ban[0], avatar[0], uid[0]


def getuserintegral(email):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql2 = 'SELECT integral FROM users WHERE email=' + '"' + email + '"'
    cursor.execute(sql2)
    integral = cursor.fetchone()
    return integral


def register(email, uname, passwd, code):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = "SELECT count(*) from users where email=\"" + email + "\";"
    cursor.execute(sql)
    emails = cursor.fetchone()
    print(emails[0])
    if emails[0] != 0:
        return 1  # 用户已经注册
    cursor2 = db.cursor()
    sql2 = 'SELECT code FROM register_code;'
    cursor2.execute(sql2)
    codes = cursor2.fetchall()
    print(codes)  #
    for i in codes:
        if code == i[0]:
            cursor4 = db.cursor()
            sql3 = "SELECT available FROM register_code WHERE code=\"" + code + "\";"
            cursor4.execute(sql3)
            if cursor4.fetchone()[0] == 0:
                print("激活码不对")
                return 2  # 激活码已经不可用
            else:
                cursor3 = db.cursor()
                sql1 = "INSERT INTO users SET email=\"" + email + "\",username=\"" + str(uname) + "\",passwd=\"" + str(
                    passwd) + "\",is_admin=0,is_ban=0,integral=" + str(
                    config.initial_integral) + ",avatar=\"default.jpg\";"
                cursor3.execute(sql1)
                db.commit()
                print("OK")
                return 0  # OK
    print("激活码不存在")
    return 3  # 激活码不存在


def refreshavatar(email, newname):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'UPDATE users SET avatar="' + newname + '" WHERE email="' + email + '";'
    cursor.execute(sql)
    db.commit()
    print("OK")
    return 0


def refreshintegral(uid, code):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT count(*) FROM integral_code WHERE code="' + str(code) + '";'
    cursor.execute(sql)
    codeexi = cursor.fetchone()[0]
    if codeexi == 0:  # 激活码不存在
        return 1
    cursor2 = db.cursor()
    sql2 = 'SELECT available FROM integral_code WHERE code="' + str(code) + '";'
    cursor2.execute(sql2)
    available = cursor2.fetchone()[0]
    if available == 0:
        return 2  # 激活码已经被使用了
    cursor3 = db.cursor()
    sql3 = 'UPDATE integral_code SET available=0,uid=' + str(uid) + ' WHERE code="' + str(code) + '";'
    cursor3.execute(sql3)
    db.commit()
    cursor4 = db.cursor()
    sql4 = 'SELECT integral FROM integral_code WHERE code="' + str(code) + '";'
    cursor4.execute(sql4)
    integral = cursor4.fetchone()[0]
    cursor5 = db.cursor()
    sql5 = 'UPDATE users SET integral=integral+' + str(integral) + ' WHERE uid=' + str(uid) + ';'
    cursor5.execute(sql5)
    db.commit()
    return 0


def getFileCount():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT count(*) FROM files WHERE ftype=0;'
    cursor.execute(sql)
    files = cursor.fetchone()[0]
    return files


def getUserDownload(email):
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT total_download FROM users WHERE email="' + email + '";'
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    return count


def getUsersAdmin():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT count(*) FROM users WHERE is_ban=1;'
    cursor.execute(sql)
    bannedcount = cursor.fetchone()[0]
    cursor2 = db.cursor()
    sql2 = 'SELECT count(*) FROM users WHERE is_ban=0;'
    cursor2.execute(sql2)
    normalcount = cursor2.fetchone()[0]
    return bannedcount, normalcount


def getRegisterCode():
    db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                         database=config.database, charset='utf8')
    print("successfully connected to the database!")
    cursor = db.cursor()
    sql = 'SELECT * FROM register_code;'
    cursor.execute(sql)
    codes = cursor.fetchall()
    return codes