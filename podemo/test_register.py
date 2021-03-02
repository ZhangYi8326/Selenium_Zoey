# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 10:04
# @Author  : Zoey
# @File    : test_register.py
# @describe:

from podemo.index_page import IndexPage


class TestRegister:
    def setup(self):
        self.index = IndexPage()

    def teardown(self):
        self.index.driver.quit()

    def test_register(self):
        assert self.index.goto_register().register()
