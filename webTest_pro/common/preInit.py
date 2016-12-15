# coding=utf-8
"""
  preInit.py
  Desc:
  Maintainer: wangfm
  CreateDate: 2016/12/7
"""
import ConfigParser
import argparse
import os
import sys

try:
    from statusdocke import checkRunner
    from configTest import TestRunner
    from logger import logger
except ImportError:
    sys.path.append(os.getenv('PY_DEV_HOME'))
    from webTest_pro.common.statusdocke import checkRunner
    from webTest_pro.configTest import TestRunner
    from webTest_pro.common.logger import logger


def _getcfgpath(initconf):
    """
      Function: _getcfgpath()
      Desc:
      Args:
         -
      Return: None
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """

    home_path = os.getenv("PY_DEV_HOME")
    if initconf == 'dev':
        cfg_path = home_path + '\webTest_pro\cfg\init_dev.conf'
    elif initconf == 'debug':
        cfg_path = home_path + '\webTest_pro\cfg\init_debug.conf'
    elif initconf == 'test':
        cfg_path = home_path + '\webTest_pro\cfg\init_test.conf'
    elif initconf == 'wf':
        cfg_path = home_path + '\webTest_pro\cfg\init_wf.conf'
    else:
        cfg_path = home_path + '\webTest_pro\cfg\init_default.conf'
    return cfg_path


def setcfghost(platformhost, mediahost, initconf, active_code):
    """
      Function: setcfghost()
      Desc:
      Args:
         - 
      Return: None
      Usage: 
      Maintainer: wangfm
      CreateDate: 2016/12/6
    """

    cfg_path = _getcfgpath(initconf)
    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    original_platform_add = cf.get('basedata', 'addr')
    original_media_add = cf.get('streaming_media', 'serverIps')
    original_active_code = cf.get('basedata', 'active_code')
    logger.info("###################configure info###################")

    if platformhost is not None:
        cf.set('basedata', 'addr', platformhost)
        cf.set('db_conf', 'host', platformhost)
        cf.set('db_conf', 'hostadd', platformhost)
        logger.info("original platform add:{0} modfied to {1}".format(original_platform_add, platformhost))
    else:
        logger.info("waring: platform host address not configured.")

    if mediahost is not None:
        cf.set('streaming_media', 'serverIps', mediahost)
        logger.info("original media add:{0} modfied to {1}".format(original_media_add, mediahost))
    else:
        logger.warning("waring: media host address not configured.")

    if active_code is not None:
        cf.set('basedata', 'active_code', active_code)
        logger.info("original media add:{0} modfied to {1}".format(original_active_code, mediahost))
    else:
        logger.warning("waring: active_code not configured.")

    cf.write(open(cfg_path, "w"))

    logger.info("Configuration success: {}".format(cfg_path.split('\\')[-1]))


def parseargs():
    """
      Function: parse_args()
      Desc: CLI
      Args:
         -
      Return: args
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """
    description = 'example: python Runner.py -f dev x.x.x.x x.x.x.x -r case'
    parser = argparse.ArgumentParser(description=description)
    helph = 'The host IP address of the platform.'
    parser.add_argument('host', help=helph)
    helpm = 'The host IP address of the media service.'
    parser.add_argument('media', help=helpm, nargs='?')
    helpa = 'The active code of the platform.'
    parser.add_argument('-a', '--active', help=helpa)
    parser.add_argument('-r', '--runner', help='foo help', choices=['case', 'check'])
    parser.add_argument('-f', '--file', help='foo help', choices=['dev', 'test', 'default', 'debug', 'wf'])
    _args = parser.parse_args()
    return _args


def preinit():
    """
      Function: preinit()
      Desc: 输入ip地址，修改配置文件，并返回平台ip
      Args:
         - 
      Return: platfrom ip address
      Usage: 
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """
    _args = parseargs()
    host = _args.host
    media = _args.media
    init_conf = _args.file
    runner = _args.runner
    active_code = _args.active

    if runner is None:
        # config conf file
        setcfghost(host, media, init_conf, active_code)
    else:
        if runner == 'check':
            # check docker status
            setcfghost(host, media, init_conf, active_code)
            checkRunner(host)
        else:
            # run testcase
            setcfghost(host, media, init_conf, active_code)
            if checkRunner(host) is True:
                logger.info("...")
                _runner = TestRunner(init_conf)
                _runner.run()
            else:
                logger.info("Service error")


if __name__ == '__main__':
    preinit()
