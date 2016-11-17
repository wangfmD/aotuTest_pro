# coding=utf-8
"""
     cleanDB.py
     Desc: for clean DB setup
     Maintainer: wangfm
     CreateDate: 2016-11-10 19:59:07
"""

import unittest
from _env import addPaths
addPaths('.')
from common.execsql import execFileSql
from common.init import sqlFilePath, db_conf

# init data
filesql = sqlFilePath + 'middle.sql'
# filesql = 'G:\\00project\\sql_lib\\middle_10.sql'
# dbinfo = {
#     'host': '10.1.0.57',
#     'usr': 'root',
#     'passwd': 'Sanbu@123456',
#     'port': '13306',
#     'database': 'middle'
# }

dbinfo = {
    'host':db_conf['host'],
    'usr':db_conf['user'],
    'passwd':db_conf['passwd'],
    'port':db_conf['port'],
    'database':db_conf['db']
}



class dbMgr(unittest.TestCase):
    def test_cleanDB(self):
        """TODO: Docstring for test_cleanDB.
        :returns: TODO

        """
        execFileSql(filesql, **dbinfo)


if __name__ == '__main__':
    unittest.main()
    # print filesql
