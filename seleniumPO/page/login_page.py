# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:55
# @Author  : Zoey
# @File    : login_page.py
# @describe:
import shelve
import time

from seleniumPO.page.base_page import BasePage


class LoginPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"

    # def __init__(self, driver):
    #     self.driver = driver

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

