#!coding=utf-8
'''
Created on 2016年6月21日

@author: lx-lang.qinyue
'''
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

from xml.dom import minidom
import os
class xmlUtils():
    
    @staticmethod
    def readXml(propertyID,fileName='element.xml'):
        try:
            by = ""
            content = ""

            
            doc2 = minidom.parse(r"../data/element.xml")
            B_DIR = os.path.dirname(os.path.dirname(__file__))
            F_dir = os.path.join(B_DIR+'\data',fileName)
            doc1 = minidom.parse(F_dir)
            root1 = doc2.documentElement
            nodes1 = root1.getElementsByTagName("element")
            for n in nodes1:
                if propertyID==n.getAttribute("id"):
                    by=n.getAttribute("by")
                    content=n.getAttribute("content") 
        except Exception,e:
            errmsg = e.args[0]
            code = -1    
            print "errcode=" + str(code)+";"+"errmsg=" + str(errmsg)+";"        
        return by, content
        
if __name__ == '__main__':
    p = xmlUtils()
    a,b = p.readXml('登录链接','element.xml')
    print a,b
            