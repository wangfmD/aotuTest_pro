# encoding: utf-8
"""
     printLog.py
     Desc: test log out
     Maintainer: wangfm
     CreateDate: 2016-11-04 10:55:56
"""
import sys
import os
sys.path.append(os.getcwd())
from t_log import *

LOG_INIT()
logger = LOG_MODULE_DEFINE('Platform')
SET_LOG_LEVEL(logger, 'info')
T_INFO("global:%d", 123)
L_INFO(logger, 'local:%d', 123)
print "abcddddd"
