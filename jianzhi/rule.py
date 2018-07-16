
#coding=utf-8
import string,random
import xlrd
from xlutils import copy as excelwrite
file = r'danciku.xls'
class rule():
    @classmethod
    def excelWrite(self,count):
            data=xlrd.open_workbook(file)
            Wdata=excelwrite.copy(data)
            ws=Wdata.get_sheet(0)
            ws.write(count,1,'y')
            Wdata.save(file)
    @classmethod
    def rea_excel(self):
        table = xlrd.open_workbook(file)
        sheet = table.sheet_by_index(0)
        nrows = sheet.nrows
        for i in xrange(1,nrows):
            s1 = sheet.row_values(i)

            if s1[1]== 'y':
                continue
            s2 = [str(x).split('.')[0] if 'float' in str(type(x)) else str(unicode(x).encode('utf-8')) for x in s1]  # utf-8 encoding
            self.excelWrite(i)
            return s2[0]
    @classmethod
    def genRule1(self):
        return ''
    
    #随机生成1-2个字母
    @classmethod
    def genRule2(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(2,3)))
    
    #随机生成1-4个数字
    @classmethod
    def genRule3(self):
        return ''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #Frist + Last + A-Z随机字母1-3个 + 0-9随机数字1-4个
    @classmethod
    def genRule4(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(1,3)))+''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #Frist + Last + 单词（单词库顺序抽取）
    @classmethod
    def genRule5(self):
        return self.rea_excel()  
    
    #Frist + 单词（单词库顺序抽取）
    @classmethod
    def genRule6(self):
        return self.rea_excel()  
    
    #Frist + 单词 + 0-9随机数字1-4个
    @classmethod
    def genRule7(self):
        return self.rea_excel()+''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #Frist + A-Z随机字母1-4个
    @classmethod
    def genRule8(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(3,4)))  
    
    #Frist + 0-9随机数字1-4个
    @classmethod
    def genRule9(self):
        return ''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #Frist + A-Z随机字母1-3个 + 0-9随机数字1-4个
    @classmethod
    def genRule10(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(2,3)))  +''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #Last + A-Z随机字母1-5个
    @classmethod
    def genRule11(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(4,5)))  
    
    #Last + 0-9随机数字1-5个
    @classmethod
    def genRule12(self):
        return ''.join(random.sample(string.digits, random.randint(4,5)))  
    
    #Last + A-Z随机字母1-5个 + 0-9随机数字1-5个
    @classmethod
    def genRule13(self):
        return ''.join(random.sample(string.ascii_letters, random.randint(3,5)))  +''.join(random.sample(string.digits, random.randint(3,5)))    
    
    #Last + 单词（单词库顺序抽取） + 0-9随机数字1-4个
    @classmethod
    def genRule14(self):
        return self.rea_excel()+''.join(random.sample(string.digits, random.randint(3,4)))  
    
    #单词 + 0-9随机数字1-8个
    @classmethod
    def genRule15(self):
        return self.rea_excel()+''.join(random.sample(string.digits, random.randint(5,8)))  
    
    #单词 + A-Z随机字母1-6个
    @classmethod
    def genRule16(self):
        return self.rea_excel()+''.join(random.sample(string.ascii_letters, random.randint(5,6)))
    
    #单词  + A-Z随机字母1-6个 + 0-9随机数字1-6个
    @classmethod
    def genRule17(self):
        return self.rea_excel()+''.join(random.sample(string.ascii_letters, random.randint(3,6)))  +''.join(random.sample(string.digits, random.randint(4,6)))  

    @classmethod
    def genRule18(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3,4)))  
