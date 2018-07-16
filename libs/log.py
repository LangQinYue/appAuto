#!/usr/bin/env python
#coding:utf-8
import logging  
import logging.handlers  
from utiity import conf
import os
class log():
    def __init__(self):
        
        BaseDir = os.path.dirname(os.path.dirname(__file__))
        logFile = os.path.join(BaseDir+'/log',conf.logfile)
        handler = logging.handlers.RotatingFileHandler(logFile, maxBytes = 1024*1024, backupCount = 5) # 实例化handler   
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
          
        formatter = logging.Formatter(fmt)   # 实例化formatter  
        handler.setFormatter(formatter)      # 为handler添加formatter  
          
        self.logger = logging.getLogger()     
        self.logger.addHandler(handler)           # 为logger添加handler  
        self.logger.setLevel(logging.DEBUG)
        #self.LOG_FILE = conf.logfile
    def errorInfo(self,message,flag=True):
        if flag:
            self.logger.info('not found element %s'% message)
        else:
            self.logger.debug(message)
    def msgInfo(self,message):

        self.logger.info(message)
    def testprint(self,a):
        print a
    def getlogger(self):
        return self.logger
    
        #logger.debug('firdddst debug message')  
#print datetime.               ('%Y-%m-%d %H-%M-%S')
'''
selenium提供了三种模式的断言：assert,verify,waitfor
    Assert：失败时，该测试将终止
    Verify：失败时，该测试继续执行，并将错误日志记录在日显示屏
    Waitfor：等待某些条件变为真，一般使用在AJAX应用程序的测试


断言常用的有，具体见如下：
assertLocation：判断当前是在正确的页面
assertTitle：检查当前页面的title是否正确
assertValue：检查input的值，check or radio，有为on，无为off
assertSelected：检查select的下拉菜单中选中是否正确
assertSelectedOptions：检查下拉菜单中的A选项是否正确
asserttext：检查指定元素的文本
assertTextParset：检查在当前给用户显示的页面上是否具有出现指定的文本
asserttextNotPresent：检查在当前给用户显示的页面上是否没有出现指定的文本
assertAttribute：检查当前指定元素的属性的值
assertTable：检查table里的某个cell中的值
assertEditable：检查指定的input是否可以编辑
assertNotEditable：检查指定的input是否不可以编辑
assertAlert：检查是否有产生带指定message的alert对话框
verifyTitle：验证预期的页面标题
verifyTextPresent：验证预期的文本是否在页面上的某个位置
verifyElementPresent：验证预期的UI元素，它的html标签的定义，是否在当前网页上
verifyText：核实预期的文本和相应的HTML标签是否都存在于页面上
verifyTable：验证表的预期内容
waitForPageToLoad：暂停执行，直到预期的新的页面加载
waitForElementPresent：等待检验某元素的存在，为真时，则执行
'''