#!coding:utf-8
import httplib
import urllib2,os
import requests
r =  requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx?wsdl')
print r.elapsed.microseconds
str = '中国电视节目预告'

if str.decode('utf-8') in r.text:
    print 'pass'
elif str.decode('utf-8') not in r.text:
    print 'fail'
path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
if os.path.isdir(path):
    print path+'1'
elif os.path.isfile(path):
    print os.path.dirname(path)+'2'
print os.pardir
print os.getcwd()
path = os.path.join(path,'libs')
print path

