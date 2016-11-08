# coding: utf-8
"""
     *.py
     Desc:test log out put
     Maintainer: wangfm
     CreateDate: 2016-11-04 15:26:52
"""

import unittest
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from log.t_log import LOG_INIT, LOG_MODULE_DEFINE, SET_LOG_LEVEL, T_INFO, L_INFO



class logMgr(unittest.TestCase):
    def test_outLog(self):
        LOG_INIT('log.log')
        logger = LOG_MODULE_DEFINE('Platform')
        SET_LOG_LEVEL(logger, 'info')
        print "exec: logMgr start..."
        T_INFO("start exec")
        L_INFO(logger, "L_info start out")
        print "exec: logMgr end."


if __name__ == '__main__':
    #  unittest.main()
    for path in sys.path:
        print path
