# coding:utf-8

import time
from os import getenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def site_login():
    # 最大待ち時間
    driver.get("https://stg.kpiee.xyz/users/sign_in")
    wait_time = 10
    wait = WebDriverWait(driver, wait_time)

    wait.until(lambda d: d.find_element(by=By.CSS_SELECTOR,
                                        value='input[type="email"]'))

    email_el = driver.find_element(by=By.CSS_SELECTOR,
                                   value='input[type="email"]')
    password_el = driver.find_element(by=By.CSS_SELECTOR,
                                      value='input[type="password"]')
    checkbox_el = driver.find_element(by=By.CSS_SELECTOR,
                                      value="input.bl_kpCheckbox+label")
    submit_button_el = driver.find_element(by=By.CSS_SELECTOR,
                                           value=".bl_kpBtn.bl_kpBtn__login")

    email = getenv('KPIEE_EMAIL')
    password = getenv('KPIEE_PASSWORD')

    time.sleep(2)

    checkbox_el.click()
    email_el.send_keys(email)
    password_el.send_keys(password)
    submit_button_el.click()


if __name__ == '__main__':

    driver.get("https://stg.kpiee.xyz/users/sign_in")

    print(driver.title)

    site_login()

    driver.quit()
