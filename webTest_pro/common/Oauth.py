# coding:utf-8

# 依赖包
import requests
# 字符集
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

headers = {'Accept': 'application/json',
           'Content-Type': 'application/x-www-form-urlencoded'}


def getAccesssToken(host):

    h_ip = 'http://' + host + '/middlecenter'
    url_oauth = '/oauth2/authorize'
    # 请求头

    payload = {'username': 'administrator',
               'password': 'xungejiaoyu',
               'response_type': 'code',
               'platform': '29a5349d-aee2-4c30-894e-47124f4c6083',
               'client_id': '6b4cfaea-7016-11e5-bd19-68f728833c05'}

    # 请求
    r = requests.post(h_ip + url_oauth, data=payload)

    # 转换为标准的json
    agent = eval(r.text,
                 type('Dummy', (dict, ),
                      dict(__getitem__=lambda s, n: n))())

    return agent

if __name__ == '__main__':
    print getAccesssToken('10.1.0.56')
