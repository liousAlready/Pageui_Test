# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 10:32 δΈε
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo.py
# @Software: PyCharm

import sys
import platform

from selenium import webdriver

print(sys.platform)

# macOS ηζ― darwin


print(platform.system())

driver = webdriver.Chrome()

text = driver.page_source
