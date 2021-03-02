# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 9:56
# @Author  : Zoey
# @File    : login_page.py
# @describe:
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from podemo.register_page import RegisterPage


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫码
        :return:
        """
        pass

    def goto_register(self):
        """
        登录页面点击注册按钮
        :return:
        """
        # click register link
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # returen RegisterPage
        return RegisterPage(self.driver)
