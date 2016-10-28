# coding=utf-8

import os
import sys
import unittest

from selenium import webdriver

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.init import execEnv
from model.baseActionAdd import user_login, add_interacts, conf_local_interact, conf_child_interact, conf_mcu
from model.init import loginInfo, db_conf

reload(sys)
sys.setdefaultencoding("utf-8")

users = [{'loginName': 'user', 'trueName': 'teacher'},
         {'loginName': 'user1', 'trueName': 'teacher1'}]

middle_interact_ip = db_conf['hostadd']
child_interact_ip = '10.1.0.45'
middle_interacts = {'host': middle_interact_ip, 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}
child_interacts = {'host': child_interact_ip, 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}

MCUequipment = {'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}

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
        # add_MCUequipments(driver, **MCUequipment)
        conf_mcu(driver)
        print 'exec:test_confChildInteract end.'

if __name__ == '__main__':
    unittest.main()
