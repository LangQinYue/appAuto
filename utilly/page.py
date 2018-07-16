#!coding=utf-8
'''
Created on 2016��6��28��

@author: lx-lang.qinyue
'''

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

from common import env
from common import lfliberties as testlib
import appium
import time

platform = env.DeviceInfo.PlatformName


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, uia_string):
        
        try:
            if platform == "Android":
                uia_string = uia_string.replace ("'","\"")
                #print uia_string
                element = self.driver.find_element_by_android_uiautomator(uia_string)
            else:
                element = self.driver.find_element_by_ios_uiautomation(uia_string)
        except Exception,ex:
            #print ex
            return "NOT FOUND"
            
        return element
    
    def input_element_text(self,pagename,elemname,value):
        
        uia_string = testlib.get_element_path(pagename, elemname)
        try:
            element = self.find_element(uia_string)
            element.send_keys(value)
        except Exception,ex:
            print "Element is not found"

    def find_container(self, uia_string):
        
        try:
                
            container = self.driver.find_elements_by_class_name(uia_string)
        except Exception,ex:
            pass
            #print ex
    
        return container
        
    def android_list_count(self,pagename,elemname):
        
        index = 0
        flag = True
        textlist = ""
        while flag is True:
            uia_string = testlib.get_element_path(pagename, elemname)
            uia_string = uia_string.replace("$INDEX",str(index))
            try:
                element = self.find_element(uia_string)
                time.sleep(1)
                if isinstance(element,appium.webdriver.webelement.WebElement):
                    index+=1
                    textlist = textlist + element.get_attribute("name")
                else:
                    flag=False
            except Exception,ex:
                #print ex
                flag = False
                
        return index, textlist
    
    def click_page_element(self,pagename,elemname):
        
        uia_string = testlib.get_element_path(pagename, elemname)
        element = self.find_element(uia_string)
        element.click()
    
    def get_element_attributes(self,pagename,elemname):
        
        #element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Go Photo Prints")')
        name = ""
        uia_string = testlib.get_element_path(pagename,elemname)
        element = self.find_element(uia_string)
        time.sleep(1)
        name = element.get_attribute("name")
        return name
    
    def get_list_length(self,pagename,elemname):
        
        textlist = ""
        
        if platform == "IOS":
            uia_string = testlib.get_element_path(pagename, elemname)
            rows = len(self.find_container(uia_string))
        else:
            rows,textlist = self.android_list_count(pagename,elemname)
        return rows
    
    def clear_element_text(self,pagename,elemname):
        
        #element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Go Photo Prints")')
        name = ""
        uia_string = testlib.get_element_path(pagename,elemname)
        try:
            element = self.find_element(uia_string)
            length = len(element.get_attribute("name"))
            i = 0
            while i < length:
                self.driver.press_keycode(22) #KEYCODE_DPAD_RIGHT
                i+=1
            while i >= 0:
                self.driver.press_keycode(67) #KEYCODE_DEL
                i-=1
        except Exception,ex:
            pass
    def get_element_leftlocation(self,pagename,elemname):
        
        try:
            uia_string = testlib.get_element_path(pagename, elemname)
            element = self.find_element(uia_string)
            x = element.location['x']
            y = element.location['y']
            print x,y
            return x+10, y
        except Exception,ex:
            return "Not Found",""

class CategoryPage(BasePage):
    
    def get_category_number(self):
        
        uia_string = testlib.get_element_path("Category", "Cell_Category")
        rows = super(CategoryPage,self).find_container(uia_string)
        return len(rows) - 1

class SourcePage(BasePage):
    
    
    def get_source_list(self):
        
        namelist = ""
        uia_string = testlib.get_element_path("Source", "List_Sizes")
        if platform == "IOS":
            rows = super(SourcePage,self).find_container(self.driver, uia_string)
        
            for row in rows:
                namelist = namelist + row.get_attribute("text")
        else:
            
            index,namelist = super(SourcePage,self).android_list_count("Source","List_Sizes")
            
        return namelist

