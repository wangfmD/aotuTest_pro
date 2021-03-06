# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_interacts
from webTest_pro.common.model.baseActionDel import del_interact
from webTest_pro.common.model.baseActionSearch import search_interact
from webTest_pro.common.model.baseActionModify import update_Middleware
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

interacts = [{'host': '10.1.0.2', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'},
             {'host': '10.1.0.3', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}]
middlewareData = [{'host': '1.1.0.1', 'port': '80', 'username': 'zhangsan', 'password': '111111', 'servicepath': '/interact', 'description': u'测试说明', 'searchName': '10.1.0.3'},
                  {'host': '10.1.0.3', 'port': '80', 'username': 'zhangsan', 'password': '111111', 'servicepath': '/interact', 'description': u'测试说明', 'searchName': '1.1.0.1'}]


class interactMgr(unittest.TestCase):
    ''''消息中间管理'''

    def setUp(self):
        if init.execEnv['execType'] == 'local':
            T_INFO(logger,"\nlocal exec testcase")
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            T_INFO(logger,"start tenantmanger...")
        else:
            T_INFO(logger,"\nremote exec testcase")
            browser = webdriver.DesiredCapabilities.CHROME
            self.driver = webdriver.Remote(command_executor=init.execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            T_INFO(logger,"start tenantmanger...")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        T_INFO(logger,"tenantmanger end!")

    def test_add_interacts(self):
        '''添加消息中间'''
        print "exec：test_add_interacts..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for interact in interacts:
            add_interacts(driver, **interact)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_interacts success."

    def test_bsearch_interacts(self):
        '''查询消息中间信息'''
        print "exec：test_search_interacts"

        driver = self.driver
        user_login(driver, **loginInfo)

        for interact in interacts:
            search_interact(driver, **interact)
            self.assertEqual(interact['host'],
                             driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr/td[2]").text)
        print "exec: test_search_interacts success."
        sleep(0.5)

    def test_bupdate_interacts(self):
        '''修改单条中心设备消息中间件数据'''
        print "exec：test_bupdate_interacts"

        driver = self.driver
        user_login(driver, **loginInfo)

        for interact in middlewareData:
            update_Middleware(driver, **interact)
        print "exec: test_bupdate_interacts success."
        sleep(0.5)

    def test_del_interacts_ok(self):
        '''删除消息中间_确定'''
        print "exec：test_del_interacts_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for interact in interacts:
            del_interact(driver, **interact)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_interacts_ok success."

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
