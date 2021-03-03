# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:05
# @Author  : Zoey
# @File    : main_page.py
# @describe:
from selenium.webdriver.common.by import By
from seleniumPO.page.add_member_page import AddMemberPage
from seleniumPO.pyse.pyselenium import PySelenium


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.element = PySelenium(self.driver)

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        # click add member
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # return AddMemberPage
        return AddMemberPage(self.driver)
