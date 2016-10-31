# coding=utf-8

import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.init import execEnv
from model.baseActionAdd import user_login, add_MCUequipments
from model.baseActionDel import del_MCUequipment
# from model.baseActionModify import 
from  model.baseActionSearch import search_MCUequipment
from  model.baseActionModify import update_Equipment
from model.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")

MCUequipments = [{'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'},
                 {'equipmentName': '95mcu', 'equipIpAddr': '10.1.0.95', 'mcu_port': '10000', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}]

equipmentData = [{'equipmentName': u'测试设备', 'equipIpAddr': '10.1.0.19', 'mcu_port': '80', 'mcuLoginName': 'zhangsan', 'mcuPasswd': '111111', 'softAgentIp': '10.1.4.33', 'softAgentPort': '80', 'bandWidth': '1000', 'searchName': '85mcu'},
                 {'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.19', 'mcu_port': '80', 'mcuLoginName': 'zhangsan', 'mcuPasswd': '111111', 'softAgentIp': '10.1.4.33', 'softAgentPort': '80', 'bandWidth': '1000', 'searchName': u'测试设备'}]


class MCUequipmentmgr(unittest.TestCase):
    ''''MCU管理'''

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
        print "MCUequipmentmgr end!"
        print "=" * 60

    def test_add_MCUequipments(self):
        '''添加MCU'''
        print "exec：test_add_MCUequipments..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in MCUequipments:
            add_MCUequipments(driver, **MCUequipment)
            self.assertEqual(u"保存成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_MCUequipments success."

    def test_bsearch_MCUequipment(self):
        '''查询MCU信息'''
        print "exec：test_search_MCUequipment"

        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in MCUequipments:
            search_MCUequipment(driver, **MCUequipment)
            self.assertEqual(MCUequipment['equipmentName'],
                             driver.find_element_by_xpath("//table[@id='centermcutab']/tbody/tr/td[4]").text)
        print "exec: test_search_MCUequipment success."
        sleep(0.5)

    def test_bupdate_MCUequipment(self):
        '''查询中心设备MCU信息'''
        print "exec：test_bupdate_MCUequipment"

        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in equipmentData:
            update_Equipment(driver, **MCUequipment)
        print "exec: test_bupdate_MCUequipment success."
        sleep(0.5)

    def test_del_MCUequipment_ok(self):
        '''删除MCU_确定'''
        print "exec：test_del_MCUequipment_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in MCUequipments:
            del_MCUequipment(driver, **MCUequipment)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_MCUequipment_ok success."

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
