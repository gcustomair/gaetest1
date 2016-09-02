import MySQLdb

_INSTANCE_NAME = 'custom-airinc:custom-db'


def connection():
    conn = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='python', user='root', passwd='Buddy123185',
                           charset='utf8')
    c = conn.cursor()

    return c, conn