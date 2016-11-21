# coding=utf-8
import ConfigParser
import sys
from log.t_log import LOG_INIT, LOG_MODULE_DEFINE, SET_LOG_LEVEL, T_INFO, L_INFO
reload(sys)
sys.setdefaultencoding("utf-8")

import os

# 从环境变量中读取项目路径，获取配置文件路径
home_path = os.environ.get('PY_DEV_HOME')
# 日志文件存放路径
logPath = home_path + '\webTest_pro\log'
logFile = logPath + '\exec.log'
# 日志路径不存在，则创建该路径
# 如果log路径不存在，则会导致用例执行失败
if os.path.exists(logPath) == True:
    print "The log path exist!"
else:
    print "The log path is not exist,create report directory..."
    os.mkdir(logPath)

# 初始化日志模块
LOG_INIT(logFile)
logger = LOG_MODULE_DEFINE('Platform')
SET_LOG_LEVEL(logger, 'info')



basedir = os.path.abspath(os.path.dirname(__file__))
# 从生成的文件中读取配置文件路径
tmpEnvFile = home_path + '\webTest_pro\common\.tmp'
with open(tmpEnvFile, 'r+') as f:
    pathTmp = f.readlines()
cfg_path = pathTmp[0]
L_INFO(logger, 'The config path >> %s', cfg_path)

# sql文件存放路径
sqlFilePath = home_path + '\webTest_pro\data\sqllib\\'




# 配置文件的学校、教室、设备信息
classroom_para = []

classroom_tmp = []

# 测试平台的访问路径前缀
base_url = ''

# 管理平台数据库信息配配置
db_conf = {}

loginInfo = {}

execEnv = {}

#流媒体地址配置
streaming_media = {}

# # 测试报告路径不存在，则创建该路径
# if os.path.exists(logPath) == True:
#     print "The log path exist!"
# else:
#     print "The log path is not exist,create report directory..."
#     os.mkdir(logPath)

cf = ConfigParser.ConfigParser()
# cf.read("G:\\04py\\aotuTest_pro\\webTest_pro\\cfg\\init_v1.conf")
cf.read(cfg_path)
sections = cf.sections()
#  print sections
# loginInfo = {'username':'hnsadmin', 'platformname': u"河南教育局"}
# 从配置文件中读取用户登录信息

for s in sections:
    if s.lower().find('classroom_para') != -1:
        classroom_tmp.append(s)
    if s.lower().find('basedata') != -1:
        base_url = 'http://' + cf.get(s, 'addr')
        child_interact_ip = cf.get(s, 'interact_1')
        loginInfo.setdefault('username', cf.get(s, 'username'))
        loginInfo.setdefault('platformname', cf.get(s, 'platformname'))
    if s.lower().find('db_conf') != -1:
        # host = cf.get(s, 'host')
        db_conf.setdefault('host', cf.get(s, 'host'))
        # hostadd = cf.get(s, 'hostadd')
        db_conf.setdefault('hostadd', cf.get(s, 'hostadd'))
        # user = cf.get(s, 'user')
        db_conf.setdefault('user', cf.get(s, 'user'))
        # passwd = cf.get(s, 'passwd')
        db_conf.setdefault('passwd', cf.get(s, 'passwd'))
        # db = cf.get(s, 'db')
        db_conf.setdefault('db', cf.get(s, 'db'))
        db_conf.setdefault('port', cf.get(s, 'port'))
    if s.lower().find('env_para') != -1:
        execEnv.setdefault('execType', cf.get(s, 'execType'))
        execEnv.setdefault('remoteUrl', cf.get(s, 'remoteUrl'))
    if s.lower().find('streaming_media') != -1:
        streaming_media.setdefault('serverIps', cf.get(s, 'serverIps'))

for s in classroom_tmp:
    opts = cf.options(s)
    arr = {}
    for o in opts:
        name = cf.get(s, o)
        # print o,": ", name
        arr.setdefault(o, unicode(name).encode("utf-8"))
    classroom_para.append(arr)

if __name__ == '__main__':
    print tmpEnvFile
    print logFile
