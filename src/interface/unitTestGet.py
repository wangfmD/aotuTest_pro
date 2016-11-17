#!/usr/bin/python2.7
#coding=utf8
r'''
Fuction: 
Version: 1.0.0
Created: Tuyj
Created date:2015/4/1
'''
from _env import addPaths
addPaths(".")
import config,requests
import unittest,json

import init.initalize as initalize
from init.Oauth import getAccesssToken, headers


cfg = config.ConfigFile('test.cfg', ensure_ascii=False)
gParams = cfg.getValue(["get"])

class LuaTest(unittest.TestCase):
    def setUp(self): 
        print '--------------开始--------------\n'
        
    def testComm(self):
         
        global gIndex
        print '--------------执行URl--------------\n'
#         获取token（str）
        access_str = getAccesssToken(initalize.address_host)  
        payload_1 = {'access_token': access_str}
        item = gParams[str(gIndex)]
        url,params = item['url'],item['params']
        gIndex += 1
        req = requests.get(initalize.address_http + initalize.host+ url, headers=headers, params=payload_1)
        initalize.returnValue(self,req)
        #47 重复的  已经删掉   下次添加
        if url=="/oauth_api/v1/auth/role/query":
            s = json.loads(req.text) 
            uuid = s["rows"][0]["uuid"]
            name = cfg.getValue(['post2', '0', 'params', 'roleName'])
            cfg.setValue(['post2', "10", "params", "uuid"], uuid, True)
       
       
    def tearDown(self):
        print '--------------结束--------------\n'


loaded = False
if not loaded:
    loaded = True
    funname = "test_name"
    for i in xrange(0, len(gParams)-1):
        fn = funname + str(i)
        exec("LuaTest.%s = LuaTest.testComm" % fn)
   

if __name__ == '__main__':
#     print getAccesssToken("10.1.0.57")
    unittest.main()

    
    