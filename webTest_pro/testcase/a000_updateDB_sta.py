import unittest, sys

from _env import addPaths
addPaths('.')
from common.mysqlKit import sqlOperating, sqlpara
from common.init import db_conf


class dbMgr(unittest.TestCase):
    def test_updateDB(self):
        print 'exec: test_updateDB...'
        for s in sqlpara:
            conn = sqlOperating(db_conf['host'],
                                db_conf['user'],
                                db_conf['passwd'],
                                db_conf['db'])
            # c = sqlOperating()
            # print s['col_name'], s['col_value']
            conn.updaeDb("UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % (s['col_value'], s['col_name']))
        print 'exec: test_updateDB end.'

if __name__ == '__main__':
    unittest.main()
    for path in sys.path:
        print path
