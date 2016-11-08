# _*_ coding: utf-8 _*_
"""
__title__ = ""
__auther__ = "acer"
__mtime__ = "2016/10/24"
"""

import unittest

from selenium import webdriver

from model.baseActionAdd import user_login, add_excellentClass
from model.baseActionDel import del_excellentClass
from model.init import loginInfo


class excellentClass(unittest.TestCase):
    def setUp(self):
        print "--"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.verificationErrors = []
        self.accept_next_alert = True
        print "\n", "=" * 60
        print "start excellentClass..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "tenantmanger end!"
        print "=" * 60

    def test_add_excellentLesson(self):
        '''添加精品课'''
        print "exec:test_add_excellentLesson..."
        driver = self.driver
        user_login(driver, **loginInfo)

        add_excellentClass(driver)
        print "exec:test_add_excellentLesson end."

    def test_del_excellentLesson(self):
        '''删除精品课'''
        print "exec:excellentLesson..."
        driver = self.driver
        user_login(driver, **loginInfo)
        # del excellentClass
        del_excellentClass(driver)
        print "exec:excellentLesson end."

    def test_add_jpk(self):
        '''生成精品课堂数'''

        print "exec: generate jplk start..."
        driver = self.driver
        user_login(driver, **loginInfo)

        add_excellentClass(driver)
        print "exec: generate jpk end."



if __name__ == '__main__':
    unittest.main()
