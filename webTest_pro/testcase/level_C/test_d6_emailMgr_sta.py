# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_emails
from model.baseActionDel import del_email
from model.baseActionModify import update_Smtp

reload(sys)
sys.setdefaultencoding("utf-8")

emails = [{'smtp': 'smtp.162.com', 'fromName': 'haosea@qq.com', 'password': '111111'},
          {'smtp': 'smtp.qq.com', 'fromName': 'haosea1@qq.com', 'password': '111111'}]
smtpData = [{'smtp': u'smtp.163.com','fromName':'519484955@qq.com','password':'111111'}]


class emailMgr(unittest.TestCase):
    ''''邮件服务器管理'''

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
        print "emailMgr end!"
        print "=" * 60

    def test_add_emails(self):
        '''添加邮件服务器'''
        print "exec：test_add_emails..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for email in emails:
            add_emails(driver, **email)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_emails success."

		
    def test_update_emails(self):
        '''修改邮件服务器'''
        print "exec：test_update_emails..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for email in smtpData:
            update_Smtp(driver, **email)
        sleep(0.5)
        print "exec：test_update_emails success."

    def test_del_emails(self):
        '''删除邮件服务器_确定'''
        print "exec：test_del_emails..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for email in emails:
            del_email(driver)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_emails success."

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
    unittest.main()
