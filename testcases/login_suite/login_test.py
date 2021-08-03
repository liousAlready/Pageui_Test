# -*- coding: utf-8 -*-
# @Time : 2021/8/3 10:26
# @Author : Limusen
# @File : login_test

import unittest
from action.login_action import LoginAction
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_window_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.get_url)

    def tearDown(self) -> None:
        self.base_page.wait(2)
        self.base_page.exit_driver()

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('test01', 'newdream123')
        # actual_result = main_page.get_username()
        self.assertEqual(main_page.get_username(), '测试人员1', 'test_login_success,执行失败')


if __name__ == "__main__":
    unittest.main()
