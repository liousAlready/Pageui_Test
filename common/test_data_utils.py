# -*- coding: utf-8 -*-
# @Time : 2021/8/10 10:33
# @Author : Limusen
# @File : test_data_utils


import os
from common.config_utils import local_config
from common.element_data_utils import ExcelUtils

current = os.path.dirname(__file__)
test_data_path = os.path.join(current, '..', local_config.test_datas_path)


class TestDataUtils:

    def __init__(self, test_suite_name, test_class_name):
        self.test_class_name = test_class_name
        self.excel_data = ExcelUtils(test_suite_name, test_data_path).get_sheet_data_by_list()
        self.testsuite_counts = len(self.excel_data) - 1  # 行首不要
        self.excel_rows = len(self.excel_data)

    def convert_excel_data_test_data(self):
        test_data_infos = {}
        for row in range(1, self.excel_rows):
            test_data_info = {}
            test_data_infos["test_name"] = self.excel_data[row][1]
