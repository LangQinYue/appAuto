#coding=utf-8
from rule import *
import scriptt
import xlrd,time,os
from xlutils import copy as excelwrite
from  datetime import datetime
import random,string,requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pytesser.pytesser import *
import ImageGrab,Image,ImageEnhance
import picture
#print rule.genRule14()
file = 'name.xlsx'
RANDOM_AGENT_SPOOFER = 'random-agent-spoofer.xpi'
FIREBUG = 'firebug-2.0.7-fx.xpi'
FIREPATH = 'firepath-0.9.7-fx.xpi'
First = ''
Last = ''

def change_proxy():
    os.system('"C:\Users\Administrator\Desktop\911S5\\ProxyTool\\AutoProxyTool.exe" -changeproxy/FR') 
    #os.system('"C:\Documents and Settings\911S5\Desktop\911S5\\ProxyTool\\AutoProxyTool.exe" -changeproxy/AU') 
    time.sleep(3) 
def testNetwork():
    import os
    import subprocess
     
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping www.whoer.net', shell = True, stdout = fnull, stderr = fnull)
    if return1:
        print 'network not ready'
        #change_proxy()
        testNetwork()
        
    else:
        fnull.close()
        return True
def excelWrite(count,j,inserStr):
        data=xlrd.open_workbook(file)
        Wdata=excelwrite.copy(data)
        ws=Wdata.get_sheet(0)
        ws.write(count,j,inserStr)
        Wdata.save(file)  
