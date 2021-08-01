# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 10:26 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : logger_demo.py
# @Software: PyCharm


import os
import logging

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../logs/test.log')

logger = logging.getLogger(__name__)  # 创建一个日志对象
logger.setLevel(level=logging.INFO)  # 设置日志级别

# 文件输入
file_log = logging.FileHandler(log_path)  # file_log对象
formatter = logging.Formatter('file:%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
file_log.setFormatter(formatter)
logger.addHandler(file_log)

logger.info('Hello word!!!')  # 替换之前的print()
logger.error('Hello word!!!')

print('UI自动化框架')
