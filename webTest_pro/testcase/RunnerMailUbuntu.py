# _*_ coding: utf-8 _*_
"""
__title__ = ""
__auther__ = "acer"
__mtime__ = "2016/10/26"
"""
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import smtplib
import os

reload(sys)

sys.setdefaultencoding('utf8')

homePath = os.environ.get("PY_DEV_HOME")
reportPath = homePath + '/webTest_pro/report/'
# print  reportPath
#  test_dir = './'
test_dir = './test/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')


def sendFileMail(file_new):
    f = open(file_new, 'rb')
    sendfile = f.read()
    f.close()

    smtpserver = 'smtp.exmail.qq.com'
    sender = 'devops@3bu.cn'  # 发件地址
    receiver = 'wangfm@3bu.cn;wuf@3bu.cn'  # 收件人地址，多人以分号分隔
    user = 'devops@3bu.cn'
    password = 'Xungejiaoyu@2015'
    Subject = '自动化测试报告'

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "report.html"'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Subject
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    filename = reportPath + now + '_restult.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)

    sendFileMail(filename)
    fp.close()
    print "send mail success!"