class mail():
    mailName = ''
    mailPassword = ''

    def __init__(self,dr,s2,url,count):
        profile = webdriver.FirefoxProfile()
        profile.add_extension(os.path.abspath(RANDOM_AGENT_SPOOFER))
        profile.add_extension(os.path.abspath(FIREBUG))
        profile.add_extension(os.path.abspath(FIREPATH))
        profile.set_preference("extensions.firebug.currentVersion", "2.0.7") 
        #self.driver = webdriver.Firefox(firefox_profile=profile) 
        self.driver =dr
        #self.driver = webdriver.Ie()
        self.driver.set_page_load_timeout(120)
        self.url = url
        self.count= count
        self.data = s2
        self.driver.maximize_window()
        
        try:
            self.driver.get(self.url)
        except Exception:  
            #print 'time out after 60 seconds when loading page'  
            self.driver.execute_script('window.stop()')
        
        #self.driver.get(self.url)
        #self.driver.implicitly_wait(20) 
        self.x = 0
        self.itemid = 0
        if 'aol' in self.url or 'aim' in self.url:
            self.itemid = '33142'
        elif 'yahoo' in self.url:
            self.itemid = '11417'
        elif 'zoho' in self.url:
            self.itemid = '4728'
        elif 'outlook' in self.url:
            self.itemid = '4728'
        print self.itemid
        # FirstName
        self.firstId =['FirstName','usernamereg-firstName','sfirstname','firstName','idf'] 
        # LastName
        self.LastId = ['LastName','usernamereg-lastName','lastname','lastName','id11']
        # 邮箱名字
        self.mailId = ['MemberName','usernamereg-yid','username','desiredSN','id22','username','email']
        # 密码输入框
        self.passwordId = ['usernamereg-password','Password','RetypePassword','password','password','verifyPassword','id2c','id2f','password1']
        # 手机号输入框
        self.phoneId = ['usernamereg-phone','PhoneNumber','mobile','confirmMobile','mobileNum']
        # 国家选择
        self.countryId = ['Country','id1a']
        # 手机号国家选择
        self.countryPhoneId = ['PhoneCountry','za_country_code','confirm_country_code','country-code','confirm_country_code']
        # 安全问题输入框
        self.answerId = ['acctSecurityAnswer','id39']
        #验证码输入框
        self.yanzhengmaId = ['wordVerify']
        #年份select
        self.year = ['BirthYear','usernamereg-year']
        #点击按钮 
        self.button = ['CredentialsAction','signupbtn']
        self.s = requests.Session()
        self.cid = ''

    def excelWrite(self,count,j,inserStr):
            data=xlrd.open_workbook(file)
            Wdata=excelwrite.copy(data)
            ws=Wdata.get_sheet(0)
            ws.write(count,j,inserStr)
            Wdata.save(file)  
    
    def getPhone(self):
        url = 'http://api.shjmpt.com:9002/pubApi/uLogin'
        payload = {'uName': 'jianqian1993', 'pWord': 'l19930329','Developer':'Developer=7tb5RKK22u6%2fU6lovcZCtA%3d%3d'}
        rs = self.s.get(url,params=payload)
        token = rs.content.split('&')[0]
        url = 'http://api.shjmpt.com:9002/pubApi/GetPhone'
        payload = {'token': token, 'ItemId': self.itemid}
        rs = self.s.get(url,params=payload)
        phone = rs.content.split(';')[0]
        return phone,token
    
    def getMessage(self,token,phone):

        url = 'http://api.shjmpt.com:9002/pubApi/GMessage'
        payload = {'token': token, 'ItemId': self.itemid,'Phone':phone}
        rs = self.s.get(url,params=payload)
        print rs.content
        return rs.content.split('&')[-1]
    
    def getby(self,by):
        getby_dict = {'ID':By.ID,
             'CLASS_NAME':By.CLASS_NAME,
             'CSS_SELECTOR':By.CSS_SELECTOR,
             'LINK_TEXT':By.LINK_TEXT,
             'NAME':By.NAME,
             'PARTIAL_LINK_TEXT':By.PARTIAL_LINK_TEXT,
             'TAG_NAME':By.TAG_NAME,
             'XPATH':By.XPATH
             }
        try:
            if by.upper() in getby_dict:
                bytype = getby_dict[by.upper()]
            return bytype
        except Exception:
            print by+'not found'   
    
    def find_element(self,by,value): 
        by = self.getby(by)
        try:
            WebDriverWait(self.driver,1).until(ec.presence_of_element_located((by,value)))
            if self.driver.find_element(by,value).is_displayed():
                return self.driver.find_element(by,value)
        except Exception,e:
            pass
            #print 'not find %s,name %s' % (value,self.data[1])
    
    def nextElement(self,ele):
        ele.send_keys(Keys.TAB)
        time.sleep(0.5)
        return self.driver.switch_to_active_element()
    def elementSendkey(self,value,text,flag=1,by="CSS_SELECTOR"):
        if flag:
            element = self.find_element(by,value)
        else:
            element = value
        element.clear()
        element.send_keys(text)
        ActionChains(self.driver).send_keys(Keys.ENTER)
        time.sleep(1)
    def elementClick(self,value,flag=1,by="CSS_SELECTOR"):
        if flag:
            element = self.find_element(by,value)
        else:
            element = value
        element.click()
        time.sleep(1.5)
     
    def elementSelect(self,value,flag=1,by="CSS_SELECTOR"):
        if flag:
            element = self.find_element(by,value)
        else:
            element = value
        select  = Select(element)
        num = len(Select(element).options)-1
        select.select_by_index(random.randint(1,num))
        time.sleep(1.5)
    def countrySelect(self,value,flag=1,by="CSS_SELECTOR"):
        if flag:
            element = self.find_element(by,value)
        else:
            element = value
        select  = Select(element)
        select.select_by_value('CN')
        time.sleep(1.5)
    def elementSelectt(self,value,flag=1,by="CSS_SELECTOR"):
        if flag:
            element = self.find_element(by,value)
        else:
            element = value
        select  = Select(element)
        num = len(Select(element).options)
        select.select_by_value('19%s' % str(random.randint(77, 97)))
        time.sleep(1.5)
    def elementsSelect(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        select  = Select(element)
        num = len(Select(element).options)-1
        select.select_by_index(random.randint(1,num))
        time.sleep(1.5)
    def existElement(self,typee,value):
        a= []
        if typee == 'class':
            jsa  = '''
                return document.getElementsByClassName('%s')
                ''' % value
        else:
            jsa  = '''
                return document.getElementById('%s')
                ''' % value
        try:
            a=self.driver.execute_script(jsa)
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
    def redYanzhengma(self,x,y,xx,yy):
        
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        img = ImageGrab.grab()
        img.save("login.png")
        #cut the random number
        
        img = Image.open(r'login.png')
        region = (x,y,xx,yy)
        cropImg = img.crop(region)
        cropImg.save(r'11.jpg')
        #change the random number to string
#         im=Image.open("11.jpg")
#         imgry = im.convert('L')
#         sharpness =ImageEnhance.Contrast(imgry)
#         sharp_img = sharpness.enhance(2.0)
#         sharp_img.save("12.jpg")
        self.cid,code = picture.run()
        return code,self.cid
        '''
        image = Image.open("12.jpg")
        valid_code = image_to_string(image)
        return valid_code
        '''
    def genterMailName(self):
        num = random.randint(1,17)
        #print num
        func = 'genRule'+str(num)
        if num in [1,2,3,4,5]:
            tr = self.data[0]+self.data[1]+getattr(rule, func)()
        elif num in (6,7,8,9,10):
            tr = self.data[0]+getattr(rule, func)()
        elif num in (11,12,13,14):
            tr = self.data[1]+getattr(rule, func)()
        elif num in (15,16,17):
            tr = getattr(rule, func)()
        return tr
    def test(self):
        t = 'sdfsdfsdf'
        mail.mailName = t
        
    def r(self):
        if self.existElement('class','buttonLargeWhite'):
            self.elementClick('.buttonLargeWhite')
            time.sleep(20)
        if self.existElement('class','personal-form'):
            time.sleep(20)
            self.elementClick('.personal-form')
        if self.existElement('id','getSn'):
            self.elementClick('#getSn')
        if self.existElement('id','login-signup'):
            self.elementClick('#login-signup')
        if self.existElement('id','signup'):
            self.elementClick('#signup')
        if self.existElement('id','signup-button'):
            self.elementClick('#signup-button')
        if self.existElement('class','email'):
            eles = self.driver.find_elements_by_css_selector('.icon.email')
            random.choice(eles).click()
            time.sleep(5)
            if self.existElement('class', 'btn-register'):
                self.elementClick('.btn-register')
                time.sleep(10)
        if self.existElement('class','btn-register'):
            self.elementClick('.btn.btn-big.btn-register')
        ele = self.driver.find_element_by_tag_name('body')
        phoneflag = 1
        phone = 1
        passwordstr = 1
        passwordflag = 1
        token = ''
        phone = ''
        cid = 0
        tr = ''
        while True:
            try:          
                ele = self.nextElement(ele)
            except Exception:
                pass
            if ele.get_attribute('tagName') == 'SELECT':
                if ele.get_attribute('id') in self.countryId:
                    self.countrySelect(ele, 0)
                    continue
                elif ele.get_attribute('id') in self.countryPhoneId:
                    self.countrySelect(ele, 0)
                    continue 
                elif ele.get_attribute('name') == 'shortCountryCode':
                    self.countrySelect(ele, 0)
                    continue               
                elif ele.get_attribute('id') == 'gender1':
                    radioo = self.driver.find_elements_by_css_selector('input[type=radio]')
                    random.choice(radioo).click()
                    continue
                else:
                    self.elementSelect(ele,0)
                    if ele.get_attribute('id') in self.year:
                        self.elementSelectt(ele, 0)
                        if self.existElement('id', 'usernamereg-freeformGender'):
                            self.elementSendkey('#usernamereg-freeformGender', random.choice(('Female','Male')))
                    if self.existElement('id', 'dobYear'):
                        self.elementSendkey('#dobYear', '19%s'%(random.randint(65,89)))
                    if self.existElement('id', 'dobDay'):
                        self.elementSendkey('#dobDay', '%s'%(random.randint(1,28)))
 
                    continue
                    #self.elementsSelect(ele)
            if ele.get_attribute('tagName') == 'INPUT':
                if ele.get_attribute('id') in self.firstId :
                    self.elementSendkey(ele, self.data[0], 0)
                    continue
                elif ele.get_attribute('id') in self.LastId :
                    self.elementSendkey(ele, self.data[1], 0)
                    if self.existElement('id', 'country_code'):
                        self.countrySelect('#country_code')
                    if self.existElement('id', 'confirm_country_code'):
                        self.countrySelect('#confirm_country_code')
                    if self.existElement('id', 'firstName'):
                        self.elementSendkey('#firstName', self.data[0])
                    if self.existElement('id', 'FirstName'):
                        self.elementSendkey('#FirstName', self.data[0])
                    continue
                elif ele.get_attribute('id') in self.mailId :
                    tr = self.genterMailName()
                    if ele.get_attribute('class') == 'sgnemail' and ele.get_attribute('id') == 'email':
                        contactEmail = rea_excel()
                        self.elementSendkey('#email', contactEmail)
                        continue  
                    if self.existElement('id', 'MemberName'):
                        pass
                    if self.existElement('id', 'username-toggle'):
                        self.elementClick('#username-toggle')
                        self.elementSendkey('#desiredSN', tr)
                        ele =  self.find_element('id', 'desiredSN')
                        continue
                    self.elementSendkey(ele, tr, 0)
                    if self.existElement('id', 'SignupPageTitle'):
                        self.elementClick('#SignupPageTitle')
                        time.sleep(3)
                    continue
                elif ele.get_attribute('id') in self.phoneId :
                    #token = self.getToken()
                    if phoneflag:
                        phone,token = self.getPhone()
                        #phone = '13078663244'
                        phoneflag = 0
                    self.elementSendkey(ele,phone, 0)
                    print ele.text
                    continue
                elif ele.get_attribute('id')  == 'desiredSN' :
                    name = self.driver.find_elements_by_css_selector('fsdf')
                    
                elif ele.get_attribute('id') in self.passwordId :
                    if passwordflag:
                        passwordstr = ''.join(random.sample(string.ascii_uppercase+string.digits, random.randint(9,12)))
                        passwordflag = 0
                    self.elementSendkey(ele, passwordstr, 0)
                    if self.existElement('id', 'SignupPageTitle'):
                        self.elementClick('#SignupPageTitle')
                    self.excelWrite(self.count,3,passwordstr)
                    mail.mailPassword = passwordstr
                    continue
                elif ele.get_attribute('id') in self.answerId :
                    answerstr = ''.join(random.sample(string.ascii_letters, random.randint(3,20)))
                    self.elementSendkey(ele, answerstr, 0)
                    if self.existElement('class', 'ddArrow'):
                        element = self.driver.find_element_by_css_selector('.ddArrow')
                        element.click()
                        time.sleep(2)
                        self.elementClick(".//*[@id='country-code_child']/ul/li[44]/span", 1, 'xpath')
                    continue
                elif ele.get_attribute('id') == 'wordVerify' :
                    while self.existElement('id', 'wordVerify'):
                        codeInput = self.find_element('CSS_SELECTOR', '#wordVerify')
                        codeInput.click()
                        code = self.redYanzhengma(538, 380, 760, 500)
                        self.elementSendkey('#wordVerify', code)
                        self.elementClick('#signup-btn')
                        time.sleep(10)
                    time.sleep(4)
                    for i in xrange(4):
                        if self.existElement('id', 'mobileConfirmCode'):
                            break
                        if self.existElement('class', 'error-text'):
                            error = self.driver.find_element_by_css_selector('.error-text')
                            if 'username ' in error.text or 'email ' in error.text:
                                name = self.driver.find_elements_by_css_selector('.sn-suggest-link')
                                random.choice(name).click()
                                self.elementClick('#signup-btn')
                                time.sleep(2)
                            elif 'phone' in error.text:
                                phone,token = self.getPhone()
                                self.elementSendkey('#mobileNum', phone)
                                self.elementClick('#signup-btn')
                                time.sleep(2)                            
                    if self.existElement('id', 'mobileConfirmCode'):
                    
                        #message = self.getMessage(token, phone)
                        for i in xrange(8):
                            
                            code = self.getMessage(token, phone).split(' ')[0]
                            print code
                            if  'False' in code:
                                time.sleep(6)
                            else:
                                break

                        time.sleep(5)
                        self.elementSendkey('#mobileConfirmCode', code)
                        self.elementClick('#signup-btn')
                        if self.existElement('class', 'username-highlight'):
                            mailText = self.find_element('CSS_SELECTOR', 'username-highlight')
                            cod = mailText.text
                            self.excelWrite(self.count, 2, cod)
                            mail.mailName = cod
                        
                    break
                # outlook yanzhengma
                elif 'spHipNoClear' in ele.get_attribute('class'):
                    codeInput = self.find_element('CSS_SELECTOR', '.spHipNoClear')
                    codeInput.click()
                    code,self.cid = self.redYanzhengma(202,310,467,450)
                    print code
                    a = 'abdcde'
                    self.elementSendkey('.spHipNoClear', code)
                    continue
                              
                
                elif ele.get_attribute('id') in self.yanzhengmaId :
                    answerstr = ''.join(random.sample(string.ascii_letters, 8))
                    self.elementSendkey(ele, answerstr, 0)
                    continue 
                elif ele.get_attribute('id') == 'user_namesurname' :
                    namestr = self.data[0] + '_' + self.data[1]
                    self.elementSendkey(ele, namestr, 0)
                    continue                 
                elif ele.get_attribute('type') == 'checkbox':
                    if self.existElement('id', 'iOptinEmail'):
                        continue
                    self.elementClick(ele, 0)
                elif ele.get_attribute('id') == 'zipCode':
                    self.elementSendkey(ele,''.join(random.sample(string.digits, random.randint(5,5))), 0,)
                #zoho
                elif ele.get_attribute('id') == 'signupbtn':
                    try:
                        for i in xrange(2):
                        
                            self.countrySelect('select[id*=country_code]')
                    except  Exception:
                        pass
                    try:
                        for i in xrange(10):
                            ele.click()
                    except Exception:
                        pass
                    time.sleep(30)
                    if self.existElement('id', 'verifyCode'):
                        for i in xrange(40):
                            code = self.getMessage(token, phone)
                            print code
                            if  'False' in code:
                                time.sleep(10)
                            else:
                                co = code.split(' ')[0]
                                
                                print co
                                break
                        #codee = self.getMessage(token, phone)
                        self.elementSendkey('#verifyCode', co)
                        self.elementClick('#buttonloader')
                    while self.existElement('class', 'jqval-error'):
                        connectmail = rea_excel()
                        self.elementSendkey('#email', connectmail)
                        ele.click()
                        time.sleep(5)
                    self.excelWrite(self.count, 2, tr+'@zoho.eu')
                    mail.mailName = tr+'@zoho.eu'
                    time.sleep(120)
                    
                    if self.existElement('class', 'msi-close'):
                        self.elementClick('.msi-close')
                        self.excelWrite(self.count, 2, tr+'@zoho.eu')
                    break
                #outlook
                elif ele.get_attribute('id') == 'CredentialsAction':
                    
                    ele.click()
                    time.sleep(5)
                    def mailname():
                        self.elementSendkey('#MemberName', self.genterMailName())
                        self.elementClick('#SignupPageTitle')
                        time.sleep(3)
                        ele.click()
                    while self.existElement('id', 'MemberNameError'):
                        mailname()
                    #ele.click()
                    def yanzhengma():
                        picture.error(self.cid)
                        code,self.cid = self.redYanzhengma(202,310,467,450)
                        self.elementSendkey('.spHipNoClear', code)
                        ele.click()
                        time.sleep(5)
                    
                    while 1:
                        try:
                            
                            if len(self.find_element('css_selector','input[id*=wlspispSolutionElement]').get_attribute('value'))==0:
                                if not self.find_element('css_selector', '.btn-primary[title="Send SMS code"]'):
                                    if self.existElement('id', 'CredentialsAction'):
                                        yanzhengma()
                            else:
                                break

                        except Exception:
                            break
                    try:
                        for i in  xrange(3):
                            ele.click()
                    except Exception:
                        pass
                    time.sleep(17)
                    if self.existElement('class', 'btn-primary'):
                        try:
                            self.elementClick('.btn-primary[title="Send SMS code"]')
                            for i in xrange(4):
                                
                                code = self.getMessage(token, phone)
                                print code
                                if  'False' in code:
                                    time.sleep(10)
                                else:
                                    co = code.split(':')[-1].split('[')[0].strip()
                                    
                                    print co
                                    break
                            time.sleep(5)
                            self.elementSendkey('input[aria-label*="Invalid"]', co)
                            self.elementClick('#SignupPageTitle')

                            for i in xrange(4):
                                ele.click()
                                time.sleep(2)
                        except Exception:
                            pass
                    time.sleep(40)
                    try:
                        self.elementClick('.nextButton>img')
                    except Exception:
                        pass
                    '''
                    se = self.driver.find_elements_by_css_selector('#rw_3__listbox .rw-list-option')
                    random.choice(se).click()
                    zone = self.driver.find_elements_by_css_selector('#rw_4__listbox .rw-list-option')
                    random.choice(se).click()
                    '''
                    self.elementClick('.nextButton>img')
                    time.sleep(2)
                    self.elementClick('.nextButton>img')
                    time.sleep(2)
                    yangshi = self.driver.find_elements_by_css_selector('.buttonGroup div')
                    random.choice(yangshi).click()
                    self.elementClick('.nextButton>img')
                    time.sleep(20)
                    tr = self.driver.find_element_by_class_name('upn').text
                    self.excelWrite(self.count, 2, tr)
                    mail.mailName = tr
                    break
                #AOL anniu
                elif ele.get_attribute('id') == 'signup-btn':
                    ele.click()
                    time.sleep(4)
                    for i in xrange(4):
                        if self.existElement('id', 'mobileConfirmCode'):
                            break
                        if self.existElement('class', 'error-text'):
                            error = self.driver.find_element_by_css_selector('.error-text')
                            print error.text
                            if 'username ' in error.text or 'email ' in error.text:
                                name = self.driver.find_elements_by_css_selector('.sn-suggest-link')
                                random.choice(name).click()
                                self.elementClick('#signup-btn')
                                time.sleep(2)
                            elif 'phone' in error.text:
                                phone,token = self.getPhone()
                                self.elementSendkey('#mobileNum', phone)
                                self.elementClick('#signup-btn')
                                time.sleep(2)                            
                    if self.existElement('id', 'mobileConfirmCode'):
                    
                        #message = self.getMessage(token, phone)
                        for i in xrange(80):
                            
                            code = self.getMessage(token, phone).split(' ')[0]
                            print code
                            if  'False' in code:
                                time.sleep(6)
                            else:
                                break

                        time.sleep(5)
                        self.elementSendkey('#mobileConfirmCode', code)
                        self.elementClick('#signup-btn')
                        if self.existElement('class', 'username-highlight'):
                            mailText = self.find_element('CSS_SELECTOR', '.username-highlight')
                            cod = mailText.text
                            self.excelWrite(self.count, 2, cod)
                            mail.mailName = cod
                    break
                    
                else:
                    if ele.get_attribute('type') == 'radio':
                        radioo = self.driver.find_elements_by_css_selector('input[type=radio]')
                        random.choice(radioo).click()
                    continue

            if ele.get_attribute('tagName') == 'BUTTON':
                if ele.get_attribute('id') == 'submitimg':
                    ele.click()
                    break    
                #yahoo确定按钮
                if ele.get_attribute('id') == 'reg-submit-button':
                    ele.click()
                    time.sleep(2)
                    for i in xrange(4):
                        if self.existElement('id', 'reg-error-phone'):
                            phone,token = self.getPhone()
                            self.elementSendkey('#usernamereg-phone', phone)
                            self.elementSendkey('#usernamereg-password',''.join(random.sample(string.ascii_uppercase+string.digits, random.randint(9,12))))
                            self.elementSendkey('#usernamereg-freeformGender', random.choice(('Female','Male')))                    
                            self.elementClick('#reg-submit-button')
                    #break
                else:
                    continue
def rea_excel():
    table = xlrd.open_workbook(file)
    sheet = table.sheet_by_index(0)
    nrows = sheet.nrows
    for i in xrange(30,nrows):
        s1 = sheet.row_values(i)
        if s1[4]== 'y':
            pass
        s2 = [str(x).split('.')[0] if 'float' in str(type(x)) else str(unicode(x).encode('utf-8')) for x in s1]  # utf-8 encoding
        excelWrite(i,4,'y')
        return s2[2]
        
def readExcel():
    #print dr
    profile = webdriver.FirefoxProfile()
    profile.add_extension(os.path.abspath(RANDOM_AGENT_SPOOFER))
    profile.add_extension(os.path.abspath(FIREBUG))
    profile.add_extension(os.path.abspath(FIREPATH))
    profile.set_preference("extensions.firebug.currentVersion", "2.0.7") 
    dr = webdriver.Firefox(firefox_profile=profile) 
    try:
        table = xlrd.open_workbook(file)
    except Exception,e:
        print str(e)
       
    sheet = table.sheet_by_index(0)  # by index
    nrows = sheet.nrows 
    for i in xrange(30,nrows):

        s1 = sheet.row_values(i)
        if s1[2] != '':
            continue
        
        #excelWrite(i,4,'y')


        change_proxy()
        if 1:
            s2 = [str(x).split('.')[0] if 'float' in str(type(x)) else str(unicode(x).encode('utf-8')) for x in s1]  # utf-8 encoding
            First = s2[0]
            Last = s2[1]
            urlList = ['http://outlook.live.com/owa/','http://mail.zoho.com','http://mail.aol.com','http://www.aim.com']

            url = random.choice(urlList)
            url = 'http://outlook.live.com/owa/'
            print url
            r = mail(dr,s2,url,i)
            print r.mailId
            driver = r.driver
            #r.redYanzhengma()
            if 'zoho' in url:
                time.sleep(10)
            r.r()
            #r.mailName = 'Nadiraimpact931@aol.com'
            #r.mailPassword = '5I7DH2BA139U'
            print 'end'
            print r.mailName,r.mailPassword
            #dr.get(url)
            '''
            ele  = dr.find_element_by_css_selector('body')
            def nextelement():
                ele.send_keys(Keys.TAB)
                time.sleep(0.5)
                return dr.switch_to_active_element()
            ele = nextelement() 
            ele.send_keys(mailName)
            ele = nextelement()
            ele.send_keys(mailPassword)
            ele = nextelement()
            ele.click()
            '''
            '''
            curr_window = dr.current_window_handle
            action = ActionChains(dr)
            action.send_keys(Keys.CONTROL+'t').perform()
            
            #print curr_window+'3333'
            handles = dr.window_handles
            print handles
            #print handles
            for handle in handles:
                if handle != curr_window:
                    dr.switch_to_window(handle)
            
            action = ActionChains(dr)
            action.send_keys(Keys.CONTROL+'t').perform()
            scriptt.readExcell(dr,r.mailName)
            #driver.quit()
            time.sleep(300)
            action = ActionChains(dr)
            action.send_keys(Keys.CONTROL+'t').perform()
            dr.get(url)
            if 'aol' in url:
                dr.find_element_by_css_selector('#lgnId1').send_keys(r.mailName)
                dr.find_element_by_css_selector('#pwdId1').send_keys(r.mailPassword)
                dr.find_element_by_css_selector('#submitID').click()
                time.sleep(30)
                dr.find_element_by_css_selector('#uniqName_4_5').click()
                dr.find_element_by_css_selector('#inboxNode').click()
            '''
                
                
            
#dr = webdriver.Firefox()
#dr.get('http://www.baidu.com')
readExcel()