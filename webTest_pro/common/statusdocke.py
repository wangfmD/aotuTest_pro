# coding=utf-8
"""
  statusdocke.py
  Desc: from version rest API get service runing status._queryStatus()
        checkRunner() -> _checkRunning()->_isRunning(),_queryStatus()
  Maintainer: wangfm
  CreateDate: 2016/12/7
"""
import requests
import json
from logger import logger
from time import sleep

# logging.basicConfig(level=logging.ERROR)

# base data, Cautious modification
serviceInfos = [{
    'serviceName': 'interact'
}, {
    'serviceName': 'jycenter'
}, {
    'serviceName': 'middlecenterfile'
}, {
    'serviceName': 'middlecas'
}, {
    'serviceName': 'middlecenterres'
}, {
    'serviceName': 'middleclient'
}]
# {'serviceName': 'middleware-mcu'},

# test Data,del later
testflag = [{
    'status': 'On',
    u'dbversion': u'V1.10.11.R',
    'serviceName': 'interact',
    u'version': u'V1.02.002.B.044',
    'serviceIp': '10.1.0.56'
}, {
    'status': 'On',
    u'dbversion': u'V1.10.18.R',
    'serviceName': 'jycenter',
    u'version': u'V1.01.001.B.008',
    'serviceIp': '10.1.0.56'
}, {
    'status': 'On',
    u'dbversion': u'V1.10.15.R',
    'serviceName': 'middlecenterfile',
    u'version': u'V1.00.001.B.010',
    'serviceIp': '10.1.0.56'
}, {
    'status': 'On',
    'serviceName': 'middlecas',
    u'version': u'V1.02.002.B.007',
    'serviceIp': '10.1.0.56'
}, {
    'status': 'On',
    u'dbversion': u'V1.10.18.R',
    'serviceName': 'middlecenterres',
    u'version': u'V1.01.001.B.008',
    'serviceIp': '10.1.0.56'
}, {
    'status': 'On',
    'serviceName': 'middleclient',
    u'version': u'V2.01.001.B.011',
    'serviceIp': '10.1.0.56'
}]



def _queryStatus(*args):
    """
      Function: _queryStatus()
      Desc: request rest API get service information.
      Args:
         -
      Return: dict-> service status
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """

    urlhead, urlip, dockermodel, urltail = 'http://', args[0], args[
        1], '/version'
    requesturl = ''.join([urlhead, urlip, '/', dockermodel, urltail])
    logger.debug("Request URL is: {}".format(requesturl))
    serviceStatusInit = {
        'status': 'Off',
        'serviceIp': args[0],
        'serviceName': args[1]
    }
    try:
        r = requests.get(requesturl)
        # logger.debug(r)
        if r.status_code == 200:

            if not hasattr(r, 'text'):
                logger.info("failed")
            else:
                try:
                    result = json.loads(r.text)
                    servicetatus = dict(serviceStatusInit)
                    servicetatus.update(result)
                    if servicetatus.has_key('version'):
                        servicetatus['status'] = 'On'
                    else:
                        servicetatus['status'] = 'NoSuch'
                except ValueError:
                    servicetatus = dict(serviceStatusInit)
                    servicetatus['status'] = 'Off'
        else:
            servicetatus = dict(serviceStatusInit)
    except requests.exceptions.ConnectionError:
        servicetatus = dict(serviceStatusInit)
        servicetatus['status'] = 'ConnectionError'
    finally:
        return servicetatus


# def checkisRunning():
#     print isRunning(testflag)


def _isRunning(serviceStatus):
    """
      Function: _isRunning()
      Desc: 检查服务是否都On，检查到服务非正常状态，返回False，不会继续检查。
      Args: requests version API retruns dict(serviceStatus)
         - dict
      Return: False/None
      Usage: 
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """

    for flagtmp in serviceStatus:
        if flagtmp['status'] == 'On':
            logger.info('{0}: {1}'.format(flagtmp['serviceName'], flagtmp['status']))
        else:
            logger.info('{0}: {1}'.format(flagtmp['serviceName'], flagtmp['status']))
            return False


def _checkRunning(plathost):
    """
      Function: _checkRunning()
      Desc: 检查服务是否都正常，正常则返回True，不正常则重复检查最多5次。
      Args:
         - 
      Return: True/None
      Usage: 
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """
    arrstatus = []
    for serviceInfo in serviceInfos:
        arrstatus.append(_queryStatus(plathost, serviceInfo['serviceName']))

    for dotimes in range(5):
        logger.info("###################Service Status###################")
        if _isRunning(arrstatus) is not False:
            logger.info("Service is Running..")
            logger.info("####################################################")
            return True
        else:
            logger.info('sleep 120s..')
            sleep(120)
            logger.info("####################################################")


def t_status(plathost):
    """
      Function: _status()
      Desc: 通过_queryStatus()返回一个服务状态list
      Args:
         -
      Return:
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """

    arrstatus = []
    for serviceInfo in serviceInfos:
        arrstatus.append(_queryStatus(plathost, serviceInfo['serviceName']))
    return arrstatus


def checkRunner(plathost):
    return _checkRunning(plathost)

if __name__ == "__main__":
    # if isRunning(testflag) is False:
    #     print "no"
    # else:
    #     print "yes"
    # checkRunning()
    # print checkRunning()
    print t_status('10.1.41.12', serviceInfos)
