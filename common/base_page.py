# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : base_page.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.ui import WebDriverWait

'''所有页面的父类,提取所有页面的公共操作，做成BasePage'''


# 启动浏览器之后，将driver传给Base_page
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        logger.info("打开url：%s" % url)

    def set_window_max(self):
        self.driver.maximize_window()
        logger.info("浏览器最大化...")

    def page_refresh(self):
        self.driver.refresh()
        logger.info("浏览器刷新...")

    def get_title(self):
        value = self.driver.title
        logger.info("获取标题：%s" % value)
        return value

    #  元素识别 通过分离处理的元素识别字典信息，返回一个元素
    # self.username_input_box = self.driver.find_element(By.XPATH, '//*[@name="account"]')
    def find_element(self, element_infos):
        '''
        :param element_infos:
        :return:
            username_input_box = {"element_name": "用户名输入框",
                                       "locator_type": "xpath",
                                       "locator_value": '//*[@name="account"]',
                                       "timeout": 5}
        '''
        locator_type = element_infos["locator_type"]
        locator_value = element_infos["locator_value"]
        locator_timeout = element_infos["timeout"]

        if locator_type == "name":
            locator_type = By.NAME
        elif locator_type == "css":
            locator_type = By.CSS_SELECTOR
        elif locator_type == "xpath":
            locator_type = By.XPATH
        elif locator_type == "id":
            locator_type = By.ID
        elif locator_type == "class_name":
            locator_type = By.CLASS_NAME
        elif locator_type == "link_test":
            locator_type = By.LINK_TEXT
        elif locator_type == "partial_link":
            locator_type = By.PARTIAL_LINK_TEXT
        element = WebDriverWait(self.driver, timeout=locator_timeout).until(
            lambda x: x.find_element(locator_type, locator_value))
        logger.info("元素识别成功：%s" % element_infos["locator_value"])
        return element

    #  元素操作

    #  封装输入参数
    def input(self, element_infos, inputs):
        element = self.find_element(element_infos)
        element.send_keys(inputs)
        logger.info("输入框输入内容：%s , 识别输入框：%s" % (inputs, element_infos["locator_value"]))

    #  封装点击方法
    def click(self, element_infos):
        element = self.find_element(element_infos)
        element.click()
        logger.info("识别元素进行点击操作：%s" % element_infos["locator_value"])

