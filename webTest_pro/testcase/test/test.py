# coding: utf-8
import logging
import os
import sys
import unittest

from webTest_pro.testcase.test._env import addPaths
from webTest_pro.testcase.model.init import base_url

sys.path.append(os.path.dirname(os.getcwd()))

tenantData = [{'platmarkName': u'河南教育局','platmarkCode':'001'}]

logging.basicConfig(filename='G:\\00project\\aotuTest_pro\\webTest_pro\\testcase\\1.log', level=logging.DEBUG)

class tenantmanger(unittest.TestCase):
    '''租户管理场景'''

    def test_add_tenant(self):
        '''添加租户'''
        logging.debug("exec: test_add_tenant...")
        logging.info("exec: test_add_tenant...")
        logging.warning("exec: test_add_tenant...")
        logging.error("exec: test_add_tenant...")
        logging.critical("exec: test_add_tenant...")



if __name__ == '__main__':
    addPaths()
    print base_url
    for path in sys.path:
        print path
