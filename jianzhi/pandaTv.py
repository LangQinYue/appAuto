#!coding=utf-8
import sys,os,time,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import requests
import win32api
cid = ''
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
s = requests.Session()
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
def getPhone():
    url = 'http://api.hellotrue.com/api/do.php?'
    payload = {'action':'loginIn','name': 'api-44g3rokq', 'password': 'm123456789'}
    rs = s.get(url,params=payload)
    token = rs.content.split('|')[1]
    url = 'http://api.hellotrue.com/api/do.php?'
    payload = {'action':'getPhone','token': token, 'sid': "1016,1076"}
    
    rs = s.get(url,params=payload)
    #print rs.url
    print '获取手机号中'
    print rs.url
    a = 0
    while rs.content.split('|')[0] == '0':
        if a == 15:
            return 0
        time.sleep(3)
        
        rs = s.get(url,params=payload)
        print rs.content
        print '获取手机号中'
        a+=1

    phone = rs.content.split('|')[1]
    return phone,token
def getMessage(token,phone):
    import re
    url = 'http://api.hellotrue.com/api/do.php?'
    payload = {'action':'getMessage','sid':41223,'phone':phone,'token': token}
    rs = s.get(url,params=payload)
    print u'获取注册手机短信'
    for i in  xrange(25):
        if  rs.content.split('|')[0] == '0':
            time.sleep(3)
            rs = s.get(url,params=payload)
            #print rs.content
            print u'获取注册手机短信'
    a = rs.content
    if rs.content.split('|')[0] == '0':
        driver.quit()
    print a
    m=re.findall(r'\d{6,6}',rs.content)
    if m:
        print m
        print m[0]
        return m[0]
    else:
        return 0
def getIP():
    import requests
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
    s = requests.Session()
    url = 'http://api.ip.data5u.com/api/get.shtml?order=391c3f1845b0ec9b1ad363fb78801df3&num=1&area=%E4%B8%AD%E5%9B%BD&carrier=0&protocol=0&an1=1&an2=2&an3=3&sp1=1&sort=1&system=1&distinct=0&rettype=1&seprator=%0D%0A'
    rs = s.get(url)
    print rs.content
    a = rs.content.split('\n')[0].split('\r')
    return a
option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"images":1}}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path=r"D:\Program Files\Chrome\chromedriver.exe",chrome_options=option)
profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 1)
#driver = webdriver.Firefox()
profile.update_preferences() 
#driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.panda.tv/')
waitElement('tool-user-info-regist')
findelement('.tool-user-info-regist.header-register-btn').click()
#shur ru shouji hao
findelement('.ruc-input-name.ruc-input-register-name').send_keys(u'15800959395')

findelement('.ruc-send-auth-code-btn').click()
time.sleep(2)
collage = s.get('https://verify.panda.tv/captcha/get?app=pandatv')
jsonstr = collage.json()
challenge = jsonstr['data']['challenge']
gt = jsonstr['data']['gt']
print challenge,gt
print collage.content,collage.text
payload = {'gt': gt, 'challenge': challenge,'referer':'http://www.panda.tv','user':'qweqwe123456','pass':'qweqweqwe','return':'json'}
r = requests.get("http://jiyanapi.c2567.com/shibie", params=payload)
jsonstrr = r.json()
while jsonstrr['status'] == 'no':
    collage = requests.get('https://verify.panda.tv/captcha/get?app=pandatv')
    jsonstr = collage.json()
    challenge = jsonstr['data']['challenge']
    gt = jsonstr['data']['gt']
    payload = {'gt': gt, 'challenge': challenge,'referer':'http://www.panda.tv','user':'qweqwe123456','pass':'qweqweqwe','return':'json'}
    r = requests.get("http://jiyanapi.c2567.com/shibie", params=payload)
    jsonstrr = r.json()
challenge = jsonstrr['challenge']
validate = jsonstrr['validate']
payload = {'challenge': challenge,'validate':validate,'seccode':validate+'|jordan'}
r = s.get("https://verify.panda.tv/captcha/verifyCode", params=payload)
jsonstrr = r.json()

#yan zheng ma
findelement('.ruc-input-register-auth').send_keys(u'yanzma')

