# coding: utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

tenantData = [{'platmarkName': u'河南教育局','platmarkCode':'001'}]


class tenantmanger(unittest.TestCase):
    '''租户管理场景'''

    def test_add_tenant(self):
        '''添加租户'''
        print "exec: test_add_tenant..."


if __name__ == '__main__':
    unittest.main()
