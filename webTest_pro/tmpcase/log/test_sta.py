# coding: utf-8
"""
     *.py
     Desc:
     Maintainer: wangfm
     CreateDate: 2016-11-04 15:26:52
"""

import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from t_log import *

# LOG_INIT('log.log')
LOG_INIT("log.log")
logger = LOG_MODULE_DEFINE('Platform')
SET_LOG_LEVEL(logger, 'info')


class logMgr(unittest.TestCase):

    def test_outLog(self):
        T_INFO("global:%d", 123)
        L_INFO(logger, 'local:%d', 123)
        print "exec: logMgr start..."
        T_INFO("start exec")
        L_INFO(logger, "L_info start out")
        print "exec: logMgr end."


if __name__ == '__main__':
    unittest.main()
