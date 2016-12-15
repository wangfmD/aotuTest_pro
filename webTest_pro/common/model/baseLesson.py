# -*- coding: utf-8 -*-
"""
     baseLesson.py
     Desc: begin lesson ect. action
     Maintainer: wangfm
     CreateDate: 2016-11-06 14:23:58
"""

from time import sleep
import requests
import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

# need to import log module, add env path
import sys, os
sys.path.append(os.environ.get('PY_DEV_HOME'))

from baseActionAdd import user_login
from webTest_pro.common.Oauth import getAccesssToken, headers

from webTest_pro.common.initData import init
from webTest_pro.common.mysqlKit import sqlOperating

#  sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
#  sys.path.append(os.getcwd())
base_url = init.base_url
db_conf = init.db_conf
loginInfo = init.loginInfo
reload(sys)
sys.setdefaultencoding('utf-8')

host = '10.1.0.46'


# 设置日志信息
#  LOG_INIT('log.log')
#  logger = LOG_MODULE_DEFINE('Platform')
#  SET_LOG_LEVEL(logger, 'info')


def queryLessonInfo(lessonName):
    """
      Func descriptions: query start lesson information
      Args: lesson name
      Return: CONFERENCE_ID, Lesson ID, classroom ID
      Usage: queryLessonInfo(lessonName)
      Author: wangfm
      Date: 2016-11-03 14:52:57
    """
    # 拼装查询SQL语句, lessonName为参数传入
    querySql = "select ID,CLASSROOM_ID,CONFERENCE_ID from interact_teach_lesson where LESSON_NAME='%s'" % lessonName
    # new 查询连接
    # c_query = sqlOperating()
    c_query = sqlOperating(db_conf['host'],
                           db_conf['user'],
                           db_conf['passwd'],
                           db_conf['db'])
    # 查询
    result = c_query.execQury(querySql)
    lessonInfo = {}
    for lie in result:
        # print dir(lie)
        # print lie
        lessonInfo.setdefault('lessonId', lie['ID'])
        lessonInfo.setdefault('classroomId', lie['CLASSROOM_ID'])
        lessonInfo.setdefault('conferenceId', lie['CONFERENCE_ID'])
    return lessonInfo


def beginJpk(driver, *args):
    """
      Func descriptions: 上精品课
      Args: webdriver
      Return: None
      Usage: beginJpk
      Author: wangfm
      Date: 2016-11-03 15:24:21
    """

    # user_login(driver, **loginInfo)
    lessonInfo = queryLessonInfo(args[0])
    lessonUrl = '/middleclient/pcManager/LessonPage.do?typeCode=1402&lessonId=' \
                + lessonInfo['lessonId'] + '&isZhu=1&classroomId=' + lessonInfo['classroomId'] \
                + '&interactType=false&created=0'
    print lessonUrl
    # get ip address from login URL
    ipAddress = urlparse.urlparse(driver.current_url).netloc
    print ipAddress
    driver.get('http://' + ipAddress + lessonUrl)
    sleep(10)
    print "TRACK ================= start"
    driver.find_element_by_xpath("//button[@id='pc_startButton']").click()
    print "end"


def beginConference(driver):
    """
      Function: beginConference()
      Desc:开始一场会议
      Args:
         - driver: webdriver
      Return: None
      Usage: beginConference(driver)
      Maintainer: wangfm
      CreateDate: 2016-11-04 11:43:15
    """
    user_login(driver, **loginInfo)
    #  conferenceInfo = queryLessonInfo('con_long')
    #  conferenceUrl = ''


def beginHdk():
    sql = "select ID,CLASSROOM_ID,CONFERENCE_ID from interact_teach_lesson where LESSON_NAME='hdk_long'"
    c_query = sqlOperating()
    result = c_query.execQury(sql)
    # print result['ID'], result['CLASSROOM_ID']
    # print result
    for lie in result:
        # print dir(lie)
        # print lie
        lessonId = lie['ID']
        classroomId = lie['CLASSROOM_ID']
        CONFERENCE_ID = lie['CONFERENCE_ID']
        print lessonId, classroomId, CONFERENCE_ID

    # h_ip = http://10.1.0.46
    h_ip = 'http://10.1.0.46'
    urlplus = '/interactbusiness/api/v1.0/mcu/checkLessonMcus'

    access_str = getAccesssToken(host)

    payload_1 = {'lessonId': lessonId,
                 'access_token': access_str}

    r = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
    print r.text
    agent = eval(r.text,
                 type('Dummy', (dict,),
                      dict(__getitem__=lambda s, n: n))())
    print agent['result']

    if agent['result'] == 'success':
        plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=' + lessonId + '&isZhu=1&classroomId=' + classroomId + '&interactType=false&created=0'
        # (//button[@id='requestDisconn_0000'])
        requestDisconn = "(//button[@id='requestDisconn_" + CONFERENCE_ID + "'])"
        # (//button[@id='requestConn_0000'])
        requestConn = "(//button[@id='requestConn_" + CONFERENCE_ID + "'])"
        print requestDisconn, requestConn
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        base_url = "http://10.1.0.46"

        # driver.get(base_url + plus_url)
        driver.get(base_url + "/middleclient/index.do")
        Select(driver.find_element_by_id("platform")).select_by_visible_text(
            u"河南教育局")
        driver.find_element_by_id("s_username").clear()
        driver.find_element_by_id("s_username").send_keys("hnsadmin")
        driver.find_element_by_id("s_password").clear()
        driver.find_element_by_id("s_password").send_keys("111111")
        # 登录
        driver.find_element_by_name("submit").click()
        driver.maximize_window()
        sleep(2)
        driver.get(base_url + plus_url)
        sleep(8)
        # 开课
        driver.find_element_by_id("pc_startButton").click()
        sleep(25)
        while True:
            try:
                driver.find_element_by_xpath(requestDisconn + "[2]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestDisconn + "[3]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestDisconn + "[4]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(3)
            try:
                driver.find_element_by_xpath(requestDisconn + "[5]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestDisconn + "[6]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[7]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestDisconn).click()
            except StaleElementReferenceException as e:
                print e
            sleep(10)
            try:
                driver.find_element_by_xpath(requestConn).click()
            except StaleElementReferenceException as e:
                print e
            sleep(20)
            try:
                driver.find_element_by_xpath(requestConn + "[2]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestConn + "[3]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestConn + "[4]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestConn + "[5]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath(requestConn + "[6]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(2)
            try:
                driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[7]").click()
            except StaleElementReferenceException as e:
                print e
            sleep(15)

        sleep(300000)
        # 开课
        driver.find_element_by_id("pc_startButton").click()
        sleep(10)
    else:
        print "上课信息为空！"


    #  if __name__ == '__main__':
    #  aad_lesson()
    #  login()
    #  print base_url
    #  print queryLessonInfo("jpk")
    #  driver = webdriver.Chrome()

    #  beginJpk(driver)


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # beginJpk(driver, 'jpk')
    lessonInfo = queryLessonInfo('jpk')
    print lessonInfo
