# -*- coding: utf-8 -*-
# @Time : 2021/8/3 10:26
# @Author : Limusen
# @File : login_test

import unittest
from action.login_action import LoginAction
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase


class LoginTest(SeleniumBaseCase):
    """
    继承 SeleniumBaseCase
    三层继承关系 LoginTest --> SeleniumBaseCase --> unittest.TestCase
    """

    def setUp(self) -> None:
        """
        自定义内容需要先调取父类的setup才能够自定义
        """
        super().setUp()
        print("---hello---")

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('test01', 'newdream123')
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, '测试人员1', 'test_login_success,执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('test01', 'newdream')
        # print("actual_result: %s" % actual_result)
        self.assertEqual(actual_result, "登录失败，请检查您的用户名或密码是否填写正确。")


if __name__ == "__main__":
    unittest.main()
