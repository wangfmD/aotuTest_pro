import sys
import unittest

from _env import addPaths

addPaths('.')
from common.mysqlKit import sqlOperating, sqlpara
from common.init import db_conf, logFile
from common.log.t_log import LOG_INIT, LOG_MODULE_DEFINE, SET_LOG_LEVEL, T_INFO, L_INFO

host = db_conf['host']

# set log info
LOG_INIT(logFile)
logger = LOG_MODULE_DEFINE('Platform')
SET_LOG_LEVEL(logger, 'info')


class dbMgr(unittest.TestCase):
    def test_updateDB(self):
        print 'exec: test_updateDB...'
        # T_INFO('global:%d', 123)
        L_INFO(logger, 'start case dbMgr')
        for s in sqlpara:
            conn = sqlOperating(db_conf['host'],
                                db_conf['user'],
                                db_conf['passwd'],
                                db_conf['db'])
            # c = sqlOperating()
            # print s['col_name'], s['col_value']
            conn.updaeDb("UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % (s['col_value'], s['col_name']))
        print 'exec: test_updateDB end.'
        L_INFO(logger, 'case dbMgr end!')

if __name__ == '__main__':
    unittest.main()
