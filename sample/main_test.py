# -*- coding: utf-8 -*-
# @Time : 2021/8/3 11:40
# @Author : Limusen
# @File : main_test


import os
from common.element_data_utils import ElementDataUtils
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config
from action.login_action import LoginAction

driver = Browser().get_driver()
driver.get(local_config.get_url)
main = LoginAction(driver).login_default()
value = main.get_username()
print(value)
