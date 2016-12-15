# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_groupsubGrps
from webTest_pro.common.model.baseActionDel import del_subjectGrp
from webTest_pro.common.model.baseActionSearch import search_subjectGrp
from webTest_pro.common.model.baseActionModify import update_subjectGrp
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

schools = [{'schoolName': u'二中', 'schoolType': u'高中', 'schoolArea': u'郑州市'},
           {'schoolName': u'三中', 'schoolType': u'中学', 'schoolArea': u'郑州市'},
           {'schoolName': u'四中', 'schoolType': u'中学', 'schoolArea': u'开封市'},
           {'schoolName': u'五中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'六中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'一中', 'schoolType': u'高中', 'schoolArea': u'郑州市'}]

classrooms = [{'className': '31className', 'classAccNumber': '1'},
              {'className': '32className', 'classAccNumber': '1'}]
modifyClassRoom = {'className': '32classNamemodify', 'classAccNumber': '100'}

subjectsGroups = [{'groupName': u'计算机', 'groupCode': '001', 'description': u'计算机'},
                  {'groupName': u'物理', 'groupCode': '002', 'description': u'物理'}]

searchsubjectGrps = [{'groupName': u'计算机'},
                     {'groupName': u'物理'}]

modifysubjectsGroup = [{'groupName': u'计算机modif', 'groupCode': '0101', 'description': u'计算机modif', 'searchName': u'计算机'}]


class schoolgroupmanager(unittest.TestCase):
    ''''科目组管理'''

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

    def test_add_subjectgrp(self):
        '''添加教室'''
        print "exec：test_add_subjectgrp..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for subjectsGroup in subjectsGroups:
            add_groupsubGrps(driver, **subjectsGroup)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_subjectgrp success."

    def test_bsearch_subjectgrp(self):
        '''查询教室信息'''
        print "exec：test_bsearch_subjectgrp"

        driver = self.driver
        user_login(driver, **loginInfo)
        for searchsubjectGrp in searchsubjectGrps:
            search_subjectGrp(driver, **searchsubjectGrp)
            self.assertEqual(searchsubjectGrp['groupName'],
                             driver.find_element_by_xpath("//table[@id='SchoolGroupmodaltab']/tbody/tr/td").text)
        print "exec test_bsearch_subjectgrp success"
        sleep(0.5)

    def test_bupdate_subjectgrp(self):
        '''修改组管理'''
        print "exec：test_bupdate_subjectgrp"

        driver = self.driver
        user_login(driver, **loginInfo)
        for itme in modifysubjectsGroup:
            update_subjectGrp(driver, **itme)
        print "exec test_bupdate_subjectgrp success"
        sleep(0.5)

    def test_del_subjectgrp_ok(self):
        '''删除科目组_确定'''
        print "exec：test_del_subjectgrp_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for searchsubjectGrp in searchsubjectGrps:
            del_subjectGrp(driver, **searchsubjectGrp)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_subjectgrp_ok success."

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
