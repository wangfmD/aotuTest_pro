# coding=utf-8
import sys
import os
import unittest

from testcase.model.baseActionAdd import user_login

sys.path.append(os.path.dirname(os.getcwd()))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchFrameException, NoAlertPresentException, NoSuchElementException
import re
from time import sleep
from init import base_url

reload(sys)
sys.setdefaultencoding("utf-8")


def test_modify_terminal(driver):
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(1)
    driver.find_element_by_link_text("32className").click()
    sleep(1)
    driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    # click modify button

    # driver.find_element_by_xpath("//button[@onclick=\"javascript:updateSchoolEquipment('ac5899d7-ef54-4457-a822-c1b82ed5adf8','0302'),$('#terminalupdate').modal({backdrop: 'static', keyboard: false});\"]").click()
    # driver.find_element_by_xpath("(//input[@name='isgkup'])[2]").click()
    # driver.find_element_by_xpath("(//input[@name='isIngkup'])[2]").click()
    driver.find_element_by_xpath("//table[@id='schoolequipmenttab']/tbody/tr[2]/td[10]/button[2]").click()
    # if t_button.is_displayed():
    #     print "Element is  displayed!"
    # else:
    #     print  "Element is not  displayed!"
    # sleep(1)
    # driver.find_element_by_xpath("(//input[@name='isIngkup'])[2]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[37]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[37]").send_keys(u"10.1.0.81终端mod")
    driver.find_element_by_xpath("(//input[@type='text'])[38]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[38]").send_keys("10.1.0.1")
    driver.find_element_by_xpath("(//input[@type='text'])[39]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[39]").send_keys("10.1.0.1")
    driver.find_element_by_xpath("(//input[@type='text'])[40]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[40]").send_keys("admin1")
    driver.find_element_by_xpath("(//input[@type='text'])[41]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[41]").send_keys("admin1")
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").clear()
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").send_keys("11")
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").clear()
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").send_keys("11bz")
    # click OK button
    driver.find_element_by_xpath("(//button[@id='submit'])[7]").click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")
    test_modify_terminal(driver)
