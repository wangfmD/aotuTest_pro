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
import unittest, json, requests
import config as config

from init.Oauth import getAccesssToken, headers
from init.initalize import returnValue, address_host, address_http, host

cfg = config.ConfigFile('test.cfg', ensure_ascii=False)
gParams = cfg.getValue(["post2"])
gIndex = 0

class LuaTest(unittest.TestCase):
    def setUp(self): 
        print '--------------开始--------------\n'
         
    def testComm(self):
          
        global gIndex
        print '--------------执行URl--------------\n'
#         获取token（str）
        access_str = getAccesssToken(address_host)  
        payload_1 = {'access_token': access_str}
        item = gParams[str(gIndex)]
        url,params = item['url'],item['params']
        gIndex += 1
        req = requests.post(address_http + host+ url, headers=headers, data=payload_1)
        print address_http + host+ url
        returnValue(self,req)
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
    cases = cfg.getValue(["post2"])
    for index, params in cases.iteritems():
        url_suffix = params['url'].split('/')[-1]
        funname = "test_%s_%s" % (url_suffix, index)
        exec("LuaTest.%s = LuaTest.testComm" % funname)
   
# def funcA(url, gParams):
#     gParamstr = ""
#     payload_1 = {'access_token': 'caf099ef-9c34-3af2-9ae1-e7264134e7e4'}
#     for key,value in gParams.iteritems():
#         gParamstr += "'%s'='%s'" % (key, value)
#         print gParamstr
#         
# for url,info in gParams:
#     funcA(url, info)
            
if __name__ == '__main__':
    unittest.main()
