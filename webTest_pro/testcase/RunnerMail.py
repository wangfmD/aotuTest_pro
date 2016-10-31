# _*_ coding: utf-8 _*_
"""
__title__ = ""
__auther__ = "acer"
__mtime__ = "2016/10/26"
"""
import os
import smtplib
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import time

reload(sys)

sys.setdefaultencoding('utf8')

homePath = os.environ.get("PY_DEV_HOME")

# 设置测试报告路径
if os.name == 'nt':
    reportPath = homePath + '\webTest_pro\\report\\'
else:
    reportPath = homePath + '/webTest_pro/report/'

# 测试报告路径不存在，则创建该路径
if os.path.exists(reportPath) == True:
    print "The report path exist!"
else:
    print "The report path is not exist,create report directory..."
    os.mkdir(reportPath)

# print  reportPath
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')


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


def sendReportWithAtt(attachment):
    f = open(attachment, 'rb')
    sendfile = f.read()
    f.close()

    if os.name == 'nt':
        attName = str(attachment).split('\\')[-1]
    else:
        attName = str(attachment).split('/')[-1]

    smtpserver = 'smtp.exmail.qq.com'
    sender = 'devops@3bu.cn'  # 发件地址
    receiver = 'wangfm@3bu.cn'  # 收件人地址，多人以分号分隔
    user = 'devops@3bu.cn'
    password = 'Xungejiaoyu@2015'
    Subject = '自动化测试报告'

    msgRoot = MIMEMultipart('related')
    att = MIMEText(sendfile, 'html', 'utf-8')
    # att['Content-Type'] = 'application/octet-stream'
    # att['Content-Disposition'] = 'attachment; filename = "report.html"'
    msgRoot['Subject'] = Subject
    msgRoot['From'] = sender
    msgRoot.attach(att)

    mime = MIMEBase('application', 'html', filename=attName)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=attName)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(sendfile)
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msgRoot.attach(mime)

    smtp = smtplib.SMTP(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(msgRoot['From'], receiver, msgRoot.as_string())

    smtp.quit()
    print('test report has send out!')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    filename = reportPath + now + '_restult.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    sendReportWithAtt(filename)
