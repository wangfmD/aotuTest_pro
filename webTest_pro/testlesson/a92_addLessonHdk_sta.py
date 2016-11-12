# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_lesson

reload(sys)
sys.setdefaultencoding("utf-8")



class interActiveTeachingMgr(unittest.TestCase):
    ''''课程管理'''

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
        print "interActiveTeachingMgr end!"
        print "=" * 60

    def test_add_hdk(self):
        '''添加互动课'''
        print "exec：test_add_hdk..."

        driver = self.driver
        user_login(driver, **loginInfo)
        add_lesson(driver)
        sleep(5)

        print "exec：test_add_hdk success."


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
    # main = unittest.main()
    print loginInfo
