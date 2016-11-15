#  coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver

from _env import addPaths

addPaths('.')
from common.log.t_log import LOG_INIT, LOG_MODULE_DEFINE, SET_LOG_LEVEL, L_INFO
from common.init import execEnv, loginInfo, db_conf, child_interact_ip
from common.init import logFile
from model.baseActionAdd import user_login, add_interacts, conf_interact_local, \
    add_MCUequipments, conf_drivers_local

reload(sys)
sys.setdefaultencoding("utf-8")

LOG_INIT(logFile)
logger = LOG_MODULE_DEFINE('Platform')
SET_LOG_LEVEL(logger, 'info')

MCUequipments = [{
    'equipmentName': '85mcu',
    'equipIpAddr': '10.1.0.85',
    'mcu_port': '80',
    'mcuLoginName': 'POLYCOM',
    'mcuPasswd': 'POLYCOM'
}, {
    'equipmentName': '95mcu',
    'equipIpAddr': '10.1.0.95',
    'mcu_port': '10000',
    'mcuLoginName': 'POLYCOM',
    'mcuPasswd': 'POLYCOM'
}]

middle_interact_ip = db_conf['hostadd']
child_interact_ip = child_interact_ip
middle_interacts = {
    'host': middle_interact_ip,
    'port': '80',
    'username': 'administrator',
    'password': 'xungejiaoyu'
}
child_interacts = {
    'host': child_interact_ip,
    'port': '80',
    'username': 'administrator',
    'password': 'xungejiaoyu'
}

MCUequipment = {
    'equipmentName': '85mcu',
    'equipIpAddr': '10.1.0.85',
    'mcu_port': '80',
    'mcuLoginName': 'POLYCOM',
    'mcuPasswd': 'POLYCOM'
}


class addDriversData(unittest.TestCase):
    ''''学校教室设备基础数据添加'''

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
            self.driver = webdriver.Remote(
                command_executor=execEnv['remoteUrl'],
                desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "generateSystemData end!"
        print "=" * 60

    def test_aconfLocalInteract(self):
        '''添加配置中心消息中间件'''
        print 'exec:test_confLocalInteract...'
        L_INFO(logger, "添加消息中间件")
        driver = self.driver
        user_login(driver, **loginInfo)
        add_interacts(driver, **middle_interacts)
        conf_interact_local(driver, middle_interact_ip)
        print 'exec:test_confLocalInteract end.'

        # def test_confChildInteract(self):
        # '''配置节点中间件'''
        # print 'exec:test_confChildInteract...'
        # driver = self.driver
        # user_login(driver, **loginInfo)
        # add_interacts(driver, **child_interacts)
        # conf_child_interact(driver, child_interact_ip, middle_interact_ip)
        # print 'exec:test_confChildInteract end.'

    def test_add_MCUequipments(self):
        '''添加MCU'''
        print "exec：test_add_MCUequipments..."
        L_INFO(logger, "添加MCU")
        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in MCUequipments:
            add_MCUequipments(driver, **MCUequipment)
        # self.assertEqual(u"保存成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_MCUequipments success."

    def test_confMCU(self):
        '''配置节点中间件'''
        print 'Exec:test_confChildInteract...'
        L_INFO(logger, "配置消息中间件管理的设备")
        driver = self.driver
        user_login(driver, **loginInfo)
        conf_drivers_local(driver)
        # conf_drivers_child(driver)
        print 'exec:test_confChildInteract end.'


if __name__ == '__main__':
    unittest.main()
    # print logFile
    # test_MCUequipments()
