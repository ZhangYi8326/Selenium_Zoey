# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 14:40
# @Author  : Zoey
# @File    : driver.py
# @describe:

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


class Driver:

    def __new__(cls):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://work.weixin.qq.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        return cls.driver
