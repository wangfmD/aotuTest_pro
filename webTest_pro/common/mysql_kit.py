# coding:utf-8
import MySQLdb
from MySQLdb import cursors
from init import db_conf


# print dir(MySQLdb.connect)
# print dir(MySQLdb)
# print dir(MySQLdb.cursors)

# mysql setting
host = '10.1.0.57'
hostadd = db_conf['hostadd']
user = 'root'
passwd = 'Sanbu@123456'
db = 'middle'
port = 13306

sqlpara = [{'col_name': 'live_server_url', 'col_value': 'rtmp://' + hostadd + ':1935/live/'},
           {'col_name': 'web_server_resource', 'col_value': 'http://' + hostadd},
           {'col_name': 'file_server_url', 'col_value': hostadd + '/filesrv'},
           {'col_name': 'mcu_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_url_visit', 'col_value': hostadd + ':11194'},
           {'col_name': 'message_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_ftp_host', 'col_value': hostadd},
           {'col_name': 'web_server_client', 'col_value': 'http://' + hostadd + '/middleclient/index.do'}
           ]


class sqlOperating:
    '''数据库操作'''

    def __init__(self, host=host, user=user, passwd=passwd, db=db, port=13306):
        try:
            self.con = MySQLdb.connect(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db,
                                       port=port,
                                       cursorclass=MySQLdb.cursors.DictCursor)
        except MySQLdb.Error, e:
            print "Mysql Err %d:%s" % (e.args[0], e.args[1])

    def execQury(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        # print dir(cur)
        return res
        self.con.close()

    def updaeDb(self, sql):
        cur = self.con.cursor()
        try:
            cur.execute(sql)
            self.con.commit()
            print 'a'
        except:
            self.con.rollback()
            print 'b'
        self.con.close()
        print 'c'
if __name__ == '__main__':
    # sql = ["UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'live_server_url'" % 'rtmp://' + hostadd + ':1935/live/',
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'web_server_resource'" % 'http://' + hostadd,
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'file_server_url'" % hostadd + '/filesrv',
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'mcu_center_host'" % hostadd,
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'file_server_url_visit'" % hostadd + ':11194',
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'message_center_host'" % hostadd,
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'file_server_ftp_host'" % hostadd,
    #        "UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = 'web_server_client'" % 'http://' + hostadd + '/middleclient/index.do']
    # sql = ["UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % 'rtmp://10.1.0.56:1935/live/']
    # for s in sqlpara:
    #     c = sqlOperating(db_conf['host'],
    #                      db_conf['user'],
    #                      db_conf['passwd'],
    #                      db_conf['db'])
    #     # c = sqlOperating()
    #     # print s['col_name'], s['col_value']
    #     c.updaeDb("UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % (s['col_value'], s['col_name']))

    # print type(db_conf['host']), db_conf['user'], db_conf['passwd'], db_conf['db'], int(db_conf['port'])
    sql = "select ID,CLASSROOM_ID from interact_teach_lesson where LESSON_NAME='hdk_long'"
    c = sqlOperating()
    result = c.execQury(sql)
    for lie in result:
        # print dir(lie)
        # print lie
        for k, v in lie.iteritems():
            print k, "=", lie[k]
