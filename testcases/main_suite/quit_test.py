# -*- coding: utf-8 -*-
# @Time : 2021/8/3 14:49
# @Author : Limusen
# @File : quit_test

import unittest
from action.login_action import LoginAction
from action.quit_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class QuitTest(SeleniumBaseCase):
    test_class_data = TestDataUtils("main_suite", "main_test").convert_excel_data_test_data()

    def test_A003_quit_success(self):
        test_data = self.test_class_data['test_quit_success']
        self._testMethodDoc = test_data['test_name']

        login_action = LoginAction(self.base_page.driver)
        # 　需要继承上一个页面的driver 不然识别不到驱动会报错
        main_page = login_action.login_default()
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        # self.assertEqual(actual_result.__contains__("用户登录"), True, "test_quit_success_不通过")
        self.assertEqual(actual_result, test_data['excepted_result'], "test_quit_success_不通过")


if __name__ == "__main__":
    unittest.main()
