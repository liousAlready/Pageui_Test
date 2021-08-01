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

#  页面是类  控件：属性 控件操作：方法
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver')


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(
            "http://47.107.178.45/zentao/www/index.php?m=user&f=login&referer=L3plbnRhby93d3cvaW5kZXgucGhwP209dXNlciZmPWxvZ2lueg=="
        )
        logger.info("打开网站")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.username_input_box = self.driver.find_element(By.XPATH, '//*[@name="account"]')  # 属性--》 控件
        self.password_input_box = self.driver.find_element(By.XPATH, '//*[@name="password"]')
        self.keep_password = self.driver.find_element(By.XPATH, '//*[@name="keepLogin[]"]')
        self.submit = self.driver.find_element(By.XPATH, '//*[@id="submit"]')

    def input_username(self, username):  # 方法 --》 控件的操作
        logger.info("输入账号: %s" % username)
        self.username_input_box.send_keys(username)

    def input_password(self, password):
        logger.info("输入密码: %s" % password)
        self.password_input_box.send_keys(password)

    def click_login(self):
        self.submit.click()
        logger.info("点击登录按钮")


if __name__ == "__main__":
    # 页面= 属性+方法
    # 属性命名 = 名字+类型
    # 操作命名 = 操作+元素对象

    login = LoginPage()  # 创建页面对象
    login.input_username("test02")
    login.input_password('newdream123')
    login.click_login()
