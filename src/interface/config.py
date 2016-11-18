#!/usr/bin/python2.7
#coding=utf8
r'''
Fuction: 
Version: 1.0.0
Created: Tuyj
Created date:2015/4/1
'''
from  _env import addPaths
addPaths(".")
import json,datetime,os,re,shutil,copy,threading,unittest

import pyLibs.t_com as t_com
import pyLibs.t_multitask as t_multitask


def geSmartNowTime(): #return yyyymmddHHMMSS.mirsec
    timenow = datetime.datetime.now()
    return "%04d%02d%02d%02d%02d%02d.%02s" % (timenow.year,timenow.month,timenow.day,timenow.hour,timenow.minute,timenow.second,str(timenow.microsecond)[:2])

class ConfigFile:
    def __init__(self, full_filename, indent=2, smart=False, tasker=None, intervals=(3, 2, 2), ensure_ascii=True):
        self.filename,self.indent,self.smart,self.tasker = full_filename,indent,smart,tasker
        self.autoSaveInv,self.deletelastBad,self.deletelastBak = intervals
        self.autoSaveInv = self.autoSaveInv if self.autoSaveInv > 0 else 3
        self.is_ext_tasker = True
        self.entrys = None
        self.changed = False
        self.gen_auto_flush = None
        self.rlock = threading.RLock()
        self.ensure_ascii = ensure_ascii

        if os.path.isdir(self.filename):
            raise ValueError('cfg file is must be file')
        if not os.path.exists(self.filename):
            fp = open(self.filename, 'w')
            fp.write('{}')
            fp.close()
        fp = open(self.filename, 'r')
        try:
            self.entrys = json.load(fp)
            fp.close()
        except Exception as ex:
            fp.close()
            if not self.smart or not self.__auto_fix():
                raise ex
            fp = open(self.filename, 'r')
            self.entrys = json.load(fp)
            fp.close()

        if smart and self.tasker is None:
            self.tasker = t_multitask.tMultitaskMgr('cfg-tasker@'+self.filename)
            self.tasker.run(t_com.default_mini_thread_stack_size)
            self.is_ext_tasker = False
        if self.tasker is not None:
            self.gen_auto_flush = self._g_auto_flush()
            self.tasker.add(self.gen_auto_flush)

    def __del__(self):
        self.stop()

    def stop(self):
        self.rlock.acquire()
        self.__flush2file()
        self.rlock.release()
        if self.gen_auto_flush is not None:
            self.gen_auto_flush.close()
            self.gen_auto_flush = None
        if self.tasker is not None and not self.is_ext_tasker:
            self.tasker.stop()
            self.tasker = None

    def Entrys(self):
        self.rlock.acquire()
        rout = copy.deepcopy(self.entrys)
        self.rlock.release()
        return rout

    def Save(self, force=False):
        self.rlock.acquire()
        self.__flush2file(force)
        self.rlock.release()

    def getValue(self, domains, default=None):
        '''e.g. file:
        {
            'China': {'JiangSu': 2014, 'XiangHai': 2015},
            'Japan': {...}
        }
        domains = ['China', 'XiangHai'] -> return 2015
        '''
        if not isinstance(domains, list):
            raise ValueError('domains MUST be list')

        self.rlock.acquire()
        found = self.entrys
        for domain in domains:
            if found.has_key(domain):
                found = found[domain]
            else:
                self.rlock.release()
                return default
        if isinstance(found, list) or isinstance(found, dict): #TODO:ok?
            out = copy.deepcopy(found)
            self.rlock.release()
            return out
        self.rlock.release()
        return found

    def setValue(self, domains, value, save=True):
        if not isinstance(domains, list):
            raise ValueError('domains MUST be list')
        keys,lastkey = domains[:-1],domains[-1]

        self.rlock.acquire()
        catched = self.entrys
        for domain in keys:
            if not catched.has_key(domain):
                catched[domain] = {}
            catched = catched[domain]
        if catched.has_key(lastkey):
            if catched[lastkey] == value:
                self.rlock.release()
                return
        if isinstance(value, list) or isinstance(value, dict): #TODO:ok?
            catched[lastkey] = copy.deepcopy(value)
        else:
            catched[lastkey] = value
        self.changed = True
        if save and not self.smart:
            self.__flush2file()
        self.rlock.release()

    def _g_auto_flush(self):
        while True:
            yield t_multitask.sleep(self.autoSaveInv)
            self.rlock.acquire()
            self.__flush2file()
            self.rlock.release()

    def __flush2file(self, force=False):
        if self.changed or force:
            self.__auto_bak()
            fp = open(self.filename, 'w')
            json.dump(self.entrys, fp, indent=self.indent, ensure_ascii=self.ensure_ascii)
            fp.close()
            self.changed = False

    def __auto_bak(self):
        path = os.path.dirname(self.filename)
        name = os.path.basename(self.filename)
        if path == '':
            path = './'
        files = os.listdir(path)
        baks = []
        for file_ in files:
            if not os.path.isfile(os.path.join(path, file_)):
                continue
            m = re.match(r'^.%s.(\d+\.\d+)$' % name, file_)
            if m is None:
                continue
            baks.append(m.groups()[0])
        baks.sort(reverse=True)
        while len(baks) >= self.deletelastBak:
            oldest = '.%s.%s' % (name,baks.pop())
            oldest = os.path.join(path, oldest)
            os.remove(oldest)
        bak_name = '.%s.%s' % (name, geSmartNowTime())
        shutil.copyfile(self.filename, os.path.join(path, bak_name))

    def __auto_fix(self):
        path = os.path.dirname(self.filename)
        name = os.path.basename(self.filename)
        files = os.listdir(path)
        baks = []
        bads = []
        for file_ in files:
            if not os.path.isfile(os.path.join(path, file_)):
                continue
            m = re.match(r'^%s.\d+\.\d+.bad$' % name, file_)
            if m is not None:
                bads.append(os.path.join(path, file_))
                continue
            m = re.match(r'^.%s.(\d+\.\d+)$' % name, file_)
            if m is None:
                continue
            baks.append(m.groups()[0])
        baks.sort(reverse=True)
        last_bak_file = None
        if len(baks) > 0:
            last_bak_file = '.%s.%s' % (name,baks[0])
            last_bak_file = os.path.join(path, last_bak_file)
        if last_bak_file is None:
            return False
        bads.sort(reverse=True)
        while len(bads) >= self.deletelastBad:
            os.remove(bads.pop())
        os.rename(self.filename, '%s.%s.bad' % (self.filename, geSmartNowTime()))
        shutil.copyfile(last_bak_file, self.filename)
        return True

cfg = ConfigFile('./test.cfg', ensure_ascii=False)
gParams = cfg.getValue(["post"])
gIndex = 0

class LuaTest(unittest.TestCase):
    def setUp(self):
        print '--------------setUp--------------\n'

    def testComm(self):
        global gIndex
        print '--------------testComm--------------\n'
        url,param = gParams[gIndex]
        gIndex += 1
        print gIndex
        print url
        print param

    def tearDown(self):
        print '--------------tearDown--------------\n'



loaded = False
if not loaded:
    loaded = True
    funname = "test_name"
    for i in xrange(0, len(gParams)-1):
        fn = funname + str(i)
        exec("LuaTest.%s = LuaTest.testComm" % fn)

def funcA(url, gParams):
    gParamstr = ""
    payload_1 = {'access_token': 'caf099ef-9c34-3af2-9ae1-e7264134e7e4'}
    for key,value in gParams.iteritems():
        gParamstr += "'%s'='%s'" % (key, value)

for url,info in gParams:
    funcA(url, info)

if __name__ == '__main__':
    cfg = ConfigFile('test.cfg', ensure_ascii=False)
    cfg.setValue(["1", "2"], "啊啊")
    