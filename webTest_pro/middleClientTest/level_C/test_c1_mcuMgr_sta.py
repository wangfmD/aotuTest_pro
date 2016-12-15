# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_MCUequipments
from webTest_pro.common.model.baseActionDel import del_MCUequipment
from webTest_pro.common.model.baseActionSearch import search_MCUequipment
from webTest_pro.common.model.baseActionModify import update_Equipment
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

MCUequipments = [{'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'},
                 {'equipmentName': '95mcu', 'equipIpAddr': '10.1.0.95', 'mcu_port': '10000', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}]

equipmentData = [
    {'equipmentName': u'测试设备', 'equipIpAddr': '10.1.0.19', 'mcu_port': '80', 'mcuLoginName': 'zhangsan', 'mcuPasswd': '111111', 'softAgentIp': '10.1.4.33', 'softAgentPort': '80', 'bandWidth': '1000',
     'searchName': '85mcu'},
    {'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.19', 'mcu_port': '80', 'mcuLoginName': 'zhangsan', 'mcuPasswd': '111111', 'softAgentIp': '10.1.4.33', 'softAgentPort': '80', 'bandWidth': '1000',
     'searchName': u'测试设备'}]


class MCUequipmentmgr(unittest.TestCase):
    ''''MCU管理'''

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



if __name__ == '__main__':
    unittest.main()
