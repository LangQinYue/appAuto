#!coding=utf-8
import sys,os,time,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver

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
option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"images":2}}
option.add_experimental_option('prefs', prefs)
flag = raw_input(u"请输入执行方式，0：新开始，   1：接下去运行\n")
driver = webdriver.Chrome(executable_path='D:\Program Files\Chrome\chromedriver.exe',chrome_options=option)
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
findelement('#TPL_username_1').send_keys(u'三点水1217')
findelement('#TPL_password_1').send_keys('hytre5886')
findelement('#J_SubmitStatic').click()
f = open('url.txt','r')
stt = f.read()
f.close()
if stt and int(flag):
    driver.get(stt)
else:
    #findelement('body').click()
    time.sleep(1)
    element = findelement('.first.fd-left.current>a')
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(1)
    if existElementt('close'):
        findelement('.close').click()
        time.sleep(1)
    findelement('.current-next a[title="供应商"]').click()
    findelement('#alisearch-keywords').send_keys(u'张家口')
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
    waitElement('list-item-itemsWrap')
    li = elementsDisplayer('.list-item-itemsWrap')
    for i,j in enumerate(li):
        try:
            product = elementsDisplayer('.list-item-itemsWrap li',li[i])
            driver.execute_script("arguments[0].scrollIntoView();", product[0])
            product[0].click()
            time.sleep(2)
            switchToWindow()
            waitElement('amount-input')
            shuxing = elementsDisplayer('.amount .control .amount-input')
            shuxing[0].send_keys('300')
            time.sleep(1)
            findelement('body').click()
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", findelement('.do-purchase.ms-yh>span'))
            findelement('.do-purchase.ms-yh>span').click()
            #time.sleep(3)
            str = u'''
    我们是河北阿里巴巴中国站商盟的，如此款产品是一手货源，请于5.12日《商盟活动日》发一张实拍图片到商盟的官方公众号。
    
    ①免费做15天高质量卡位补单（shua单）。
    ②直接报名参加“伙拼周末团”的活动，当天就能通过活动，位置是在伙拼箱包首页的前10位置。
    ③会把商盟3000多个分销商对接到你店铺，（这些分销商，每家每天卖货量都超30单）确保成功对接10家能卖货的分销商，然后去上架卖这款产品，行业top前十卖家把分销商资源共享出来了，确保这款产品代发销量每天达到10单以上。
    这期活动是免费活动，和前三期活动一样，也是10个名额。
    
    关注商盟微信公众号：河北1688商盟
    
            '''
            waitElement('textarea-trigger')
            if findelement('.fee').get_attribute('class') == 'input fee':
                try:
                    findelement('.input.fee').send_keys('1')
                except Exception:
                    pass
            findelement('.textarea-trigger').click()
            findelement('.textarea-content .input').send_keys(str)
            findelement('body').click()
            driver.find_element_by_xpath('//label[@for="unit-tag-radio-trade-mode-1-1"]').click()
            findelement('.button.button-important.button-large.make-order').click()
            #driver.close()
            time.sleep(3)
            switchToWindow()
            closeOtherWindow()
            time.sleep(2)
        except Exception:
            try:
                switchToWindow()
                closeOtherWindow()
                time.sleep(2)
                r = driver.current_url
                if curr!=r:
                    driver.get(curr)
                    print curr
                    time.sleep(2)
                    waitElement('list-item-itemsWrap')
                    #findelement('#filter_cxtSort').click()
                    li = elementsDisplayer('.list-item-itemsWrap')

            except Exception:
                pass
                
        #li = elementsDisplayer('.list-item-itemsWrap')
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
    
