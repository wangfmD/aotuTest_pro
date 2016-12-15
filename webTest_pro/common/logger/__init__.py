import os
from deflog import init_log, T_INFO

def getlogfile():
    home_path = os.environ.get('PY_DEV_HOME')
    logpath = home_path + '\webTest_pro\log'
    logfile = logpath + '\clientRun.log'
    if os.path.exists(logpath) == True:
        print ">>Log path:{}".format(logpath)
    else:
        print "Create report directory..."
        os.mkdir(logpath)
        print ">>Log path:{}".format(logpath)
    return logfile

logger = init_log(getlogfile())

# init_log(getlogfile())

