# coding=utf-8
"""
     test exec *.sql with python
     Desc:*
     Maintainer: wangfm
     CreateDate: 2016-11-09 17:56:28
"""
# cmd login
# mysql -h10.1.0.56 -uroot -pSanbu@123456 -P13306
import MySQLdb
from subprocess import Popen, PIPE


def execFileSql(*args, **kwargs):
    """
      Function: execFileSql()
      Desc: 删除数据库，并重建，最后刷库
      Args:
         - :file
         - :**
      Return: result
      Usage: execFileSql(file, **)
      Maintainer: wangfm
      CreateDate: 2016-11-10 15:57:02
    """
    # init data
    filesql = args[0]
    host = kwargs['host']
    usr = kwargs['usr']
    passwd = kwargs['passwd']
    port = int(kwargs['port'])
    database = kwargs['database']

    # clean database
    try:
        conn = MySQLdb.connect(host=host, user=usr, passwd=passwd, port=port)
        cur = conn.cursor()
        cur.execute('DROP DATABASE IF EXISTS %s' % database)
        cur.execute(
            'CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARSET utf8 COLLATE utf8_general_ci' %
            database)
        # CREATE DATABASE IF NOT EXISTS middle DEFAULT CHARSET utf8 COLLATE
        # utf8_general_ci
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    process = Popen(
        'mysql -h%s -P%s -u%s -p%s %s' %
        (host,
         port,
         usr,
         passwd,
         database),
        stdout=PIPE,
        stdin=PIPE,
        shell=True)
    print "1------"
    print "exec sql,wait..."
    output = process.communicate('source ' + filesql)
    print output
    print "end."


def exec_test():
    """
      Function: exec_test()
      Desc: test
      Args:
         - :
      Return:
      Usage:
      Maintainer: wangfm
    """
    filesql = 'G:\\00project\\sql_lib\\middle_10.sql'
    dbinfo = {'host':'10.1.0.56', 'usr': 'root','passwd': 'Sanbu@123456',
              'port':'13306',
              'database':'middle2'}
    execFileSql(filesql, **dbinfo)

if __name__ == '__main__':
    exec_test()
