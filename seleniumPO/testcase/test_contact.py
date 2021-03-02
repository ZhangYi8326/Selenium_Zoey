# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:41
# @Author  : Zoey
# @File    : test_contact.py
# @describe:

from seleniumPO.page.main_page import MainPage
from seleniumPO.page.login_page import LoginPage


class TestContact:
    def setup(self):
        # self.mainpage = MainPage()
        self.loginpage = LoginPage()

    def teardown_class(self):
        self.mainpage.quit_driver()

    def test_login(self):
        """
        扫码登录
        :return:
        """
        self.loginpage.scan()

    def test_addmember(self):
        username = "u222"
        account = "a222"
        phone = "11122222222"
        page = self.mainpage.goto_add_member()
        names = page.get_member()
        assert username in names
