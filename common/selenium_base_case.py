# -*- coding: utf-8 -*-
# @Time : 2021/8/3 16:06
# @Author : Limusen
# @File : selenium_base_case


import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config


class SeleniumBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.get_url

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_window_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        self.base_page.wait(2)
        self.base_page.exit_driver()
        # 测试用例失败截图
