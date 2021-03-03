# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:55
# @Author  : Zoey
# @File    : login_page.py
# @describe:
import shelve
import time

from seleniumPO.pyse.pyselenium import PySelenium


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.element = PySelenium(self.driver)

    def scan(self):
        """
        扫码登录:读取cookies登录
        :return:
        """
        db = shelve.open("../../lesson/mydbs/cookies")
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print(cookie)
        time.sleep(3)
        self.driver.refresh()

