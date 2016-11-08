# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
from mysqlKit import sqlOperating, sqlpara
from InitData import user_login
from Oauth import getAccesssToken, headers
from init import base_url, db_conf
import requests, sys
reload(sys)
sys.setdefaultencoding('utf-8')

host = db_conf['host']


def login():

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

    h_ip = base_url
    urlplus = '/interactbusiness/api/v1.0/mcu/checkLessonMcus'

    access_str = getAccesssToken(host)

    payload_1 = {'lessonId': lessonId,
                 'access_token': access_str}

    r = requests.post(h_ip + urlplus, headers=headers, data=payload_1)
    print r.text
    agent = eval(r.text,
                 type('Dummy', (dict, ),
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
        # base_url = "http://10.1.0.57"
        verificationErrors = []
        accept_next_alert = True
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
            # try:
            #     driver.find_element_by_xpath(requestDisconn + "[4]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(3)
            # try:
            #     driver.find_element_by_xpath(requestDisconn + "[5]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(2)
            # try:
            #     driver.find_element_by_xpath(requestDisconn + "[6]").click()
            # except StaleElementReferenceException as e:
            #     print e
            sleep(2)
            # try:
            #     driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[7]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(2)
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
            # try:
            #     driver.find_element_by_xpath(requestConn + "[4]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(2)
            # try:
            #     driver.find_element_by_xpath(requestConn + "[5]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(2)
            # try:
            #     driver.find_element_by_xpath(requestConn + "[6]").click()
            # except StaleElementReferenceException as e:
            #     print e
            # sleep(2)
            # try:
            #     driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[7]").click()
            # except StaleElementReferenceException as e:
            #     print e
            sleep(15)

        sleep(300000)
        # 开课
        driver.find_element_by_id("pc_startButton").click()
        sleep(10)
    else:
        print "上课信息为空！"


#
if __name__ == '__main__':
    # aad_lesson()
    login()
    # print base_url
