# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:53
# @Author  : Zoey
# @File    : index_page.py
# @describe:
from selenium.webdriver.common.by import By
from seleniumPO.page.login_page import LoginPage

from seleniumPO.page.base_page import BasePage


class IndexPage(BasePage):
    def goto_login(self):
        """
        进入到登录页面
        :return:
        """
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return LoginPage
        return LoginPage(self.driver)
