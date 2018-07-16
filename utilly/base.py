#coding=utf-8
'''
Created on 2016年7月5日

@author: lx-lang.qinyue
'''
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import sys
sys.path.append("..")
from selenium.common.exceptions import NoSuchElementException
import driver.appdriver as appdriver
from appium.webdriver.webdriver import WebDriverWait
from time import sleep
from xml.etree import ElementTree as elementTree
import config.config as readConfig
from appium.common.exceptions import NoSuchContextException as EC
from selenium.webdriver.common.keys import Keys
Keys.BACK_SPACE
WebDriver.open_notifications()#展开通知栏
global  outtimes
configLocal = readConfig.ReadConfig()
class Operation(object):
    def is_exist(self, driver, type, value):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """

        if self.get_context(driver) != "NATIVE_APP":
            driver.switch_to.context(driver.contexts[-1])

        try:
            #
            if type == "id":
                return driver.find_element_by_id(value)
            
            if type == "classname":
                return driver.find_element_by_class_name(value)
            if type == "xpath":
                return driver.find_element_by_xpath(value)
                 
            if type == "name":
                return driver.find_element_by_name(value)
                 
            return False
        except NoSuchElementException as e:
            return e
    def does_exist(self, driver, type, value):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.is_exist(driver, type, value):
            sleep(1)
            i += 1

            if i >= int(configLocal.get_config_value("findElementTimes")):
                return False
        else:
            return True
    #获取元素   
    def find_element(self,by,value): 
        by = self.getby(by)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(by,value))
            conf.flag = True
        except Exception,e:
            pass
        if conf.flag:
            return self.driver.find_element(by,value)
        self.driver.find_element_by_android_uiautomator(new uiselect)
    
    #获取一组元素
    def find_elements(self,by,value):
        #return self.driver.find_element(*loc)
        by = self.getby(by)
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_elements(by,value))
            conf.flag = True
        except Exception:
            pass
        if conf.flag:
            return self.driver.find_elements(by,value)
    def get_element(self, driver, type, value, index='0'):
        """
        get one element
        :return:
        """
        if self.does_exist(driver, type, value):
            if type == "id":
                element = driver.find_element_by_id(value)
                return element
            if type == "classname":
                element = driver.find_element_by_class_name(value)
                return element
            if type == "xpath":
                element = driver.find_element_by_xpath(value)
                return element
            if type == "name":
                element = driver.find_element_by_name(value)
                return element
            if type == "link_text":
                element_list = driver.find_element_partial_by_link_text(value)
                return element
            if type == "tag_name":
                element_list = driver.find_element_by_tag_name(value)
                return element
            if type == "css_selector":
                element_list = driver.find_element_by_css_selector(value)
                return element
            return None
        else:
            return None

    def get_element_list(self, driver, type, value):
        """
        get elementList
        :return:elements
        """
        if self.does_exist(driver, type, value):
            if type == "id":
                element_list = driver.find_elements_by_id(value)
                return element_list
            if type == "classname":
                element_list = driver.find_elements_by_class_name(value)
                return element_list
            if type == "xpath":
                element_list = driver.find_elements_by_xpath(value)
                return element_list
            if type == "name":
                element_list = driver.find_elements_by_name(value)
                return element_list
            if type == "link_text":
                element_list = driver.find_elements_by_partial_link_text(value)
                return element_list
            if type == "tag_name":
                element_list = driver.find_elements_by_tag_name(value)
                return element_list
            if type == "css_selector":
                element_list = driver.find_elements_by_css_selector(value)
                return element_list
            return None
        else:
            return None

    def get_element_byios_uiautomation(self, driver, elements):
        """
        get_element_byios_uiautomation
        """
        return driver.find_element_by_ios_uiautomation(element)

    def get_element_by_accessibility_id(self, driver, id):
        """
        get_element_by_accessibility_id
        """
        return driver.find_elements_by_accessibility_id(id)

    def get_element_value(self, driver, type, value, index='0'):
        """
        # ����Ԫ�ص��ı�ֵ
        """
        element = self.get_element(driver, type, value, index)
        return element.text()

    def get_element_size(self, driver, type, value, index='0'):
        """
        # ����Ԫ�ص��ı�ֵ
        """
        element = self.get_element(driver, type, value, index)
        return element.size()

    def get_element_location(self, driver, type, value, index='0'):
        """
        # ����Ԫ�ص��ı�ֵ
        """
        element = self.get_element(driver, type, value, index)
        return element.location()

    def is_selected(self, driver, type, value, index='0'):
        """
        is_selected
        """
        element = self.get_element(driver, type, value, index)
        return  element.is_slected()

    def click(self, driver, type, value, index='0'):
        """
        click element
        :return:
        """
        try:
            element = self.get_element(driver, type, value, index)
            if element:

                element.click()
            else:
                print value,
                print 'is not exits'
        except AttributeError as e:
            raise e
 
    def send_key(self, driver, type, value, index='0', values='fengshuai'):
        """
        input the key
        :param values
        :return:
        """
        try:
            element = self.get_element(driver, type, value, index)
            element.clear()
            element.send_keys(values)
        except AttributeError as e:
            raise e

    def get_contexts(self, driver):
        """
        :param values
        :return: ���ص�ǰ�Ự�е������ģ�ʹ�ú����ʶ��h5��ҳ��ؼ�
        """
        values = driver.contexts
        return values


    def get_context(self, driver):
        """
        :param values
        :return: ���ص�ǰ�Ự�е�������
        """
        value = driver.context
        return value

    def get_tag_name(self, driver, type, value, index='0'):
        """
        get_tag_name
        """
        element = self.get_element(driver, type, value, index)
            
        return element.tag_name()

    def get_window_size(self, driver):
        """
        get current windows size mnn
        :return:windowSize
        """
        global windowSize
        windowSize = driver.get_window_size()
        return windowSize

    def scroll(self, driver, origin_element, destination_element):
        """# ��Ԫ��origin_el������Ԫ��destination_el
        """
        driver.scroll(origin_element, destination_element)

    def drag_and_drop(self, driver, origin_element, destination_element):
        """# ��Ԫ��origin_el�ϵ�Ŀ��Ԫ��destination_el
        """
        driver.drag_and_drop(origin_element, destination_element)

    def tap(self, driver, positions, duration=1000):
        """"#ģ����ָ�������������ָ���������ð�סʱ�䳤�ȣ����룩
        #driver.tap([(x,y),[x1,y1]]),500)
        """
        driver.tap(positions, duration)

    def swipe(self, driver, start_x, start_y, end_x, end_y, duration=None):
        """#��A�㻬����B�㣬����ʱ��Ϊ����
        """
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    def flick(self, driver, start_x, start_y, end_x, end_y, duration=None):
        """#��סA�����ٻ�����B��
        """
        driver.flick(start_x, start_y, end_x, end_y, duration)
        
    def swipe_to_up(self, driver, during=None):
        """
        swipe UP
        :param during:
        :return:
        """
        # if windowSize == None:
        window_size = get_window_size()

        width = window_size.get("width")
        height = window_size.get("height")
        driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, during)

    def swipe_to_down(self, driver, during=None):
        """
        swipe down
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, during)

    def swipe_to_left(self, driver, during=None):
        """
        swipe left
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, during)

    def swipe_to_right(self, driver, during=None):
        """
        swipe right
        :param during:
        :return:
        """
        window_size = get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, during)

    def reset(self):
        """
        #����Ӧ��(����ɾ��Ӧ������)
        """
        driver.reset()

    def hide_keyboard(self, driver, key_name=None, key=None, strategy=None):
        """
        #���ؼ���,iOSʹ��key_name���أ���׿��ʹ�ò���
        #Hides the software keyboard on the device. In iOS, use `key_name` to press a particular key, or `strategy`. 
        #In Android, no parameters are used.
        """
        driver.hide_keyboard(key_name)

    def long_press_keycode(self, driver, keycode, metastate=None):
        """
        #����һ�������İ����루����ĳ����
        """
        driver.long_press_keycode(keycode)

    def background_app(self, driver, seconds):
        """
        # ��̨����app������
        """
        driver.background_app(seconds)

    def is_app_installed(self, driver, bundle_id):
        """
        app is_app_installed
        """
        driver.is_app_installed(bundle_id)

    def remove_app(self, driver, bundle_id):
        """
        remove_app
        """
        driver.remove_app(bundle_id)

    def lock(self, driver, seconds):
        """#����һ��ʱ��  iOSר��"""
        driver.lock(seconds)
