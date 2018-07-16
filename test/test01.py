#!coding=utf-8
'''
Created on 2016��6��27��

@author: lx-lang.qinyue
'''
import sys 
from _abcoll import Container
reload(sys)
sys.setdefaultencoding("utf-8")
import unittest
from time import sleep
from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#import desired_capabilities
class FindByAccessibilityIdTests(unittest.TestCase):
    """docstring for FindByAccessibilityIdTests"""
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '192.168.248.101:5555'
        #desired_caps['app'] = PATH(r'../../apk/aa.apk')
        #desired_caps['appActivity'] = 'com.fuiou.mgr.activity.LogoutActivity'
        desired_caps['appActivity'] = 'com.zhihu.android.app.ui.activity.MainActivity'
        #desired_caps['appActivity'] = 'com.baidu.fb.activity.WelcomeActivity'
        #desired_caps['appPackage'] = 'com.fuiou.mgr' 
        #desired_caps['appPackage'] = 'com.baidu.fb'
        desired_caps['appPackage'] = 'com.zhihu.android'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
    def atest01(self):
        #self.driver.remove_app('com.zhihu.android')
        pass
    def up(self):
        size = self.driver.get_window_size()
        self.driver.flick(size.get('width')/2, size.get('height')*0.9, size.get('width')/2, size.get('height')*0.1)
    def test_find_single_element(self):
        #self.driver.implicitly_wait(5)
        import time
        time.sleep(7)
#         el = self.driver.find_elements_by_xpath('//android.widget.TextView')
#         #self.driver.set_value(el[0], 'lang')
#         action = TouchAction(self.driver)
#         print el[1].get_attribute('text')
#         #action.tap(el[1],1).release().perform()
#         self.driver.scroll(el[0], el[1])
#         time.sleep(3)
        self.driver.wait_activity('com.baidu.fb.activity.WelcomeActivity',6)
        
        time.sleep(5)
                       
            
            

if __name__ == '__main__':
    #unittest.main()
    city = {'中国':['北京','武汉'],'美国':['纽约','baxi'],'法国':['巴黎','dd']}
    for country in city:
        for a in  city[country]:
            print a
