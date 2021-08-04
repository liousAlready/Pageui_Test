# -*- coding: utf-8 -*-
# @Time : 2021/8/4 10:39
# @Author : Limusen
# @File : keyboard_demo


import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from common.base_page import BasePage

system = sys.platform

print(system)

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("杀不死建档立卡就离开自行车")