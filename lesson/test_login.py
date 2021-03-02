# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 15:44
# @Author  : Zoey
# @File    : test_login.py
# @describe:

import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_cookie(self):
        """
        复用浏览器，并打印输出当前页面cookies
        :return:
        """
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        cookies = self.driver.get_cookies()
        print(cookies)

    # def teardown(self):
    #     self.driver.quit()

    def test_save_cookies(self):
        """
        存cookie
        :return:
        """
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
              'value': '1688850387684186'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
              'value': 'zx9Z1qzuAU3Z-uLrsAd8nlH-eWQNAjO2hPLu8XfxBAKduUwQBlv920yntvtBtK7nZwYFORDEVqpQimhYzSxXchlPdP6JYkI0bpNlD214IAhLhoOzgGniQknU_dcuoxQXX6ldlNyWzaJAqKNni2EhtNZTzZ2b-K1jycQsf5anrPFH0d8Dpz-ph6t-nZdvzWYKqZ_87_DwYzwQV19MLCGG7DSa5B0P4czuBfGKY_oa4ZbHLNwqKICRDHppJhSOZazk743EF412JOmeaaQmrHiAeA'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
              'value': '1688850387684186'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
              'value': '1970324984372555'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
              'value': 'XxoIHbLnOyxokL35kaMXYbUwO8B111IR4_Zmh-O-UgRx5wnoDvkp6Nndz_xvpHaP'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
              'value': 'a3378584'},
             {'domain': '.qq.com', 'expiry': 1614671763, 'httpOnly': False, 'name': '_gat', 'path': '/',
              'secure': False, 'value': '1'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
              'value': '825592423330234'},
             {'domain': 'work.weixin.qq.com', 'expiry': 1614678464, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
              'secure': False, 'value': 'adqcjc'},
             {'domain': '.qq.com', 'expiry': 1614758113, 'httpOnly': False, 'name': '_gid', 'path': '/',
              'secure': False, 'value': 'GA1.2.854857268.1614567783'},
             {'domain': '.qq.com', 'expiry': 1677743713, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
              'value': 'GA1.2.1103770228.1614567783'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1646103781, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
              'path': '/', 'secure': False, 'value': '0'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
              'value': '1'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
              'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646207555, 'httpOnly': False,
                                   'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                   'value': '1614567782,1614646948,1614671556'},
             {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
              'secure': False, 'value': '1644045644575884'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1617263716, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
              'path': '/', 'secure': False, 'value': 'zh'},
             {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
              'secure': False, 'value': '945530072364646566a07a3dd401e41858051f69f9b5d938acfab0cdc7fae1c8'},
             {'domain': '.qq.com', 'expiry': 2147483643, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
              'value': 'vUpd7UDSHu'}
        ]
        db = shelve.open('./mydbs/cookies')
        db['cookie'] = cookies
        db.close()

    def test_get_cookies(self):
        """
        取cookie
        :return:
        """
        db = shelve.open("./mydbs/cookies")
        cookies = db['cookie']
        for cookie in cookies:
            print(cookie)
        db.close()

    def test_login(self):
        """
        登录微信
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("./mydbs/cookies")
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.refresh()
        db.close()




