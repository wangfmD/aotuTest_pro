# coding=utf-8
import ConfigParser
import os
import sys

sys.path.append(os.getenv('PY_DEV_HOME'))
from webTest_pro.common.logger import logger

from webTest_pro.common.os_sqlfile_read import getSqlPath

reload(sys)
sys.setdefaultencoding("utf-8")

home_path = os.environ.get('PY_DEV_HOME')


def getCfgPath():
    tmpEnvFile = home_path + '\webTest_pro\common\.tmp'
    if os.path.exists(tmpEnvFile):
        with open(tmpEnvFile, 'r+') as f:
            pathTmp = f.readlines()
        cfg_path = pathTmp[0]
#         print cfg_path
        logger.info('cfg file path %s' % tmpEnvFile)
    else:
        cfg_path = home_path + '\webTest_pro\cfg\init_default.conf'
        logger.info('cfg file path %s' % tmpEnvFile)
    return cfg_path



def getCfgs(cfg_path):
    # 配置文件的学校、教室、设备信息
    classroom_para = []

    classroom_tmp = []

    # 测试平台的访问路径前缀
    base_url = ''

    # 管理平台数据库信息配配置
    db_conf = {}

    loginInfo = {}

    execEnv = {}

    # 流媒体地址配置
    streaming_media = {}

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
    # from conf get classroom_para
    for s in classroom_tmp:
        opts = cf.options(s)
        arr = {}
        for o in opts:
            name = cf.get(s, o)
            arr.setdefault(o, unicode(name).encode("utf-8"))
        classroom_para.append(arr)
    return classroom_para, base_url, db_conf, loginInfo, execEnv, streaming_media, child_interact_ip


def get_active_code(cfg_path):
    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    active_code = cf.get('basedata', 'active_code')
    return active_code


class cfg(object):
    def __init__(self):
        # self.logFile = getLogFile()
        self.cfg_path = getCfgPath()
        self.tmpData = getCfgs(self.cfg_path)
        self.classroom_para = self.tmpData[0]
        self.base_url = self.tmpData[1]
        self.db_conf = self.tmpData[2]
        
        self.loginInfo = self.tmpData[3]
        self.execEnv = self.tmpData[4]
        self.streaming_media = self.tmpData[5]
        self.child_interact_ip = self.tmpData[6]
        #读取路径
        # data_path = getSqlPath(self.base_url, self.db_conf)
        data_path = getSqlPath(self.base_url)
        self.sqlFilePath = data_path[0]
        self.sqlStatements = data_path[1]
        self.active_code = get_active_code(self.cfg_path)
#         self.sqlFilePathVer = data_path[1]
        logger.info("#############################Init basedata start#############################")
        logger.info(">>>>base_url: {}".format(self.base_url))
        logger.info(">>>>cfg_path: {}".format(self.cfg_path))
        logger.info(">>>>child_interact_ip: {}".format(self.child_interact_ip))
        logger.info(">>db_conf")
        for k, v in self.db_conf.items():
            logger.info(">>>>{0}: {1}".format(k, v))
        logger.info(">>loginInfo")
        for k,v in self.loginInfo.items():
            logger.info(">>>>{0}: {1}".format(k, v))
        logger.info(">>>>media IP: {}".format(self.streaming_media))
        logger.info(">>>>sql Version: {}".format(self.sqlFilePath))
        logger.info(">>>>sqlStatements: {}".format(self.sqlStatements))
        logger.info("#############################Init basedata end#############################")

if __name__ == "__main__":
    init = cfg()
