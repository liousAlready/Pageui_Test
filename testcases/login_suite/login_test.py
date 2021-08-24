# -*- coding: utf-8 -*-
# @Time : 2021/8/3 10:26
# @Author : Limusen
# @File : login_test

import unittest
from action.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    """
    继承 SeleniumBaseCase
    三层继承关系 LoginTest --> SeleniumBaseCase --> unittest.TestCase
    """

    test_class_data = TestDataUtils("login_suite", "login_test").convert_excel_data_test_data()

    def setUp(self) -> None:
        """
        自定义内容需要先调取父类的setup才能够自定义
        """
        super().setUp()
        # self.test_class_data = TestDataUtils("login_suite", "LoginTest").convert_excel_data_test_data()

    @unittest.skipIf(test_class_data['test_login_success']['is_not'], '')
    def test_A001_login_success(self):
        test_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_data['test_name']

        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_data['test_parameter'].get('username'),
                                               test_data['test_parameter'].get('password'))
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, test_data['excepted_result'], 'test_login_success,执行失败')

    def test_A002_login_fail(self):
        test_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_data['test_parameter'].get('username'),
                                                test_data['test_parameter'].get('password'))
        self.assertEqual(actual_result, test_data['excepted_result'], 'test_login_fail,执行失败')


if __name__ == "__main__":
    unittest.main()
