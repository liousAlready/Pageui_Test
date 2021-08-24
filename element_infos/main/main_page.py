# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:07 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_page.py
# @Software: PyCharm

import os
from common.element_data_utils_02 import ElementDataUtils
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config


# from action.login_action import LoginAction


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils("main", "main_page").get_element_infos()

        # elements = ElementDataUtils('main').get_element_data('main_page')
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        self.wait(2)
        return value

    def click_username(self):
        self.click(self.user_menu)

    def click_quit_button(self):
        self.click(self.quit_button)


if __name__ == "__main__":
    driver = Browser().get_driver()
    # driver.get(local_config.get_url)
    # main = LoginAction(driver).login_default()
    # value = main.get_username()
    # print(value)
