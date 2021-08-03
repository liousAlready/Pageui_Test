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

    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding="utf-8")

    @property
    def get_url(self):
        url = self.cfg.get("DEFAULT", "LOGIN_URL")
        return url

    @property
    def get_driver_path(self):
        url = self.cfg.get("DRIVER_PATH", "DRIVER_PATH")
        return url

    @property
    def get_logs_path(self):
        logs_path = self.cfg.get("LOGS", "LOGS_PATH")
        return logs_path

    @property
    def report_path(self):
        report_path = self.cfg.get("REPORTS", "REPORTS_PATH")
        return report_path

    @property
    def default_driver(self):
        default_driver = self.cfg.get("DRIVER", "DEFAULT_DRIVER")
        return default_driver

    @property
    def time_out(self):
        time_out = self.cfg.get("DEFAULT", "TIME_OUT")
        return float(time_out)

    @property
    def log_level(self):
        log_level_value = int(self.cfg.get('LOGS', 'LOG_LEVEL'))
        return log_level_value

    @property
    def log_path(self):
        log_path = self.cfg.get('LOGS', 'LOGS_PATH')
        return log_path

    @property
    def screenshot_path(self):
        screenshot_path_value = self.cfg.get('DEFAULT', 'SCREEN_PATH')
        return screenshot_path_value

    @property
    def name_default(self):
        name_default = self.cfg.get('DEFAULT', 'NAME')
        return name_default

    @property
    def password_default(self):
        password_default = self.cfg.get('DEFAULT', 'PASSWORD')
        return password_default


local_config = ConfigUtils()

if __name__ == "__main__":
    print(local_config.log_path)
