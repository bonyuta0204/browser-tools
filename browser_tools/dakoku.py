# coding:utf-8

import time
from os import getenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class FreeeDakoku:

    def __init__(self, email, password):
        self.driver = webdriver.Chrome()
        self.email = email
        self.password = password

    def login(self):
        # 最大待ち時間
        self.driver.get("https://accounts.secure.freee.co.jp/login/hr")
        wait_time = 10
        wait = WebDriverWait(self.driver, wait_time)

        wait.until(lambda d: d.find_element(by=By.CSS_SELECTOR,
                                            value='input[type="email"]'))

        email_el = self.driver.find_element(by=By.CSS_SELECTOR,
                                            value='input[type="email"]')
        password_el = self.driver.find_element(by=By.CSS_SELECTOR,
                                               value='input[type="password"]')
        submit_el = self.driver.find_element(by=By.CSS_SELECTOR,
                                             value='input[type="submit"]')

        time.sleep(2)

        email_el.send_keys(self.email)
        password_el.send_keys(self.password)
        submit_el.click()

        try:
            wait.until(
                lambda d: 'https://p.secure.freee.co.jp' in d.current_url)
        except TimeoutException:
            raise Exception('ログインに失敗しました')

        print('login succeeded')

    def shukkin():
        print('shukkin')

    def taikin():
        print('taikin')

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    dakoku = FreeeDakoku()
    dakoku.login()
    time.sleep(10)
    dakoku.quit()
