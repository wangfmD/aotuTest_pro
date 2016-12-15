# coding=utf-8
import os

from t_log import LOG_INIT, LOG_MODULE_DEFINE, SET_LOG_LEVEL, T_INFO, L_INFO


def getlogfile():
    home_path = os.environ.get('PY_DEV_HOME')
    logpath = home_path + '\webTest_pro\log'
    logfile = logpath + '\webTest_pro.log'
    if os.path.exists(logpath) == True:
        print ">>Log path:{}".format(logpath)
    else:
        print "Create report directory..."
        os.mkdir(logpath)
        print ">>Log path:{}".format(logpath)
    return logfile

LOG_INIT(getlogfile())
logger = LOG_MODULE_DEFINE('webTest_pro')
SET_LOG_LEVEL(logger, 'info')
