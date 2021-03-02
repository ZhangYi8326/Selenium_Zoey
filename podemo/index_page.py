# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 9:34
# @Author  : Zoey
# @File    : index_page.py
# @describe:

from selenium import webdriver
from selenium.webdriver.common.by import By

from podemo.login_page import LoginPage
from podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com")
        self.driver.maximize_window()

    def goto_login(self):
        """
        进入到登录页面
        :return:
        """
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return LoginPage
        return LoginPage(self.driver)
