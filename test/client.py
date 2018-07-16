#coding:utf-8
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
'''
from socket import *
client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8000))
while  1:
	buf = input ('please input something to server:')
	if buf == 'quit':
		break
	client.send(buf.encode('utf-8'))
	data = client.recv(1024)
	print ('server:',data.decode('utf-8'))
	if not data:
		print 'server shutdown conection'
client.close()
'''

from socket import *
client = socket()
while 1:
	buf = raw_input("Please input your name:\n")
	client.sendto(buf.encode('utf-8'), ('123.206.41.84',80))
	data,server = client.recvfrom(1024)
	print data.decode('utf-8'),server
client.close()

'''
	osi：  应用层 表示层 会话 传输层 网络层 数据链路层 物理层


	sftp 加密文件传输协议
	ftp  不加密文件传输协议
	telnet 明文远端登录服务器协议
	ssh   加密的远端登录服务器协议
	smtp 25端口
	http 80端口
	应用层 telnet http ftp ssh
	协议：规范了一种格式
	
	
	套接字：
	电脑直接通信
	公司：服务器
	电话：套接字
	通讯员：listen()
	TCP：
	面向链接套接字：TCP/IP（SOCK_STREAM）:流->流->流
	
	UDP：UDP
	
	
	进程在计算机中 内存分配资源的最小单位
	线程 最小的执行单位 共享内存
	创建进程 fork()
	
	UDP：SOCK_DGRAM 报文 无链接
	Tcp:SOCK_STREAM 流 有链接

'''