# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:25 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : config_utils.py
# @Software: PyCharm
import configparser
import os

current = os.path.dirname(__file__)
config_path = os.path.join(current, '../config/config.ini')


class ConfigUtils:

    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding="utf-8")

    @property
    def get_url(self):
        url = self.cfg.get("default", "LOGIN_URL")
        return url

    @property
    def get_driver_path(self):
        url = self.cfg.get("driver_path", "DRIVER_PATH")
        return url

    @property
    def get_logs_path(self):
        logs_path = self.cfg.get("logs", "LOGS_PATH")
        return logs_path

    @property
    def default_driver(self):
        default_driver = self.cfg.get("driver", "DEFAULT_DRIVER")
        return default_driver


local_config = ConfigUtils()

if __name__ == "__main__":
    print(local_config.get_url)
    print(local_config.get_driver_path)
    print(local_config.default_driver)
