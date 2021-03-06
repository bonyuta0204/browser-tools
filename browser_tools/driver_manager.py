# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def install_chrome_driver():
    webdriver.Chrome(service=Service(ChromeDriverManager().install()))


if __name__ == '__main__':
    install_chrome_driver()
