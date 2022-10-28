import pymysql
import config
import app
import datetime
from time import strftime

db = pymysql.connect(host=config.host, port=config.port, user=config.user_name, password=config.passwd,
                     database=config.database, charset='utf8')
print("successfully connected to the database!")

def verifyRefreshDate():
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
    cursor = db.cursor()
    pp = datetime.date.today()
    p = pp.strftime("%Y-%m-%d")
    print(p)
    sql = "UPDATE refresh set refresh_date=\'"+str(p)+"\';"
    cursor.execute(sql)
    sql2 = "UPDATE files set safename = lower(name);"
    cursor.execute(sql2)
    db.commit()
    print("refreshed the date")
    return 0

def search(searchtext):
    sql = "SELECT * FROM files;"
    cursor = db.cursor()
    cursor.execute(sql)
    rest = cursor.fetchall()
    result = []
    for i in rest:  #搜索
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
    cursor = db.cursor()
    print(route)
    """
    if 'root' in route:
        route = route[4:]
        """
    sql = 'SELECT * FROM files WHERE uplink='+'\"'+route+'\"'
    cursor.execute(sql)
    rest = cursor.fetchall()

    return rest

def gethome():
    cursor = db.cursor()
    sql = "SELECT * FROM files WHERE uplink='/root';"
    cursor.execute(sql)
    rest = cursor.fetchall()
    return rest

def filedetail(route,name):
    cursor = db.cursor()
    sql = 'SELECT * FROM files WHERE uplink='+'\"'+route+'\"'+'AND name='+'\"'+name+'\"'
    cursor.execute(sql)
    rest = cursor.fetchall()
    return rest