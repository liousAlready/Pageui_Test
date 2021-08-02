# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:07 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_page.py
# @Software: PyCharm


from selenium.webdriver.common.by import By
from element_infos.login.login_page import LoginPage
from common.log_utils import logger


class MainPage:

    def __init__(self):
        login = LoginPage()
        login.input_username("test02")
        login.input_password('newdream123')
        login.click_login()
        self.driver = login.driver  # 把login的driver转移到main
        self.company_name_show = self.driver.find_element(By.XPATH, '//*[@id="companyname"]')
        self.my_zone_show = self.driver.find_element(By.XPATH,
                                                     '//*[@class="active"]/*[@href="/zentao/www/index.php?m=my&f=index"]')
        self.my_product = self.driver.find_element(By.XPATH,
                                                   '//*[@data-id="product"]/*[@href="/zentao/www/index.php?m=product&f=index&locate=no"]')
        self.username_show_box = self.driver.find_element(By.XPATH, '//*[@class="user-name"]')

    def get_companyname(self):
        """获取公司名称"""
        value = self.company_name_show.get_attribute("title")
        logger.info("获取公司名称：%s" % value)
        return value

    def goto_myzone(self):
        """选择我的地盘"""
        self.my_zone_show.click()
        logger.info("点击我的地盘")

    def goto_myproduct(self):
        """点击我的产品"""
        self.my_product.click()
        logger.info("点击我的产品")

    def get_username(self):
        """获取用户名"""
        value = self.username_show_box.text
        logger.info("获取用户名称：%s" % value)
        return value


if __name__ == "__main__":
    main = MainPage()
    username = main.get_username()
    companyname = main.get_companyname()
