# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 14:44
# @Author  : Zoey
# @File    : pyselenium.py
# @describe:
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seleniumPO.pyse.driver import Driver


class PySelenium:

    def __init__(self, driver):
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()

    def find(self, locator, value):
        self.driver.find_element(locator, value)

    def finds(self, locator, value):
        self.driver.find_elements(locator, value)

    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
