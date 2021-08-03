# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 10:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : log_utils.py
# @Software: PyCharm

import time
import logging
import os
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '..', local_config.log_path)


class LogUtil(object):
    def __init__(self, logger=None):
        """
        :param logger:  日志对象
        """
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(logger)  # 日志对象
        self.logger.setLevel(local_config.log_level)  # 日志级别

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 输出到文件
        self.fh.setLevel(local_config.log_level)
        self.ch = logging.StreamHandler()  # 输出到控制台
        self.ch.setLevel(local_config.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger


logger = LogUtil().get_log()

if __name__ == '__main__':
    logger.info('newdream')
