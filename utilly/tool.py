#!coding=utf-8
'''
Created on 2016Äê6ÔÂ28ÈÕ

@author: lx-lang.qinyue
'''

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
#! /usr/bin/python

import os
import sys
import time
import datetime
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from common import env
import json
from pprint import pprint

URL = ""
version = ""

def get_element_path(pagename, componentname):
    
    filename ="data/" + env.ElementsMapping.FileName
    filename = os.path.join(os.getcwd(), filename)
    
    #pprint(filename)
    
    with open(filename) as data_file:
        data = json.load(data_file)
    
    #pprint(data[pagename][componentname])
    
    return data[pagename][componentname]
    

def get_logname(testfile_name):
    path = os.getcwd()
    ctime = time.strftime("%m%d%H%M", time.localtime())
    path = path + '\\' + 'test_log' + '\\'
    filename = testfile_name + version + '_'+ str(ctime) + '.html'
    path = path + filename
    return path
    
def get_screenshots_path():
    
    ctime = time.strftime("%m%d%H%M", time.localtime())
    path = os.path.join(os.getcwd(),'test_log')

    if os.path.isdir(path) == False:
        os.makedirs(path)
    
    path = os.path.join(path,str(ctime))
    
    if os.path.isdir(path) == False:
        os.makedirs(path)
    
    return path

def get_current_time():
     currenttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
     return currenttime

def create_email_body(data):
    body = ''
    p = 0
    f = 0
    e = 0
    if len(data) > 0:
        for d in data:
            if d == "PASS":
                p = p + 1
            if d == "FAILED":
                f = f + 1
            if d == "ERROR":
                e = e + 1
        total = p + f + e
    body = "Total:" + str(total)+ "\n\r"
    body = body + "Pass:" + str(p) + "\n\r"
    body = body + "Failed:" + str(f) + "\n\r"
    body = body + "Error:" + str(e)

    return body
      

def get_recipients(hostname):
    sattr = ''
    try:
        sattr = getattr(env,hostname)
    except Exception,e:
        sattr = getattr(env, 'other')
    res = sattr.recipients
    return res

def send_mail(subj, body):
    
    smtpserver = env.Notification.Smtpserver
    sender = env.Notification.Sender
    recipients = env.Notification.Recipients
    session = smtplib.SMTP(smtpserver)
    msg = MIMEMultipart()
    msg['From'] = sender
    #msg['To'] = ", ".join(recipients)
    msg['To'] = recipients
    msg['Subject'] = subj
    msg.attach(MIMEText(body,'plain-text'))
   #part = MIMEBase('application', "octet-stream")
   #part.set_payload(att)
   #Encoders.encode_base64(part)
   #part.add_header('Content-Disposition', 'attachment; filename="test_report.html"')
   #msg.attach(part)
    smtpresult = session.sendmail(sender, recipients, msg.as_string())
    

if __name__ == '__main__':
    data = get_element_path("Home", "Butt_Start")