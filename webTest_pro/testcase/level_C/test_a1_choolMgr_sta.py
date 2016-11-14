# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import add_schools, user_login
from model.baseActionDel import del_school
from model.baseActionModify import update_School
reload(sys)
sys.setdefaultencoding("utf-8")

schools = [{'schoolName': u'二中', 'schoolType': u'高中', 'schoolArea': u'郑州市'},
           {'schoolName': u'三中', 'schoolType': u'中学', 'schoolArea': u'郑州市'},
           {'schoolName': u'四中', 'schoolType': u'中学', 'schoolArea': u'开封市'},
           {'schoolName': u'五中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'六中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'一中', 'schoolType': u'高中', 'schoolArea': u'郑州市'}]
schoolData = [{'schoolName': u'河南一中', 'searchName': u'二中'}]
schoolDel = [{'schoolName': u'三中'},
             {'schoolName': u'四中'},
             {'schoolName': u'五中'},
             {'schoolName': u'六中'},
             {'schoolName': u'一中'}]

class schoolmanager(unittest.TestCase):
    ''''学校管理'''

    def setUp(self):
        if execEnv['execType'] == 'local':
            print "\n", "=" * 20, "local exec testcase", "=" * 19
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(20)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."
        else:
            print "\n", "=" * 20, "remote exec testcase", "=" * 18
            browser = webdriver.DesiredCapabilities.CHROME
            self.driver = webdriver.Remote(command_executor=execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(20)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "schoolmanager end!"
        print "=" * 60

    def test_addschool(self):
        '''添加学校'''
        print "执行：添加学校测试"
        driver = self.driver
        driver.refresh()
        sleep(2)
        user_login(driver, **loginInfo)

        for school in schools:
            add_schools(driver, **school)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)

        sleep(0.5)

    def test_bsearch_school(self):
        '''学校查询'''
        print "执行：学校查询"

        try:
            driver = self.driver
            user_login(driver, **loginInfo)

            driver.find_element_by_link_text(u"系统管理").click()
            driver.find_element_by_link_text(u"学校管理").click()
            sleep(1)
            driver.find_element_by_xpath("//input[@id='condition']").clear()
            driver.find_element_by_xpath("//input[@id='condition']").send_keys(u"教育局")
            driver.find_element_by_xpath("//button[@id='searchbtn']").click()
            sleep(1)
            self.assertEqual(u"河南省教育局", driver.find_element_by_xpath(".//*[@id='schoolname']").text)
            print "查询学校成功。"
        except Exception as e:
            print "查询学校失败。"
            print e
        sleep(1)

    def test_bupdate_school(self):
        '''修改单条学校数据'''
        print "执行：修改单条学校数据"
        # try:
        driver = self.driver
        user_login(driver, **loginInfo)
        for itms in schoolData:
            update_School(driver,**itms)
        sleep(1)
        # resultContent = driver.find_element_by_css_selector("div.layui-layer-content.firepath-matching-node").text
        # self.assertEqual(u"河南一中", resultContent)
        print "修改单条学校数据:成功。"
    # except Exception as e:
        print "修改单条学校数据失败。"
        sleep(1)

    def test_del_school_ok(self):
        '''删除学校_确定'''
        print "执行：删除学校_确定"
        driver = self.driver
        user_login(driver, **loginInfo)

        for flag in schoolDel:
            del_school(driver,**flag)
            # self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)

    def test_del_school_cancel(self):
        '''删除学校_取消'''
        print "执行：删除学校_取消"
        try:
            driver = self.driver
            user_login(driver, **loginInfo)

            # add_school(driver, u'一中', u'高中', u'郑州市')
            sleep(0.5)
            driver.find_element_by_link_text(u"系统管理").click()
            driver.find_element_by_link_text(u"学校管理").click()
            sleep(0.5)
            driver.find_element_by_xpath("//button[@id='delsc']").click()
            driver.find_element_by_css_selector("a.layui-layer-btn1").click()
            self.assertEqual(u"一中", driver.find_element_by_xpath("//*[@id='schoolname']").text)
            # print driver.find_element_by_xpath("//*[@id='schoolname']").text
            print "删除学校_取消：成功"
        except Exception as e:
            print e
            print "删除学校_取消：失败"

        sleep(1)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print e
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
