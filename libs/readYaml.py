#!/usr/bin/env python
#coding:utf-8
'''
    元素属性保存在yaml文件中，此为读取yaml文件中数据
'''
import yaml
import os
class readYaml(object):
    def __init__(self,filename):
        B_DIR = os.path.dirname(os.path.dirname(__file__))
        F_dir = os.path.join(B_DIR+'\data',filename)
        #self.key = key
        try:
            self.f = open(F_dir)
        except Exception,e:
            print 'not open'
    def readYaml(self):
        self.x = yaml.load(self.f)
        #print self.x
        return self.x
    def readkey(self,key):
        return self.x[key].split(',')[0],self.x[key].split(',')[1]
if __name__ == '__main__':
    a = readYaml('TestDate.yaml')
    yamldata = a.readYaml()
    print yamldata['hao123'].split(',')[0]

