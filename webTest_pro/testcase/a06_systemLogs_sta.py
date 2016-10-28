# coding=utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.init import execEnv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from time import sleep
from model.baseActionAdd import user_login
from  model.baseActionSearch import search_systemLog
from model.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")

operaters = [{'user': 'hnsadmin'}]


class interactGroup(unittest.TestCase):
    ''''互动组管理'''

    def setUp(self):
        if execEnv['execType'] == 'local':
            print "\n", "=" * 20, "local exec testcase", "=" * 19
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."
        else:
            print "\n", "=" * 20, "remote exec testcase", "=" * 18
            browser = webdriver.DesiredCapabilities.CHROME
            self.driver = webdriver.Remote(command_executor=execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "schoolmanager end!"
        print "=" * 60

    def test_search_systemLog(self):
        '''查询系统日志信息'''
        print "exec：test_search_systemLog"
        driver = self.driver
        user_login(driver, **loginInfo)
        for operater in operaters:
            search_systemLog(driver, **operater)
            result = driver.find_element_by_xpath("//tbody[@id='systemLogs']/tr/td[3]").text
            self.assertEqual(operater['user'], result)
            print "search result: {}".format(result)
        print "exec: test_search_systemLog success."
        sleep(0.5)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            print e
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == '__main__':
    unittest.main()
