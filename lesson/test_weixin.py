# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/9 18:47
@Auth ： Zoey
@File ：test_weixin.py
@Description：
"""
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeiXin:
    def setup(self):
        # 复用当前打开的浏览器
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # 获取当前页面的cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850387684186'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ZDLJ-nqjHYQJAMKrLDERTfFK_ReyRNqYWxMQ32qXN533uWXyTY4TkshVlcGyT6d7nnTIPdCjCpBQwJxeNmQ3Xf3DtkN9vOS-LwmkdKoP8keVcktWh0CpEmt6SkRHUVf7X-Kq3GqjoDEGwZJOchkCel83BdLiOQ0YaT8t0CNYgDzIZyJDRZ6DXS-gT0oZrsN_x7peNtkDoan7ZCqfvinVRSEjlofFlcIw0qgZOSfJ-qth9iXCrR-E0BwtR6p-HXNP-KqlPdRieDhku76yM-rGJw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850387684186'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324984372555'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'XxoIHbLnOyxokL35kaMXYcEY4JV--yB8lrB6vBG5JocOls2QkgIRZIqB8tR6mpYS'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3117709'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612869027'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1000511919617191'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644405026, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612854291,1612867206,1612868952,1612869018'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6047996690'}, {'domain': '.qq.com', 'expiry': 1620643179, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'secure': False, 'value': '1.1.1448342440.1612867179'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612885732, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '64j1puf'}, {'domain': '.qq.com', 'expiry': 1612955446, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.276739561.1612854292'}, {'domain': '.qq.com', 'expiry': 1675941046, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.68911452.1612854292'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644390196, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1615461050, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1874410691, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5ced39c3507f8'}, {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f6491862162810a29e4bca2acf9b6f12c16a1ca136029eed2deee4f8f60a5a44'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'udoduWDYRs'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '3844364288'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print(cookie)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(6)

    def test_contart(self):
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = [
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #         #      'value': '1688850387684186'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #         #      'value': 'ZDLJ-nqjHYQJAMKrLDERTfFK_ReyRNqYWxMQ32qXN533uWXyTY4TkshVlcGyT6d7nnTIPdCjCpBQwJxeNmQ3Xf3DtkN9vOS-LwmkdKoP8keVcktWh0CpEmt6SkRHUVf7X-Kq3GqjoDEGwZJOchkCel83BdLiOQ0YaT8t0CNYgDzIZyJDRZ6DXS-gT0oZrsN_x7peNtkDoan7ZCqfvinVRSEjlofFlcIw0qgZOSfJ-qth9iXCrR-E0BwtR6p-HXNP-KqlPdRieDhku76yM-rGJw'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #         #      'value': '1688850387684186'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #         #      'value': '1970324984372555'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #         #      'value': 'XxoIHbLnOyxokL35kaMXYcEY4JV--yB8lrB6vBG5JocOls2QkgIRZIqB8tR6mpYS'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #         #      'value': 'a3117709'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #         #      'path': '/', 'secure': False, 'value': '1612869027'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #         #      'value': '1000511919617191'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #         #      'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644405026, 'httpOnly': False,
        #         #                      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #         #                      'value': '1612854291,1612867206,1612868952,1612869018'},
        #         #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #         #      'value': 'direct'},
        #         #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #         #      'secure': False, 'value': '6047996690'},
        #         #     {'domain': '.qq.com', 'expiry': 1620643179, 'httpOnly': False, 'name': '_gcl_au', 'path': '/',
        #         #      'secure': False, 'value': '1.1.1448342440.1612867179'},
        #         #     {'domain': 'work.weixin.qq.com', 'expiry': 1612885732, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #         #      'secure': False, 'value': '64j1puf'},
        #         #     {'domain': '.qq.com', 'expiry': 1612955446, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #         #      'value': 'GA1.2.276739561.1612854292'},
        #         #     {'domain': '.qq.com', 'expiry': 1675941046, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #         #      'value': 'GA1.2.68911452.1612854292'},
        #         #     {'domain': '.work.weixin.qq.com', 'expiry': 1644390196, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #         #      'path': '/', 'secure': False, 'value': '0'},
        #         #     {'domain': '.work.weixin.qq.com', 'expiry': 1615461050, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #         #      'path': '/', 'secure': False, 'value': 'zh'},
        #         #     {'domain': '.qq.com', 'expiry': 1874410691, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #         #      'secure': False, 'value': '0_5ced39c3507f8'},
        #         #     {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #         #      'value': 'f6491862162810a29e4bca2acf9b6f12c16a1ca136029eed2deee4f8f60a5a44'},
        #         #     {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #         #      'value': 'udoduWDYRs'},
        #         #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #         #      'secure': False, 'value': '3844364288'}]
        db = shelve.open("./mydbs/cookies")
        cookies = db["cookie"]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print(cookie)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_elements_by_css_selector(".index_service_cnt_item")[1].click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys(r"D:\Users\Administrator\PycharmProjects\Selenium_Zoey\lesson\mydata.xlsx")
        time.sleep(3)
        self.driver.find_element_by_css_selector(".ww_btn_Large").click()
        time.sleep(3)

    def test_shelve(self):
        # 存cookies
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850387684186'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'ZDLJ-nqjHYQJAMKrLDERTfFK_ReyRNqYWxMQ32qXN533uWXyTY4TkshVlcGyT6d7nnTIPdCjCpBQwJxeNmQ3Xf3DtkN9vOS-LwmkdKoP8keVcktWh0CpEmt6SkRHUVf7X-Kq3GqjoDEGwZJOchkCel83BdLiOQ0YaT8t0CNYgDzIZyJDRZ6DXS-gT0oZrsN_x7peNtkDoan7ZCqfvinVRSEjlofFlcIw0qgZOSfJ-qth9iXCrR-E0BwtR6p-HXNP-KqlPdRieDhku76yM-rGJw'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850387684186'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324984372555'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'XxoIHbLnOyxokL35kaMXYcEY4JV--yB8lrB6vBG5JocOls2QkgIRZIqB8tR6mpYS'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a3117709'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1612869027'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '1000511919617191'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644405026, 'httpOnly': False,
        #                      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                      'value': '1612854291,1612867206,1612868952,1612869018'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '6047996690'},
        #     {'domain': '.qq.com', 'expiry': 1620643179, 'httpOnly': False, 'name': '_gcl_au', 'path': '/',
        #      'secure': False, 'value': '1.1.1448342440.1612867179'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1612885732, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '64j1puf'},
        #     {'domain': '.qq.com', 'expiry': 1612955446, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.276739561.1612854292'},
        #     {'domain': '.qq.com', 'expiry': 1675941046, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.68911452.1612854292'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1644390196, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1615461050, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 1874410691, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': False, 'value': '0_5ced39c3507f8'},
        #     {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': 'f6491862162810a29e4bca2acf9b6f12c16a1ca136029eed2deee4f8f60a5a44'},
        #     {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': 'udoduWDYRs'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '3844364288'}]
        # db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        # 取cookies
        db = shelve.open("./mydbs/cookies")
        cookies = db["cookie"]

