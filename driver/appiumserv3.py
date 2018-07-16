#!coding=utf-8
'''
Created on 2016年12月1日

@author: lx-lang.qinyue
'''

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

from appium import webdriver

# 使用正则表达式筛选设备 id
import re

# 使用time.sleep(xx)函数进行等待
import time

# 使用 os 模块调用命令
import os

# 测试的包的路径和包名
appLocation = " /Users/Downloads/app.apk "

# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())

# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

# 读取 APK 的 package 信息
appPackageAdb = list(os.popen('aapt dump badging ' + appLocation ).readlines())
appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]

# 删除以前的安装包
os.system('adb uninstall ' + appPackage)


desired_caps = {
    'platformName': 'Android',
    'platformVersion': deviceVersion,
    'deviceName': deviceId,
    'appPackage': appPackage,
    'appWaitPackage': appPackage,
    'app': appLocation,
    'appActivity': appPackage + ".PageSplash",


command_executor = "http://localhost:4723/wd/hub"