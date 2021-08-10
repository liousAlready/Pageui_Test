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

    # 读取excel单张表 多行多列
    def get_sheet_data_by_list(self):
        all_excel_data = []
        for row_num in range(self.excel_rows()):
            row_excel_data = []
            for col_num in range(self.excel_column()):
                cell_value = self.excel_read(row_num, col_num)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data


if __name__ == "__main__":
    # ex：qwe是sheet页面名称  后面接的是文件名称 如果不传内容则默认打印新页面
    # ExcelUtils("qwe", "../element_info_datas/logins.xlsx").excel_create("测试")

    current = os.path.dirname(__file__)
    dir_path = os.path.join(current, '..', local_config.test_datas_path)
    sheet_infos = ExcelUtils('login_suite', dir_path).get_sheet_data_by_list()
    print(sheet_infos[1][1])
