# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:05 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : login_page.py
# @Software: PyCharm

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import *


#  页面是类  控件：属性 控件操作：方法

class LoginPage(BasePage):  # 继承页面类

    def __init__(self, driver):
        # 驱动的处理
        # 1.继承父类  子类构造方法需要显示调用父类的构造
        super().__init__(driver)
        # # 2.父类方法.构造方法(self,driver)
        # BasePage.__init__(self, driver)

        self.username_input_box = {"element_name": "用户名输入框",
                                   "locator_type": "xpath",
                                   "locator_value": '//*[@name="account"]',
                                   "timeout": 5}
        self.password_input_box = {"element_name": "密码输入框",
                                   "locator_type": "xpath",
                                   "locator_value": '//*[@name="password"]',
                                   "timeout": 5}
        self.submit = {"element_name": "登录按钮",
                       "locator_type": "xpath",
                       "locator_value": '//*[@id="submit"]',
                       "timeout": 5}

    def input_username(self, username):  # 方法 --》 控件的操作
        logger.info("输入账号: %s" % username)
        self.input(self.username_input_box, username)

    def input_password(self, password):
        logger.info("输入密码: %s" % password)
        self.input(self.password_input_box, password)

    def click_login(self):
        self.click(self.submit)
        logger.info("点击登录按钮")


if __name__ == "__main__":
    # 页面= 属性+方法
    # 属性命名 = 名字+类型
    # 操作命名 = 操作+元素对象
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url(
        "http://47.107.178.45/zentao/www/index.php?m=user&f=login&referer=L3plbnRhby93d3cvaW5kZXgucGhwP209dXNlciZmPWxvZ2lueg==")
    login_page.set_window_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    driver.quit()
