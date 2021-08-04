# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 9:26 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : excel_utils.py
# @Software: PyCharm


import os
import xlrd
import xlwt
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
excel_file_path = os.path.join(current_path, '..', local_config.test_data_path, r'element_info_datas.xls')


class ExcelUtils:
    """
    单独封装xlrd读取excel表格的工具类
    """

    def __init__(self, sheet_name, filename=excel_file_path):
        self.filename = filename
        self.sheet_name = sheet_name

    # 获取excel总行数
    def excel_rows(self):
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheet_name)
        return table.nrows

    # 获取excel总列数
    def excel_column(self):
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheet_name)
        return table.ncols

    # 读取excel 单行单列
    def excel_read(self, row, column):
        """
        :param row: 行
        :param column: 列
        :return:
        """
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheet_name)
        return table.cell_value(row, column)

    # 判断excel文件是否存在，不存在则创建，存在则直接打开编辑
    def excel_create(self, new_name="新页面"):
        """
        :param new_name: 首行首列展示的内容
        :return:
        """
        if not os.path.exists(self.filename):
            data = xlwt.Workbook()
            table = data.add_sheet(self.sheet_name)
            table.write(0, 0, new_name)
            data.save(self.filename)

    # # 读取excel单张表 多行多列
    # def get_element_data(self, page_name):
    #     element_info_dict = {}
    #     for number in range(1, self.excel_rows()):
    #         if self.excel_read(number, 2) == page_name:
    #             element_info = {}
    #             element_info['element_name'] = self.excel_read(number, 1)
    #             element_info['locator_type'] = self.excel_read(number, 3)
    #             element_info['locator_value'] = self.excel_read(number, 4)
    #             time_out_value = self.excel_read(number, 5)
    #             element_info['timeout'] = time_out_value if isinstance(time_out_value,
    #                                                                    float) else local_config.time_out
    #             element_info_dict[self.excel_read(number, 0)] = element_info
    #
    #     return element_info_dict


if __name__ == "__main__":
    # ex：qwe是sheet页面名称  后面接的是文件名称 如果不传内容则默认打印新页面
    ExcelUtils("qwe", "../element_info_datas/logins.xlsx").excel_create("测试")
