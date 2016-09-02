import MySQLdb

_INSTANCE_NAME = 'ricksf1site:f1database'


def connection():
    db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='f1data', user='root', passwd='Buddy123185',
                           charset='utf8')
    cur = db.cursor()

    cur.execute("select forename, surname from drivers")

    for item in cur.fetchall():
        print item
