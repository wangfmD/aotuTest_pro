# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_classrooms
from model.baseActionDel import del_classroom
from model.baseActionModify import modify_classrooms

reload(sys)
sys.setdefaultencoding("utf-8")


schools = [{'schoolName': u'二中', 'schoolType': u'高中', 'schoolArea': u'郑州市'},
           {'schoolName': u'三中', 'schoolType': u'中学', 'schoolArea': u'郑州市'},
           {'schoolName': u'四中', 'schoolType': u'中学', 'schoolArea': u'开封市'},
           {'schoolName': u'五中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'六中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'一中', 'schoolType': u'高中', 'schoolArea': u'郑州市'}]

classrooms = [{'className': '31className', 'classAccNumber': '1'},
              {'className': '32className', 'classAccNumber': '1'}]
modifyClassRoom = {'className': '32classNamemodify', 'classAccNumber': '100'}


class schoolmanager(unittest.TestCase):
    ''''教室管理'''

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

    def test_add_school(self):
        '''添加教室'''
        print "执行：添加教室"

        driver = self.driver
        user_login(driver, **loginInfo)

        for classroom in classrooms:
            add_classrooms(driver, **classroom)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)

    def test_cmodify_school(self):
        '''修改教室信息'''
        print "exec：test_modify_school"

        driver = self.driver
        user_login(driver, **loginInfo)
        modify_classrooms(driver, **modifyClassRoom)
        self.assertEqual(u"修改成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        print "exec：test_modify_school success."

        sleep(0.5)

    def test_del_school_cancel(self):
        '''删除学校_取消'''
        print "执行：删除学校_取消"

        driver = self.driver
        user_login(driver, **loginInfo)

        for classroom in classrooms:
            del_classroom(driver)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
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
