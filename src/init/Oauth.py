# coding:utf-8
import requests
import initalize


# 字符集

# headers = {'Accept': 'application/json',
#            'Content-Type': 'application/x-www-form-urlencoded'}

headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
         'Accept-Encoding':'gzip, deflate, sdch',
         'Accept-Language':'zh-CN,zh;q=0.8',
         'Cache-Control':'no-cache',
         'Connection':'keep-alive',
         'Content-Type':'application/x-www-form-urlencoded',
         'Cookie':'JSESSIONID=4AB6487A994C0DE3CD98F09F945C67ED; sid='+initalize.shiro_sid+'; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN',
         'Host':initalize.address_host,
         'Pragma':'no-cache',
         'Referer':'http://'+initalize.address_host+'/middleclient/index.do',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2837.0 Safari/537.36',
         'X-Requested-With':'XMLHttpRequest'
             } 
def getAccesssToken(host):
    s = requests.Session()
    h_ip = 'http://' + host + '/middlecenter'
    url_oauth = '/oauth2/authorize'
    # 请求头
    payload = {'username': initalize.user_name,
               'password': initalize.user_password,
               'response_type': 'code',
               'platform': initalize.user_platform,
               'client_id': initalize.user_client_id,
               'redirect_uri': initalize.user_redirect_uri}

    # 请求
    r = s.post(h_ip + url_oauth, data=payload)
    # 转换为标准的json
    agent = eval(r.text,
                 type('Dummy', (dict, ),
                      dict(__getitem__=lambda s, n: n))())

    return agent['access_token']


if __name__ == '__main__':
    print getAccesssToken("10.1.0.57")
