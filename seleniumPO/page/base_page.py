# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 10:13
# @Author  : Zoey
# @File    : base_page.py
# @describe:

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # option = Options()
            # option.debugger_address = '127.0.0.1:9222'
            # self.driver = webdriver.Chrome(options=option)
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def quit_driver(self):
        self.driver.quit()

    def find(self, locator, value):
        self.driver.find_element(locator, value)

    def finds(self, locator, value):
        self.driver.find_elements(locator, value)

    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
