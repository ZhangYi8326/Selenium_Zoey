# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:41
# @Author  : Zoey
# @File    : test_contact.py
# @describe:

from seleniumPO.page.main_page import MainPage
from seleniumPO.page.login_page import LoginPage
from seleniumPO.pyse.driver import Driver
from seleniumPO.page.index_page import IndexPage
from seleniumPO.page.add_member_page import AddMemberPage


class TestContact:

    def setup_class(self):
        self.driver = Driver()
        self.loginpage = LoginPage(self.driver)
        self.index = IndexPage(self.driver)
        self.mainpage = MainPage(self.driver)
        self.addmember = AddMemberPage(self.driver)

    def setup_class(self):
        self.driver.quit()

    def test_index(self):
        """
        从首页进入登录页面
        :return:
        """
        self.index.goto_login()

    def test_login(self):
        """
        扫码登录
        :return:
        """
        self.loginpage.scan()

    def test_goto_addmember_page(self):
        """
        从主页进入通讯录页面
        :return:
        """
        self.mainpage.goto_add_member()

    def test_addmember(self):
        """
        添加成员
        :return:
        """
        username = "u222"
        account = "a222"
        phone = "11122222222"
        self.addmember.add_member(username, account, phone)
        names = self.addmember.get_member()
        assert username in names
