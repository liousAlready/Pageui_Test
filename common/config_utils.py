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

    @property
    def element_info_path(self):
        element_info_path = self.cfg.get("TEST", "element_info_path")
        return element_info_path

    @property
    def test_data_path(self):
        test_data_path = self.cfg.get("TEST", "TEST_DATES")
        return test_data_path

    @property
    def test_path(self):
        test_path = self.cfg.get("TEST", "TEST_CASE")
        return test_path

    @property
    def test_datas_path(self):
        test_path = self.cfg.get("TEST", "TEST_DATA_PATH")
        return test_path

    @property
    def test_data_paths(self):
        test_data_paths = self.cfg.get("TEST", "test_data_paths")
        return test_data_paths

    @property
    def smtp_server(self):
        smtp_server = self.cfg.get("email", "smtp_server")
        return smtp_server

    @property
    def smtp_sender(self):
        smtp_sender = self.cfg.get("email", "smtp_sender")
        return smtp_sender

    @property
    def smtp_sender_password(self):
        smtp_sender_password = self.cfg.get("email", "smtp_sender_password")
        return smtp_sender_password

    @property
    def smtp_receiver(self):
        smtp_receiver = self.cfg.get("email", "smtp_receiver")
        return smtp_receiver

    @property
    def smtp_cc(self):
        smtp_cc = self.cfg.get("email", "smtp_cc")
        return smtp_cc

    @property
    def smtp_subject(self):
        smtp_subject = self.cfg.get("email", "smtp_subject")
        return smtp_subject


local_config = ConfigUtils()

if __name__ == "__main__":
    print(local_config.time_out)
    print(local_config.smtp_subject)
    print(local_config.smtp_receiver)
    print(local_config.smtp_sender)
    print(local_config.test_data_path)
