# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:05 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : login_page.py
# @Software: PyCharm

import os
import time
from common.log_utils import logger
from common.base_page import *
# from common.element_data_utils import ElementDataUtils
from common.element_data_utils_02 import ElementDataUtils
from common.browser import *
from common.base_page import *


#  页面是类  控件：属性 控件操作：方法

class LoginPage(BasePage):  # 继承页面类

    def __init__(self, driver):
        super().__init__(driver)

        # elements = ElementDataUtils("login").get_element_data("login_page")
        elements = ElementDataUtils("login", "login_page").get_element_info()

        self.username_input_box = elements["username_inputbox"]
        self.password_input_box = elements["password_inputbox"]
        self.submit = elements["login_button"]

    def input_username(self, username):  # 方法 --》 控件的操作
        self.wait(1)
        logger.info("输入账号: %s" % username)
        self.input(self.username_input_box, username)

    def input_password(self, password):
        logger.info("输入密码: %s" % password)
        self.input(self.password_input_box, password)

    def click_login(self):
        logger.info("点击登录按钮")
        self.click(self.submit)

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()


if __name__ == "__main__":
    # 页面= 属性+方法
    # 属性命名 = 名字+类型
    # 操作命名 = 操作+元素对象

    driver = Browser().get_driver()
    login_page = LoginPage(driver)

    login_page.open_url(local_config.get_url)
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.wait(2)
    login_page.screenshot_as_file()
    login_page.wait(2)
    driver.quit()
