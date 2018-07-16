#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from huakuaii import BaseGeetestCrack
from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class IndustryAndCommerceGeetestCrack(BaseGeetestCrack):

    u"""工商滑动验证码破解类"""

    def __init__(self, driver):
        super(IndustryAndCommerceGeetestCrack, self).__init__(driver)

    def crack(self):
        """执行破解程序
        """
        self.input_by_id()
        self.click_by_id()
        time.sleep(2)
        x_offset = self.calculate_slider_offset()
        print 'x_pff'
        print x_offset
        self.drag_and_drop(x_offset=x_offset)


def main():
    driver = webdriver.Chrome(executable_path=r"D:\Program Files\Chrome\chromedriver.exe")
    driver.get("http://bj.gsxt.gov.cn/sydq/loginSydqAction!sydq.dhtml")
    cracker = IndustryAndCommerceGeetestCrack(driver)
    cracker.crack()
    print(driver.get_window_size())
    time.sleep(3)
    driver.save_screenshot("screen.png")
    driver.close()


if __name__ == "__main__":
    #main()
    s = 'dsfsdfds'
    d = s+'|jordan'
    print d