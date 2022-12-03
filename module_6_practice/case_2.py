import time
import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

login = "qa4@yandex.ru"
password = "123"

#  Страница логина
LOGIN_FIELD = "//input[@id='login_email']"
PASSWORD_FIELD = "//input[@id='password']"
SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

# Страница профиля
# PROFILE_LINK = "//span[@class='full-name']"
PROFILE_LINK = "//div[@class='__navigation__profile-menu__6c7ac    ']"
MY_PROFILE_SETTING_LINK = "//a[@href='/profile/settings']"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.freeconferencecall.com/en/us/login")

#  Записывае URL страницы логина
login_url = driver.current_url

#  Логинимся
driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(login)
driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
driver.find_element(By.XPATH, SUBMIT_BUTTON).click()
time.sleep(3)

#  Проверяем, что залогинились
assert driver.current_url != login_url, "Логин не получился"

driver.find_element(By.XPATH, PROFILE_LINK).click()
driver.find_element(By.XPATH, MY_PROFILE_SETTING_LINK).click()

time.sleep(3)