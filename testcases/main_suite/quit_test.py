# -*- coding: utf-8 -*-
# @Time : 2021/8/3 14:49
# @Author : Limusen
# @File : quit_test

import time
import unittest
from action.login_action import LoginAction
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from action.quit_action import QuitAction


class QuitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_window_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.get_url)

    def tearDown(self) -> None:
        self.base_page.wait(2)
        self.base_page.exit_driver()

    def test_quit_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_default()
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__("用户登录"), True, "test_quit_success_不通过")



if __name__ == "__main__":
    unittest.main()
