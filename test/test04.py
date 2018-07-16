#!coding=utf-8
'''
Created on 2016年8月7日

@author: lx-lang.qinyue
'''

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
import sys,os
import time


def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    #sys.stdout.flush()


if __name__ == '__main__':
        import re
        import pickle
        import paramiko
        
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect('192.168.21.40', 22, 'PClear', '123456')
#         stdin, stdout, stderr = ssh.exec_command('df')
#         #print stdout.read()
#         print stdin
#         ssh.close();
        import TriAquae

