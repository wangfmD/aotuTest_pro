# coding=utf-8
import ConfigParser
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import os

# 从环境变量中读取项目路径，获取配置文件路径
home_path = os.environ.get('PY_DEV_HOME')
cfg_path = home_path + '/webTest_pro/cfg/init_v1.conf'
# 配置文件的学校、教室、设备信息
classroom_para = []
# {'equipmentlogpwd': 'admin',
# 'locaddr': '10.1.0.139',
# 'schoolid': '\xe9\x83\x91\xe5\xb7\x9e\xe4\xb8\x80\xe4\xb8\xad',
# 'equipment_name': '10.1.0.139\xe7\xbb\x88\xe7\xab\xaf',
#  'equipmentlogname': 'admin',
#  'ipaddr': '10.1.0.139',
# 'classname': '139\xe6\x95\x99\xe5\xae\xa4',
#  'equimenttype': '2',
# 'equipmentmodel': 'Group\xe7\xb3\xbb\xe5\x88\x97',
# 'classaccnumber': '1'}
classroom_tmp = []
# 测试平台的访问路径前缀
base_url = ''
# 管理平台数据库信息配配置
db_conf = {}
cf = ConfigParser.ConfigParser()
# cf.read("G:\\04py\\aotuTest_pro\\webTest_pro\\cfg\\init_v1.conf")
cf.read(cfg_path)
sections = cf.sections()
#  print sections
# loginInfo = {'username':'hnsadmin', 'platformname': u"河南教育局"}
# 从配置文件中读取用户登录信息
loginInfo = {}
execEnv = {}

for s in sections:
    if s.lower().find('classroom_para') != -1:
        classroom_tmp.append(s)
    if s.lower().find('basedata') != -1:
        base_url = 'http://' + cf.get(s, 'addr')
        child_interact_ip = cf.get(s, 'interact_1')
        loginInfo.setdefault('username',cf.get(s,'username'))
        loginInfo.setdefault('platformname',cf.get(s,'platformname'))
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

for s in classroom_tmp:
    opts = cf.options(s)
    arr = {}
    for o in opts:
        name = cf.get(s, o)
        # print o,": ", name
        arr.setdefault(o, unicode(name).encode("utf-8"))
    classroom_para.append(arr)

if __name__ == '__main__':
    print execEnv
    pass
