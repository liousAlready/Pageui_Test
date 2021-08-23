# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 3:58 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : element_data_utils.py
# @Software: PyCharm

import os
from common.config_utils import local_config
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xls')


class ElementDataUtils(ExcelUtils):
    """

    封装实现业务的读取类

    """

    def __init__(self, module_name, path=excel_path):
        super(ElementDataUtils, self).__init__(module_name, path)

    # 读取excel单张表 多行多列
    def get_element_data(self, page_name):
        element_info_dict = {}
        for number in range(1, self.excel_rows()):
            if self.excel_read(number, 2) == page_name:
                element_info = {}
                element_info['element_name'] = self.excel_read(number, 1)
                element_info['locator_type'] = self.excel_read(number, 3)
                element_info['locator_value'] = self.excel_read(number, 4)
                time_out_value = self.excel_read(number, 5)
                element_info['timeout'] = time_out_value if isinstance(time_out_value,
                                                                       float) else local_config.time_out
                element_info_dict[self.excel_read(number, 0)] = element_info

        return element_info_dict


if __name__ == "__main__":
    info = ElementDataUtils("login").get_element_data("login_page")
    # print(info)
    for e in info.values():
        print(e)
