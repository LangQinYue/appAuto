#coding:utf-8

import urllib
import re
import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
import requests,urllib2,json
from io import StringIO
count = 1000000          #书籍ID
if count <1000000:     #如果书籍的ID小于200W
    while True:                 # 条件为真
        count += 1             #循环开始，并且count += 1 
        try:                          #try 捕获异常
            url = 'https://api.douban.com/v/book/%s' %count             #自动通过count数量的变化请求接口数据 
            r = requests.head(url)
            #print r.headers
            #content = r.head
            print r
            url2 = urllib2.Request(url)                                                          # 使用urllib2的request方法
            response = urllib2.urlopen(url2)                                               #用urlopen打开上一步返回的结果，得到请求后的响应内容
            apicon = response.read()                                                          #读取response
            #print apicon
        except urllib2.HTTPError:                                                              #如果频繁请求，会被判定为恶意请求， 并被封IP 这个只是一个实例，没有加时间间隔，想深入做的同学可以加一下
            print "error , urllib2.HTTPError : %s " %count  
cookies = dict(cookies_are='working')
search = {'word':'云层','pbook':0}
reque = requests.Session()
r = requests.get('http://yuedu.baidu.com/search',params = search,cookies=cookies,allow_redirects=True)
r.encoding = 'gbk'
s =  r.content.decode('gbk').encode('utf-8')

#print r.status_code,r.cookies
#print s
'''
from requests import Request, Session
url = 'http://www.baidu.com'
data = {'word':'云层','pbook':0}
headers = {'Accept-Encoding': 'gzip, deflate'}
s = Session()
req = Request('GET',  url, data=data, headers=headers)

prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    stream=stream,#内容流
    verify=True, #启用SSL证书
    proxies=proxies,#代理设置
    cert=cert,#指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
    timeout=5000#超时时间
)

print(resp.status_code)
'''
#headers = 'cache-control': 'max-age=80'
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
data = {'email':'langqy@163.com','pwd':'b96e2e010f4135ff56bc975e0296edb47cb510c6'}
s = requests.Session()
r = s.post('http://www.oschina.net/action/user/hash_login',data = json.dumps(data),headers = headers)
auth =('langqy@163.com','lang7356923')
yanzheng = s.get('http://my.oschina.net/langqy/?ft=bbs&scope=2&showme=1',headers=headers)

#print yanzheng.text
#print r.content.encode('utf-8')
'''
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
BUFSIZE = 1024
server.bind(('127.0.0.1',8000)) #绑定ip和端口
server.listen(5) #最多接受5个连接
while True:
    client,addr = server.accept()
    print ('connection',addr)
    while 1:
        #返回的是一个b'str'
        data = client.recv(BUFSIZE)
        print 'client',data
        if not data:
            print ('connection shutdown form',addr)
            break
        buf = input('please input something to client: ')
        client.send(buf)
    client.close()
server.close()
'''
import os
path = os.path.join(os.getcwd(),'test02.py')
os.stat(path).st_size
def outer(func):
    def log(*arg,**args):
        print 'begin'
        func(*arg,**args)
    return log
def inner(func):
    def logg(*arg,**args):
        print 'end'
        func(*arg,**args)
    return logg
@outer
@inner
def f1(*arg):
    sum=0
    for i in arg:
        sum+=i
    print sum
    print 'f1函数'
h={'a':1}
def outter(func):
    def inner(*args, **kwargs):
        print(inner.__doc__)  # None
        return func()
    return inner

@outter
def function():
    """
    asdfasd
    :return:
    """
    print('func')
function()