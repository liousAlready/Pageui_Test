# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : base_page.py
# @Software: PyCharm

import time
import os
from selenium import webdriver
from common import HTMLTestReportCN
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.config_utils import local_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''所有页面的父类,提取所有页面的公共操作，做成BasePage'''


# 启动浏览器之后，将driver传给Base_page
class BasePage:

    def __init__(self, driver):
        self.driver = driver  # driver

    def open_url(self, url):
        self.driver.get(url)
        logger.info("打开url：%s" % url)

    def close_browser(self):
        self.driver.close()
        logger.info("关闭当前tab页签")

    def exit_driver(self):
        self.driver.quit()
        logger.info("退出浏览器")

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

    def get_text(self, element_info):
        element = self.find_element(element_info)
        logger.info("获取文本信息：%s" % element)
        return element.text

    def back_up(self):
        self.driver.back()
        logger.info("返回上一页...")

    def forward(self):
        self.driver.forward()
        logger.info("前进一页...")

    # 　封装时间
    def wait(self, seconds=local_config.time_out):
        """
        固定等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        time.sleep(seconds)
        logger.info("休息一会儿 %s 秒钟~" % seconds)

    def implicitly_wait(self, seconds=local_config.time_out):
        """
        隐式等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待个 %s 秒" % seconds)

    def find_element(self, element_info):
        """
        通过分离处理的元素识别字典信息，返回一个元素

        :param element_info: 元素信息，字典类型{}
        :return: element对象
        """
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
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        return element

    #  元素操作

    #  封装输入参数
    def input(self, element_info, inputs):
        """
        :param element_info: 元素信息，字典类型{}
        :param inputs: 输入参数
        """
        element = self.find_element(element_info)
        element.send_keys(inputs)
        logger.info("输入框输入内容：%s , 识别输入框：%s" % (inputs, element_info["locator_value"]))

    #  封装点击方法
    def click(self, element_info):
        """
        :param element_info: 元素信息，字典类型{}
        """
        element = self.find_element(element_info)
        element.click()
        logger.info("识别元素进行点击操作：%s" % element_info["locator_value"])

    # selenium 执行js
    def __execute_script(self, js_str, element_info=None):
        """
        :param js_str: selenium_js 的执行语句  ex: arguments[0].removeAttribute("%s");
        :param element_info: 元素信息，字典类型{}
        """
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    def delete_element_attribute1(self, element_info, attribute_name):
        """移除元素属性-001"""
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def delete_element_attribute(self, element_info, attribute_name):
        """
        :param element_info: 元素信息，字典类型{}
        :param attribute_name: 需要移除的元素
        """
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        """
        :param element_info: 元素信息，字典类型{}
        :param attribute_name: 需要设置的元素
        :param attribute_value: 最终修改的值
        :return:
        """
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value), element)

    # 　弹出窗封装
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        """
        :param action: 默认点击确定操作
        :param time_out: 超时时间
        """
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return alter_text

    #  句柄封装
    def get_window_handle(self):
        """获取句柄"""
        return self.driver.window_handles

    def switch_to_window_by_handle(self, window_handle):
        """
        :param window_handle: 切换到某个句柄
        :return:
        """
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self, title):
        """
        :param title: 根据title切换
        :return:
        """
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_window_by_url(self, url):
        """
        :param url: 根据url切换
        """
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    # def screenshot_as_file(self):
    #     report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', local_config.report_path)
    #     report_dir = HTMLTestReportCN.ReportDirectory(report_path)
    #     report_dir.get_screenshot(self.driver)
    #     print(report_dir)

    def screenshot_as_file(self, *screenshot_path):
        """
        :param screenshot_path:  *screenshot_path 元祖类型不定长参数，不带参数为0 默认存放在当前路径
        """
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir, '..', screenshot_filepath, 'UI_Test_%s.png' % now)
        print(screenshot_filepath)
        self.driver.get_screenshot_as_file(screenshot_filepath)

    # 跳转框架 1.iframe ==> id/name跳转  2.frame元素对象
    # 思路一
    def switch_to_iframe(self, element_info):
        self.wait()
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info("现在跳转框架：%s" % element_info["locator_value"])

    # 思路二
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self, element_info):
        self.wait()
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路三
    def switch_to_iframe_new(self, **element_dict):
        # ＊＊代表字典  switch_to_iframe_01(id=iframe_id)
        # element = (element_info)
        self.wait(3)
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)

    # 鼠标键盘封装( 判断操作系统类型)
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

    def move_mouse_double_click(self, element_info):
        """双击元素"""
        target = self.find_element(element_info)
        ActionChains(self.driver).double_click(target).perform()
        logger.info("双击元素：%s" % element_info['locator_value'])

    def move_to_mouse_element(self, element_info):
        """鼠标悬停"""
        target = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(target).perform()
        logger.info("鼠标当前悬停在：%s" % element_info['locator_value'])

    def long_press_element(self, element_info, second):
        """长按元素--按住多久然后释放"""
        target = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(target).pause(second)

    # 键盘操作
    def keyboard_tab(self, element_info):
        """点击tab键"""
        element = self.find_element(element_info)
        element.send_keys(Keys.TAB)
        logger.info("点击tab：%s" % element_info['locator_value'])

    def keyboard_delete(self, element_info):
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


if __name__ == "__main__":
    driver = webdriver.Chrome()
    # 带参数
    # BasePage(driver).screenshot_as_file('config')
    # 不带参数
    BasePage(driver).screenshot_as_file()
