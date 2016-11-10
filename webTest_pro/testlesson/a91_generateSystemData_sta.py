#  coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo, db_conf
from model.baseActionAdd import user_login, add_interacts, conf_local_interact, \
    conf_child_interact, add_MCUequipments, conf_drivers_local

reload(sys)
sys.setdefaultencoding("utf-8")

users = [{'loginName': 'user',
          'trueName': 'teacher'},
         {'loginName': 'user1',
          'trueName': 'teacher1'}]

MCUequipments = [{'equipmentName': '85mcu',
                  'equipIpAddr': '10.1.0.85',
                  'mcu_port': '80',
                  'mcuLoginName': 'POLYCOM',
                  'mcuPasswd': 'POLYCOM'},
                 {'equipmentName': '95mcu',
                  'equipIpAddr': '10.1.0.95',
                  'mcu_port': '10000',
                  'mcuLoginName': 'POLYCOM',
                  'mcuPasswd': 'POLYCOM'}]

middle_interact_ip = db_conf['hostadd']
child_interact_ip = '10.1.0.58'
middle_interacts = {'host': middle_interact_ip,
                    'port': '80',
                    'username': 'administrator',
                    'password': 'xungejiaoyu'}
child_interacts = {'host': child_interact_ip,
                   'port': '80',
                   'username': 'administrator',
                   'password': 'xungejiaoyu'}

MCUequipment = {'equipmentName': '85mcu',
                'equipIpAddr': '10.1.0.85',
                'mcu_port': '80',
                'mcuLoginName': 'POLYCOM',
                'mcuPasswd': 'POLYCOM'}

schools = []
school = {}


class generateSystemData(unittest.TestCase):
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
            self.driver = webdriver.Remote(command_executor=execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "generateSystemData end!"
        print "=" * 60

    def test_add_MCUequipments(self):
        '''添加MCU'''
        print "exec：test_add_MCUequipments..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for MCUequipment in MCUequipments:
            add_MCUequipments(driver, **MCUequipment)
            self.assertEqual(u"保存成功！", driver.find_element_by_css_selector /
                             (".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_MCUequipments success."

    def test_aconfLocalInteract(self):
        '''配置中心消息中间件'''
        print 'exec:test_confLocalInteract...'
        driver = self.driver
        user_login(driver, **loginInfo)
        add_interacts(driver, **middle_interacts)
        conf_local_interact(driver, middle_interact_ip)
        print 'exec:test_confLocalInteract end.'

    def test_confChildInteract(self):
        '''配置节点中间件'''
        print 'exec:test_confChildInteract...'
        driver = self.driver
        user_login(driver, **loginInfo)
        add_interacts(driver, **child_interacts)
        conf_child_interact(driver, child_interact_ip, middle_interact_ip)
        print 'exec:test_confChildInteract end.'

    def test_confMCU(self):
        '''配置节点中间件'''
        print 'Exec:test_confChildInteract...'
        driver = self.driver
        user_login(driver, **loginInfo)
        conf_drivers_local(driver)
        # conf_drivers_child(driver)
        print 'exec:test_confChildInteract end.'


if __name__ == '__main__':
    unittest.main()
