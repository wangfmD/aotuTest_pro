# coding=utf-8
"""
     cleanDB.py
     Desc: for clean DB setup
     Maintainer: wangfm
     CreateDate: 2016-11-10 19:59:07
"""
import os
import sys
import unittest

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.execsql import execFileSql, execFileSqlOnly
from webTest_pro.common.initData import init
from webTest_pro.common.logger import logger,T_INFO
from webTest_pro.common.mysqlKit import sqlOperating
from webTest_pro.common.dockerservice import restart_service

host = init.db_conf['host']
active_code, service = init.active_code, 'interact'
streaming_media = init.streaming_media
hostadd = init.db_conf['hostadd']
mediaAddr = streaming_media['serverIps']

# init data
filesql = init.sqlFilePath + 'middle.sql'
filesqlversion = init.sqlFilePath + 'middle_db_version.sql'

dbinfo = {
    'host': init.db_conf['host'],
    'usr': init.db_conf['user'],
    'passwd': init.db_conf['passwd'],
    'port': init.db_conf['port'],
    'database': init.db_conf['db']
}


class dbMgr(unittest.TestCase):
    """dbMgr"""
    def test_cleanDB(self):
        """重刷数据库"""
        T_INFO(logger, 'start test_cleanDB.')
        execFileSql(filesql, **dbinfo)
        logger.info("exec sql {}".format(filesql))
        execFileSqlOnly(filesqlversion, **dbinfo)
        T_INFO(logger, "exec sql {}".format(filesqlversion))
        T_INFO(logger, 'end test_cleanDB.')
        
    def test_updateDB_version(self):
        T_INFO(logger, 'start case dbMgr')
        conn = sqlOperating(init.db_conf['host'],
                            init.db_conf['user'],
                            init.db_conf['passwd'],
                            init.db_conf['db'])
        conn.updaeDb(init.sqlStatements)
            
        T_INFO(logger, 'exec: test_updateDB end.')


    def test_z_restart_interact(self):
        T_INFO(logger, 'exec: test_restart_interact...')
        restart_service(host, active_code, service)
        print 'exec: test_restart_interact end.'
        T_INFO(logger,'case test_restart_interac end!')

if __name__ == '__main__':
    unittest.main()
