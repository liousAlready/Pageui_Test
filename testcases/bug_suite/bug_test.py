# -*- coding: utf-8 -*-
# @Time : 2021/8/20 13:45
# @Author : Limusen
# @File : bug_test

import unittest
from action.bug_action import BugAction
from common.selenium_base_case import SeleniumBaseCase
from action.login_action import LoginAction
from common.test_data_utils import TestDataUtils


class BugTest(SeleniumBaseCase):
    test_class_data = TestDataUtils("bug_suite", "bug_test").convert_excel_data_test_data()

    def test_A004_commit_bug(self):
        test_data = self.test_class_data['test_commit_bug']
        self._testMethodDoc = test_data['test_name']

        login = LoginAction(self.base_page.driver)
        main_page = login.login_default()
        bug = BugAction(main_page.driver)
        result = bug.commit_bug(test_data['test_parameter'].get('title'), test_data['test_parameter'].get('content'))
        self.assertIn(test_data['test_parameter'].get('title'), result, "test_commit_bug--失败")

    # def test_A002_login_fail(self):
    #     test_data = self.test_class_data['test_login_fail']
    #     self._testMethodDoc = test_data['test_name']
    #     login_action = LoginAction(self.base_page.driver)
    #     actual_result = login_action.login_fail(test_data['test_parameter'].get('username'),
    #                                             test_data['test_parameter'].get('password'))
    #     self.assertEqual(actual_result, test_data['excepted_result'], 'test_login_fail,执行失败')


if __name__ == "__main__":
    unittest.main()
