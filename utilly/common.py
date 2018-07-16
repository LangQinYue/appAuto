#!coding=utf-8
'''
Created on 2016年6月25日

@author: lx-lang.qinyue
'''

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
'''
Created on 2015年8月19日

@author: xun
'''
import httplib2
import json
import xlwt
import sqlite3
import xlrd
from dominate.tags import table
import datetime
import pymysql

class oprMysql:
    def __init__(self,host,user,passwd,db,port,charset):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.port = port
        self.conn=pymysql.connect(host = self.host,user = self.user,passwd = self.passwd,db = self.db,port = self.port,charset = self.charset)
        self.cur = self.conn.cursor()
            
    def getTablesName(self):
        self.cur.execute('show tables')
        result = self.cur.fetchall()
        tablesname = []
        i = 0
        while i <len(result):
            tablesname.append(result[i][0])
            i = i+1
        return tablesname
    
    def getTableHeader(self,tablename):
        self.cur.execute('describe %s'%tablename)
        result = self.cur.fetchall()
        header = []
        for i in result:
            header.append(i[0])       
        return header
    
    def getTableData(self,tablename):
        self.cur.execute('select * from %s'%tablename)
        data = self.cur.fetchall()
        return data
    
    def getTablesHeader(self,tablesname):
        data = {}
        for tablename in tablesname:
            self.cur.execute('describe %s'%tablename)
            tables = self.cur.fetchall()
            header = []
            for i in tables:
                header.append(i[0])   
            data.setdefault(tablename,header)                              
        return data
    
    def getTablesData(self,tablesname):
        data = {}
        for tablename in tablesname:
            self.cur.execute('select * from %s'%tablename)
            tabledata = self.cur.fetchall()
            data.setdefault(tablename,tabledata)
        return data
    
    def closeConnect(self):                  
        self.cur.close()
        self.conn.commit()  
        self.conn.close()
        
    def toExcel(self,excelpath):     
        tablesname = self.getTablesName()
        tablesheader = self.getTablesHeader(tablesname)
        tablesdata = self.getTablesData(tablesname)
        self.closeConnect()
        excel = oprexcel(excelpath)
        excel.saveTables(tablesname, tablesheader, tablesdata)
    

        
        
class oprsqlite:
    def __init__(self,sqlpath):
        self.sqlpath = sqlpath
        self.cx = sqlite3.connect(sqlpath)
        self.cu = self.cx.cursor()

    def getTablesName(self):
        self.cu.execute('select name from sqlite_master where type = "table" order by name')        
        tables = self.cu.fetchall()
        tablesname = []
        i = 0
        while i <len(tables):
            tablesname.append(tables[i][0])
            i = i+1
        return tablesname
    
    def getTableHeader(self,tablename):
        self.cu.execute('PRAGMA table_info(%s)'%tablename)
        tables = self.cu.fetchall()
        header = []
        for i in tables:
            header.append(i[1])          
        return header
    
    def getTableData(self,tablename):
        self.cu.execute('select * from %s'%tablename)
        data = self.cu.fetchall()
        return data
    
    def getTablesHeader(self,tablesname):
        data = {}
        for tablename in tablesname:
            self.cur.execute('describe %s'%tablename)
            tables = self.cur.fetchall()
            header = []
            for i in tables:
                header.append(i[0])   
            data.setdefault(tablename,header)                                   
        return data
    
    def getTablesData(self,tablesname):
        data = {}
        for tablename in tablesname:
            self.cu.execute('select * from %s'%tablename)
            tabledata = self.cu.fetchall()
            data.setdefault(tablename,tabledata)
        return data
    
    def closeConnect(self):
        self.cx.close()

    def toExcel(self,excelpath):     
        tablesname = self.getTablesName()
        tablesheader = self.getTablesHeader(tablesname)
        tablesdata = self.getTablesData(tablesname)
        self.closeConnect()
        excel = oprexcel(excelpath)
        excel.saveTables(tablesname, tablesheader, tablesdata)          
              