class PhotosPage(BasePage):
    
    def select_photos(self, start_index,count):
        
        if platform == "IOS":
            res = self.ios_select_photos(start_index,count)
        else:
            res = self.android_select_photos(start_index,count)
        
        return res
    
    def android_select_photos(self,start_index,count):
        
        i = 0
        total_photos = super(PhotosPage,self).get_list_length("Photos","Cell_Photos")
        #print total_photos
        
        if (start_index > total_photos) or count > (total_photos-start_index+1):
            return False
        else:
            while (i < count):
                
                uia_string = testlib.get_element_path("Photos", "Cell_Photos")
                uia_string = uia_string.replace("$INDEX",str(start_index))
                uia_string = uia_string.replace ("'","\"")
        
                try:
                    element = super(PhotosPage,self).find_element(uia_string)
                    element.click()
                    i+=1
                    start_index+=1  
                except Exception,ex:
                    #print ex
                    return False     
                    
            return True
            
    def ios_select_photos(self,counter):
        
        pass
        
class SetQuantityPage(BasePage):
        
    def set_finish_type(self,typename):
        
        if typename == "Glossy":
            tname = "RButt_Finishtype_Glossy"
        elif typename == "Matte":
            tname = "RButt_Finishtype_Matte"
        else:
            tname = "RButt_Finishtype_Matte"
        try:
            uia_string = testlib.get_element_path("SetQuantity", tname)
            element = super(SetQuantityPage,self).find_element(uia_string)
            element.click()
        except Exception, ex:
            #print ex
            pass
    
    def set_size_quantity(self, index, action, count):
        
        if action == "More":
            uia_string = testlib.get_element_path("SetQuantity", "Butt_More")
        else:
            uia_string = testlib.get_element_path("SetQuantity", "Butt_Less")
        
        uia_string = uia_string.replace("$INDEX",str(index))
        
        #print uia_string
        try:
            element = super(SetQuantityPage,self).find_element(uia_string)
        
            i = 0
        
            while i < count:
            
                element.click()
                i+=1
        except Exception,ex:
            #print ex
            pass
            
class EditPage(BasePage):
    
    def crop_photo(self):
        
        try:
        
            uia_string = testlib.get_element_path("ReviewEdit", "ImageView_CropImage")
            """"
            element = super(EditPage,self).find_element(uia_string)
            element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageView")')
            x = element.location['x']
            y = element.location['y']
            x1,y1,x2,y2 = element.get_attribute("location")
            print x1,y1,x2,ya
            x= (x2-x1)/2
            y= (y2-y1)/2
            self.driver.swipe(x,y,x-100,y-100)
            """
            self.driver.swipe(850,600,700,750)
            uia_string = testlib.get_element_path("ReviewEdit", "Butt_Edit_Done")
            element = super(EditPage,self).find_element(uia_string)
            element.click()
        except Exception,ex:
            print ex
            pass

class CreditPage(BasePage):
    
    def set_datepicker_value(self,typename,value):
        
        if typename == "Month":
            elem_name = "Text_ExpMonth"
        else:
            elem_name = "Text_ExpYear"
        
        try:
        
            uia_string = testlib.get_element_path("CreditInfo", elem_name)
            element = super(CreditPage,self).find_element(uia_string)
            x = element.location['x']
            y = element.location['y']
            #print x,y
            width = element.size['width']
            height = element.size['height']
            #print height, width
            name = element.get_attribute("name")
            # set month
            y1 = y - height
            #print y1
            i = 0
            while name != value and i < 12:
               
                self.driver.swipe(x,y,x,y1)
                name = element.get_attribute("name")
                #print name
                i+=1
                
        except Exception,ex:
            print ex
            pass
    
    def set_expiration_date(self,month_value,year_value):
        
        self.set_datepicker_value("Month",month_value)
        self.set_datepicker_value("Year",year_value)
        
        
        
        