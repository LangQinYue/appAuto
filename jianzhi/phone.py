#!coding=utf-8
import time,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import sys,xlrd,re,random
from xlutils import copy as excelwrite
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
file  = 'phone.xlsx'
count = 0
#driver.set_page_load_timeout(60)
def existElement(value):
    
        #self.loadJquery()
    js = '''
        if($('%s').not(':hidden').length > 0){return 1;}else{return 0;}
    ''' % value
    try:
        a=driver.execute_script(js)
        return a
    except Exception:
        return 0
def existElementt(value,typee='class'):
    a= []
    if typee == 'class':
        jsa  = '''
            return document.getElementsByClassName('%s')
            ''' % value
    elif typee == 'tag':
        jsa  = '''
            return document.getElementsByTagName('%s')
            ''' % value
    else:
        jsa  = '''
            return document.getElementById('%s')
            ''' % value
    try:
        a=driver.execute_script(jsa)
    except Exception:
        pass
    if a:
        if typee == 'class':
            for i in a:
                if i.is_displayed():
                    return 1
        else:
            if a.is_displayed():
                return 1

    return 0   
def waitElement(value,timeout=15):
    global count
    if existElementt(value):
        return 1

    else:
        time.sleep(1)
        count +=1
        if count>timeout:
            count = 0
            return
        waitElement(value, timeout)
def findelement(value): 
    #waitElement(value)
    try:
        WebDriverWait(driver,20).until(ec.presence_of_element_located((By.CSS_SELECTOR,value)))
        if driver.find_element(By.CSS_SELECTOR,value).is_displayed():
            return driver.find_element(By.CSS_SELECTOR,value)
    except Exception,e:
        pass
def elementsDisplayer(value,element = None):
    if element:
        elements = element.find_elements_by_css_selector(value)
        return [element for element in elements if element.is_displayed()]
    else:
        elements =driver.find_elements_by_css_selector(value)
        return [element for element in elements if element.is_displayed()]
def elementSelect(ele,value):
    element = ele
    #value = int(value)
    select  = Select(element)
    num = len(Select(element).options)-1
    #select.select_by_index(value)
    select.select_by_value('%s' % str(value))
    time.sleep(1)
def switchToWindow():
    curr_window = driver.current_window_handle
    #print curr_window+'3333'
    handles = driver.window_handles
    #print handles
    for handle in handles:
        if handle != curr_window:
            driver.switch_to_window(handle)
def closeOtherWindow():
        curr_window = driver.current_window_handle
        handles = driver.window_handles
        for handle in handles:
            if handle != curr_window:
                driver.switch_to_window(handle)
                driver.close()
                driver.switch_to_window(curr_window)
def excelWrite(count,j,inserStr):
        data=xlrd.open_workbook(file)
        Wdata=excelwrite.copy(data)
        ws=Wdata.get_sheet(0)
        ws.write(count,j,inserStr)
        Wdata.save(file)
try:
    table = xlrd.open_workbook(file)
except Exception,e:
    print str(e)
count = 0       
sheet = table.sheet_by_index(0)  # by index
nrows = sheet.nrows
count = nrows
option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"images":2}}
option.add_experimental_option('prefs', prefs)
flag = raw_input(u"请输入执行方式，0：新开始，   1：接下去运行\n")
driver = webdriver.Chrome(executable_path=r"D:\Program Files\Chrome\chromedriver.exe",chrome_options=option)
profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
#driver = webdriver.Firefox()
profile.update_preferences() 
#driver = webdriver.Firefox()

driver.maximize_window()
driver.get('https://www.1688.com/')
waitElement('account-signin')
findelement('.account-signin>a').click()
time.sleep(2)
driver.switch_to_frame(findelement('#loginchina iframe'))
time.sleep(2)
try:
    findelement('#J_Quick2Static').click()
except Exception:
    pass
findelement('#TPL_username_1').send_keys(u'梦琪箱包厂:子账号1')
findelement('#TPL_password_1').send_keys('lijin1977')
findelement('#J_SubmitStatic').click()
f = open('url.txt','r')
stt = f.read()
f.close()
time.sleep(5)
if stt and int(flag):
    driver.get(stt)
else:
    #findelement('body').click()
    time.sleep(1)
    element = findelement('.first.fd-left.current>a')
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(0.3)
    if existElementt('close'):
        findelement('.close').click()
        time.sleep(1)
    findelement('.current-next a[title="供应商"]').click()
    findelement('#alisearch-keywords').send_keys(u'容城')
    findelement('#alisearch-submit').click()
    findelement('#filter_cxtSort').click()
#time.sleep(2)
for i in xrange(20):
    curr = driver.current_url
    #print curr
    f = open('url.txt','w')
    f.write(curr)
    f.close()
    waitElement('page-next')
    #findelement('.page-next').click()
    waitElement('list-item-title-text')
    li = elementsDisplayer('.list-item-title-text')
    for i,j in enumerate(li):
        try:
            if i>0:
                driver.execute_script("arguments[0].scrollIntoView();", li[i-1])
            li[i].click()
            switchToWindow()
            waitElement('show-category')
            time.sleep(1.5)
            findelement('li[data-page-name="contactinfo"] a').click()
            waitElement('contact-info')
            time.sleep(1.5)
            commany=findelement('.contact-info>h4').text
            excelWrite(count,0,commany)
            try:
                if existElementt('m-mobilephone'):
                    phone = findelement('.m-mobilephone dd').text
                    excelWrite(count,1,phone)
            except Exception:
                pass
            count +=1
            switchToWindow()
            closeOtherWindow()
            time.sleep(2)
        except Exception:
            try:
                switchToWindow()
                closeOtherWindow()
                time.sleep(2)
                r = driver.current_url
                if r!=curr:
                    driver.get(curr)
                    print curr
                    time.sleep(2)
                    waitElement('list-item-itemsWrap')
                    #findelement('#filter_cxtSort').click()
                    li = elementsDisplayer('.detail-float-items')

            except Exception:
                pass
                
    try:
        waitElement('page-next')
        time.sleep(1)
        findelement('.page-next').click()
        #findelement('#filter_cxtSort').click()
        time.sleep(2)
    except Exception:
        driver.refresh()
        waitElement('page-next')
        findelement('.page-next').click()
        #findelement('#filter_cxtSort').click()
        time.sleep(2)
    