class oprexcel:
    def __init__(self,excelpath):
        self.excelpath = excelpath
    
    def saveTable(self,tablename,tableheader,tabledata):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(tablename,cell_overwrite_ok=True) 
        for i in range(0,len(tableheader)):
            sheet1.write(0,i,tableheader[i])
        i = 0
        while i < len(tabledata):
            for j in range(0,len(tabledata[i])):
                sheet1.write(i+1,j,tabledata[i][j])
            i = i+1
        f.save(self.excelpath)
        
    def saveTables(self,tablesname,tablesheader,tablesdata):
        f = xlwt.Workbook()
        for tablename in tablesname:
            sheet1 = f.add_sheet(tablename,cell_overwrite_ok=True) 
            for i in range(0,len(tablesheader.get(tablename))):
                sheet1.write(0,i,tablesheader.get(tablename)[i])
            i = 0
            while i < len(tablesdata.get(tablename)):
                for j in range(0,len(tablesdata.get(tablename)[i])):
                    sheet1.write(i+1,j,tablesdata.get(tablename)[i][j])
                i = i+1            
        f.save(self.excelpath)
        print('Save successfully')

        
class readExcel():
    def __init__(self,excelpath):
        self.excelpath = excelpath
        
    def readTable(self,tablename):
        data = xlrd.open_workbook(self.excelpath)
        table = data.sheet_by_name(tablename)
        nrows = table.nrows
        ncols = table.ncols
        header = table.row_values(0)
        tabledata = []
        i = 1
        while i < nrows:
            rdata = table.row_values(i)
            if rdata[0]:
                if isinstance(rdata[0],float):
                    rdata[0] = int(rdata[0])
                j = 0
                row = {}
                while j <len(header):                         
                    row.setdefault(header[j],rdata[j])
                    j = j+1   
                tabledata.append(row)
            i=i+1
        return tabledata
    
    def readTables(self,tablesname):
        data = xlrd.open_workbook(self.excelpath)
        tablesdata = {}
        for tablename in tablesname:
            table = data.sheet_by_name(tablename)
            nrows = table.nrows
            ncols = table.ncols
            header = table.row_values(0)
            tabledata = []
            i = 1
            while i < nrows:
                rdata = table.row_values(i)
                if rdata[0]:    
                    if isinstance(rdata[0],float):
                        rdata[0] = int(rdata[0])
                    j = 0
                    row = {}
                    while j <len(header):                
                        row.setdefault(header[j],rdata[j])
                        j = j+1           
                    tabledata.append(row)
                i=i+1
            tablesdata.setdefault(tablename,tabledata)
        return tablesdata

class sendAPI:
    def __init__(self,url,data,method='POST',contentType = 'json'):
        self.url =url
        self.data = data
        self.method = method
        self.contentType = contentType
        self.h = httplib2.Http(".cache")  
        
    def run(self):
        if self.method == 'POST' and self.contentType == 'json':
            successCount = 0
            failCount =0
            result = {}
            start = datetime.datetime.now()
            for i in self.data:
                encodedjson = json.dumps(i)   
                resp, content = self.h.request(self.url, self.method,encodedjson, headers={"Content-Type": "application/%s"%self.contentType} )  
                if resp.get('status')=='200':
                    successCount = successCount +1
                else:
                    failCount = failCount +1
                
            end = datetime.datetime.now()
            duration = end - start
            duration =  duration.seconds +duration.microseconds/1000000
            result.setdefault('duration',duration)
            result.setdefault('successCount',successCount)
            result.setdefault('failCount',failCount)
            print(result)
            return result
        else:
            print('no support')
 
                    
        


if __name__ == '__main__':
    
    userdata = [{"version_number":"115541","download_url":"34343434343"}]
    cc = sendAPI("http://127.0.0.1:5000/api/v1.0/version",userdata)
    cc.run()
#    cc.run()
#    a =oprMysql('69.164.202.55','test','test','test',3306,"utf8")

#    a.toExcel('D:/demo.xls')
    
#    b = readExcel('D:/demo.xls')


#    print(content)