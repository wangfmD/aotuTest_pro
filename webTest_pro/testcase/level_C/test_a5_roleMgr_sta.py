# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_roles
from model.baseActionModify import update_roleManagement

reload(sys)
sys.setdefaultencoding("utf-8")

roles = [{'roleName': 'a2role1', 'roleCode': '1', 'description': 'comment role'}]

roleData = [{'roleName': u'奥数组','roleCode':'001','description':u'说明测试数据','searchName':'a2role2'}]


class roleMgr(unittest.TestCase):
    ''''角色管理'''

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

    def test_add_role(self):
        '''添加角色'''
        print "exec：test_add_role..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for role in roles:
            add_roles(driver, **role)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_role success."

		
    def test_update_role(self):
        '''修改角色'''
        print "exec：test_update_role..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for role in roleData:
            update_roleManagement(driver, **role)
            # self.assertEqual(u"修改成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_role success."
    # def test_bsearch_role(self):
    #     '''修改教室信息'''
    #     print "exec：test_search_role"
    #
    #     driver = self.driver
    #     user_login(driver, **loginInfo)
    #     for user in users:
    #         search_user(driver, **user)
    #         self.assertEqual(user['loginName'],
    #                          driver.find_element_by_xpath("//tbody[@id='userlists']/tr/td[3]").text)
    #     print "exec: test_search_role success."
    #     sleep(0.5)

    # def test_del_role_ok(self):
    #     '''删除科目组_确定'''
    #     print "exec：test_del_role_ok..."
    # 
    #     driver = self.driver
    #     user_login(driver, **loginInfo)
    # 
    #     for role in roles:
    #         del_role(driver)
    #         self.assertEqual(u"删除成功", driver.find_element_by_css_selector(".layui-layer-content").text)
    #         sleep(0.5)
    #     print "exec：test_del_role_ok success."

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
