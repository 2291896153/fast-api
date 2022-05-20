import pymysql


def db():
    return pymysql.connect(host='192.168.3.250',
                           port=30102,
                           user='root',
                           password='123456',
                           database='cost')


def cursor():
    return db().cursor()


def execute(sql):
    cursor().execute(sql)


def fetchall():
    return cursor().fetchall()


def db_close():
    db().close()
