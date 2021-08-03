# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:38 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : browser.py
# @Software: PyCharm

import os
import sys
from selenium import webdriver
from common.config_utils import local_config
from selenium.webdriver.chrome.options import Options
from common.log_utils import logger

# 浏览器类，用来提供driver驱动

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, "..", local_config.get_driver_path)


class Browser:
    system_driver = sys.platform

    def __init__(self, path=driver_path):
        self.driver_path = path
        self.driver_name = local_config.default_driver
        self.driver_system = Browser.system_driver

    def get_driver(self):
        if self.driver_name.lower() == "chrome":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_chrome_driver()
        elif self.driver_name.lower() == 'firefox':
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_firefox_driver()
        elif self.driver_name.lower() == "edge":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        """去除谷歌浏览器控制白条"""
        if self.driver_system.lower() == "darwin":
            chrome_options = Options()
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
            chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
            chrome_driver_path = os.path.join(self.driver_path, 'chromedriver')
            driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
            logger.info('初始化Google浏览器并启动')
            return driver
        else:
            chrome_options = Options()
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
            chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
            chrome_driver_path = os.path.join(self.driver_path, 'chromedriver.exe')
            driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
            logger.info('初始化Google浏览器并启动')
            return driver

    def __get_firefox_driver(self):
        if self.driver_system.lower() == "darwin":
            firefox_driver_path = os.path.join(self.driver_path, 'geckodriver')
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            logger.info('初始化Firefox浏览器并启动')
            return driver
        else:
            firefox_driver_path = os.path.join(self.driver_path, 'geckodriver.exe')
            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            logger.info('初始化Firefox浏览器并启动')
            return driver

    def __get_edge_driver(self):
        edge_driver_path = os.path.join(self.driver_path, 'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        logger.info('初始化Edge浏览器并启动')
        return driver

    def __get_remove_to_driver(self):  # selenium支持分布式 grid ==》配置（你自己的代码编写、对方电脑的配置）
        pass


if __name__ == "__main__":
    Browser().get_driver()
