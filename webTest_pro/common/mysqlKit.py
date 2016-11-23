# coding:utf-8
import MySQLdb
from MySQLdb import cursors
from init import db_conf, streaming_media


# print dir(MySQLdb.connect)
# print dir(MySQLdb)
# print dir(MySQLdb.cursors)

# mysql setting
host = '10.1.0.46'
hostadd = db_conf['hostadd']
user = 'root'
passwd = 'Sanbu@123456'
db = 'middle'
port = 13306
mediaAddr = streaming_media['serverIps']

sqlpara = [{'col_name': 'live_server_url', 'col_value': 'rtmp://' + hostadd + ':1935/live/'},
           {'col_name': 'web_server_resource', 'col_value': 'http://' + hostadd},
           {'col_name': 'file_server_url', 'col_value': mediaAddr + '/filesrv'},
           {'col_name': 'mcu_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_url_visit', 'col_value': mediaAddr + ':11194'},
           {'col_name': 'message_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_ftp_host', 'col_value': mediaAddr},
           {'col_name': 'web_server_client', 'col_value': 'http://' + hostadd + '/middleclient/index.do'},
           {'col_name': 'centerfile_host', 'col_value': hostadd}
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
            print "DB connection info:"
            print "  >>host: {0}\n  >>user: {1}\n  >>password: {2}\n  >>database: " \
                  "{3}\n  >>port:{4}".format(host,user,passwd,db,port)
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
            print 'updated successful.'
        except:
            self.con.rollback()
            print 'updated failed.'
        self.con.close()
        print 'closed connection.'
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


    # sql = "select ID,CLASSROOM_ID from interact_teach_lesson where LESSON_NAME='hdk_long'"
    # c = sqlOperating()
    # result = c.execQury(sql)
    # for lie in result:
        # for k, v in lie.iteritems():
            # print k, "=", lie[k]
    print mediaAddr

