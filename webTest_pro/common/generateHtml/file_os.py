# coding: utf-8
import os
import json
import socket
import sys

from html_template import Template_mixin

reload(sys)
sys.setdefaultencoding('utf8')

def checkAssic(instr):
    if not isinstance(instr, unicode):
        try: return instr.decode('gbk')
        except UnicodeDecodeError: pass
        try: return instr.decode('utf8')
        except UnicodeDecodeError: pass
    return instr

def getDirOrFileList(p, choose):
        p = str(p)
        if p == "":
              return [ ]
        p = p.replace("/", "\\")
        if p[ -1] != "\\":
             p = p + "\\"
        a = os.listdir(p)
        b = []
        if choose == 'folder':
            for x in a:
                if os.path.isdir(p + x):
                    b.append(checkAssic(x))
        elif choose == 'file':
            for x in a:
                if os.path.isfile(p + x):
                    b.append(checkAssic(x))
        return b
    

class HTMLFileRunner(Template_mixin):
    """
    """
#     print Template_mixin.HTML_TMPL_CEREPORT
    def __init__(self, title=None, description=None):
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
    '''
    filePath:文件路径
    folderPath:文件夹路径
    '''
    def generatr(self, folderPath):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname) + "report\\"
        mkdirFolder = folderPath + "\\" + ip
        '''创建文件夹 不存在创建'''
        if not  os.path.exists(mkdirFolder):
            os.mkdir(mkdirFolder)
        file_objects = open(folderPath + "\index.html", 'w')
        outputs = self.HTML_TMPL_INDEX % dict(
            title=self.title,
            description=self.description,
            folder=json.dumps(getDirOrFileList(folderPath, "folder"), ensure_ascii=False),
            folderPath=folderPath,
            getcwd=os.getcwd(),
        )
        file_objects.write(outputs)
        file_objects.close()
        '打开文件'
        file_object = open(mkdirFolder + "\cereport.html", 'w')
        output = self.HTML_TMPL_CEREPORT % dict(
            title=self.title,
            description=self.description,
            file=json.dumps(getDirOrFileList(mkdirFolder, "file"), ensure_ascii=False),
            folderPath=folderPath,
            getcwd=os.getcwd(),
        )
        file_object.write(output)
        file_object.close()

if __name__ == '__main__':
    hostname = socket.gethostname()
    print socket.gethostbyname(hostname)
#     folderPath = "Z:\\reports\\"
#     HTMLFileRunner(title='测试报告 ', description='用例执行情况：').generatr(folderPath)
#     folderPath = "Z:\\reports"
#     HTMLFileRunner(title='测试报告 ', description='用例执行情况：').generatr(folderPath)
