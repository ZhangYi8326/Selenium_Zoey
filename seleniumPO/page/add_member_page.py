# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 11:25
# @Author  : Zoey
# @File    : add_member_page.py
# @describe:
from selenium.webdriver.common.by import By
from seleniumPO.pyse.pyselenium import PySelenium


class AddMemberPage:

    def __init__(self, driver):
        self.driver = driver
        self.element = PySelenium(self.driver)

    def add_member(self, username, account, phone):
        """
        添加联系人
        :return:
        """
        # 输入用户名
        self.element.find(By.ID, "username").send_keys(username)
        # 输入账号
        self.element.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入手机号
        self.element.find(By.ID, "memberAdd_phone").send_keys(phone)
        # 点击保存
        self.element.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        """
        获取所有的联系人姓名
        :return:
        """
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.element.wait_for_click(10, locator)
        eles_list = self.element.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(eles_list)
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        return names
