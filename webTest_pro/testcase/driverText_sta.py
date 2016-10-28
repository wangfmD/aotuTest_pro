# coding=utf-8

import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.baseActionAdd import user_login, add_emails,add_lesson
from model.baseActionDel import del_email
from model.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")

emails = [{'smtp': 'smtp.162.com', 'fromName': 'haosea@qq.com', 'password': '111111'},
          {'smtp': 'smtp.163.com', 'fromName': 'haosea1@qq.com', 'password': '111111'}]


class interActiveTeachingMgr(unittest.TestCase):
    ''''课程管理'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        print "\n", "=" * 60
        print "interActiveTeachingMgr_..."

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
        sleep(500)

        print "exec：test_add_hdk success."

    # def test_del_emails(self):
    #     '''删除邮件服务器_确定'''
    #     print "exec：test_del_emails..."
    # 
    #     driver = self.driver
    #     user_login(driver, **loginInfo)
    # 
    #     for email in emails:
    #         del_email(driver)
    #         sleep(1.5)
    #         self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
    #         sleep(0.5)
    #     print "exec：test_del_emails success."

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
    main = unittest.main()
