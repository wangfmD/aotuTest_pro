# coding=utf-8
import ConfigParser
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import os

# 从环境变量中读取项目路径，获取配置文件路径
home_path = os.environ.get('PY_DEV_HOME')
basedir = os.path.abspath(os.path.dirname(__file__))
tmpEnvFile = basedir + '\.tmp'
with open(tmpEnvFile, 'r+') as f:
    pathTmp = f.readlines()
# cfg_path = home_path + '/webTest_pro/cfg/init_v1.conf'
cfg_path = pathTmp[0]

print cfg_path