# 截屏
	def getScreenShot(filename):
		mytime=getMyTime()
		myscreenshot="C:/Users/Administrator/Documents/"+mytime+filename+".png"
		driver.get_screenshot_as_file(myscreenshot)
		
	def getAlertText():
		alerttest = driver.switch_to_alert().text()
		return alerttest
    def set_location(self, driver, latitude, longitude, altitude):
        """
        :Args:
         - latitudeγ�� - String or numeric value between -90.0 and 90.00
         - longitude���� - String or numeric value between -180.0 and 180.0
         - altitude���θ߶�- String or numeric value
        """
        driver.set_location(driver, latitude, longitude, altitude)
    def get_attribute(self,attribute):
        pass
    '''
    def get_attribute(self, attribute):
        """
        get the element attribute
        :param attribute:
        :return:value
        """
        try:
            element = self.find_element()
            value = element.get_attribute(attribute)
            return value
        except AttributeError:
            raise
    def waitUntilElementByID(self,eleid):
        self.wait.until(EC.presence_of_element_located((By.ID,eleid)))
    
    def clickBack(self):
        os.system("adb shell input keyevent 4") 
        
    def clickEnter(self):
        os.system("adb shell input keyevent 66") 
        
    def clickHome(self):
        os.system("adb shell input keyevent 3") 
        
    def clickMenu(self):
        os.system("adb shell input keyevent 1") 
    
    #元素文本清除
    def elementClear(self,el):
        el.click()
        driver.keyevent(123)#光标移动到最后
        length = len(el.text())
        while length > 0:
            length-=1
            driver.keyevent(67)#删除键
            
    #切换acctive
    def wait_activity(self, activity, timeout, interval=1):
        """Wait for an activity: block until target activity presents
        or time out.

        This is an Android-only method.

        :Agrs:
          - activity - target activity
         - timeout - max wait time, in seconds
         """
        try:
             WebDriverWait(self, timeout, interval).until(lambda d: d.current_activity == activity)
             return True
         except TimeoutException:
             return False
    '''