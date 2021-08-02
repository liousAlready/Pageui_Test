# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : base_page.py
# @Software: PyCharm

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
    def find_element(self, element_info):
        locator_type = element_info["locator_type"]
        locator_value = element_info["locator_value"]
        locator_timeout = element_info["timeout"]

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
        element = WebDriverWait(self.driver, locator_timeout).until(
            lambda x: x.find_element(locator_type, locator_value))
        logger.info("元素识别成功：%s" % element_info["locator_value"])
        return element

    #  元素操作

    #  封装输入参数
    def input(self, element_info, inputs):
        element = self.find_element(element_info)
        element.send_keys(inputs)
        logger.info("输入框输入内容：%s , 识别输入框：%s" % (inputs, element_info["locator_value"]))

    #  封装点击方法
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info("识别元素进行点击操作：%s" % element_info["locator_value"])

    # selenium 执行js
    def __execute_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    def delete_element_attribute1(self, element_info, attribute_name):
        """移除元素属性-001"""
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def delete_element_attribute(self, element_info, attribute_name):
        """移除元素属性"""
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        """修改元素属性"""
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value), element)

    # 跳转框架 1.iframe ==> id/name跳转  2.frame元素对象
    # 思路一
    def switch_to_iframe(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info("现在跳转框架：%s" % element_info["locator_value"])

    # 思路二
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路三
    def switch_to_iframe1(self, **element_dict):
        # ＊＊代表字典  switch_to_iframe_01(id=iframe_id)
        # element = (element_info)
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)

    # 移动鼠标操作
    def move_mouse_right_click(self, element_info):
        """右击鼠标"""
        target = self.find_element(element_info)
        ActionChains(self.driver).context_click(target).perform()
        logger.info("右击元素：%s" % element_info['locator_value'])

    def move_mouse_left_click(self, element_info):
        """左击鼠标"""
        target = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(target).perform()
        logger.info("左击元素：%s" % element_info['locator_value'])

    def mova_mouse_double_click(self, element_info):
        """双击元素"""
        target = self.find_element(element_info)
        ActionChains(self.driver).double_click(target).perform()
        logger.info("双击元素：%s" % element_info['locator_value'])

    def move_mouse_to_element(self, element_info):
        """鼠标悬停"""
        target = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(target).perform()
        logger.info("鼠标当前悬停在：%s" % element_info['locator_value'])

    # 键盘操作
    def keyboard_tab(self, element_info):
        """点击tab键"""
        element = self.find_element(element_info)
        element.send_keys(Keys.TAB)
        logger.info("点击tab：%s" % element_info['locator_value'])

    def keyboard_delte(self, element_info):
        """删除键"""
        element = self.find_element(element_info)
        element.send_keys(Keys.BACK_SPACE)
        logger.info("删除内容：%s" % element_info['locator_value'])

    def keyboard_all(self, element_info):
        """全选"""
        element = self.find_element(element_info)
        element.send_keys(Keys.COMMAND, 'a')
        logger.info("全选内容：%s" % element_info['locator_value'])

    def keyboard_copy(self, element_info):
        """复制内容"""
        element = self.find_element(element_info)
        element.send_keys(Keys.COMMAND, 'c')
        logger.info("复制内容：%s" % element_info['locator_value'])

    def keyboard_paste(self, element_info):
        """粘贴内容"""
        element = self.find_element(element_info)
        element.send_keys(Keys.COMMAND, 'v')
        logger.info("粘贴内容：%s" % element_info['locator_value'])

    def keyboard_cut(self, element_info):
        """剪切内容"""
        element = self.find_element(element_info)
        element.send_keys(Keys.COMMAND, 'x')
        logger.info("剪切内容：%s" % element_info['locator_value'])
