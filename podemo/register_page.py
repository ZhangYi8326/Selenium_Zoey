# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 9:56
# @Author  : Zoey
# @File    : register_page.py
# @describe:
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_register_title(self):
        """
        进入注册页面
        :return:
        """
        title = self.driver.find_element(By.CSS_SELECTOR, ".register_simple_header_title").text
        return title

    def register(self):
        """
        注册
        :return:
        """
        # 输入公司名
        self.driver.find_element(By.ID, "corp_name").send_keys("111111")
        # 输入管理者姓名
        self.driver.find_element(By.ID, "manager_name").send_keys("222222")
        # 输入电话号码
        self.driver.find_element(By.ID, "register_tel").send_keys("12122222222")
        # 点击获取验证码
        self.driver.find_element(By.ID, "get_vcode").click()
        # 输入验证码
        self.driver.find_element(By.ID, "vcode").send_keys("123123")
        # 勾选同意协议复选框
        self.driver.find_element(By.ID, "iagree").click()
        # 点击注册
        self.driver.find_element(By.ID, "submit_btn").click()
