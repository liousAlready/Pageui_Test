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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def get_text(self):
        value = self.driver.text()
        logger.info("获取文本信息：%s" % value)
        return value

    def back_up(self):
        self.driver.back()
        logger.info("返回上一页...")

    def forward(self):
        self.driver.forward()
        logger.info("前进一页...")

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
        elif locator_type == "class":
            locator_type = By.CLASS_NAME
        elif locator_type == "linktext":
            locator_type = By.LINK_TEXT
        elif locator_type == "partiallink":
            locator_type = By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            locator_type = By.TAG_NAME
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

    # 跳转框架
    def iframe_switch_to(self, element_infos):
        iframe = self.find_element(element_infos)
        self.driver.switch_to.frame(iframe)
        logger.info("现在跳转框架：%s" % element_infos["locator_value"])

    # 移动鼠标操作
    def move_mouse_right_click(self, element_infos):
        """右击鼠标"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).context_click(target).perform()
        logger.info("右击元素：%s" % element_infos['locator_value'])

    def move_mouse_left_click(self, element_infos):
        """左击鼠标"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).click_and_hold(target).perform()
        logger.info("左击元素：%s" % element_infos['locator_value'])

    def mova_mouse_double_click(self, element_infos):
        """双击元素"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).double_click(target).perform()
        logger.info("双击元素：%s" % element_infos['locator_value'])

    def move_mouse_to_element(self, element_infos):
        """鼠标悬停"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).move_to_element(target).perform()
        logger.info("鼠标当前悬停在：%s" % element_infos['locator_value'])

    # 键盘操作
    def keyboard_tab(self, element_infos):
        """点击tab键"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.TAB)
        logger.info("点击tab：%s" % element_infos['locator_value'])

    def keyboard_delte(self, element_infos):
        """删除键"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.BACK_SPACE)
        logger.info("删除内容：%s" % element_infos['locator_value'])

    def keyboard_all(self, element_infos):
        """全选"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.COMMAND, 'a')
        logger.info("全选内容：%s" % element_infos['locator_value'])

    def keyboard_copy(self, element_infos):
        """复制内容"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.COMMAND, 'c')
        logger.info("复制内容：%s" % element_infos['locator_value'])

    def keyboard_paste(self, element_infos):
        """粘贴内容"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.COMMAND, 'v')
        logger.info("粘贴内容：%s" % element_infos['locator_value'])

    def keyboard_cut(self, element_infos):
        """剪切内容"""
        element = self.find_element(element_infos)
        element.send_keys(Keys.COMMAND, 'x')
        logger.info("剪切内容：%s" % element_infos['locator_value'])
