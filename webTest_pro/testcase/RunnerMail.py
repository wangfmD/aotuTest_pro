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
from email.header import Header

import smtplib
import os

reload(sys)

sys.setdefaultencoding('utf8')

homePath = os.environ.get("PY_DEV_HOME")
reportPath = homePath + '\webTest_pro\\report\\'
# print  reportPath
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_ssta.py')


def sendReport(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'devops@3bu.cn'  # 发件地址
    msg['To'] = 'wangfm@3bu.cn'  # 收件人地址，多人以分号分隔

    smtp = smtplib.SMTP('smtp.exmail.qq.com')
    smtp.login('devops@3bu.cn', 'Xungejiaoyu@2015')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out!')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    filename = reportPath + now + '_restult.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    sendReport(filename)
