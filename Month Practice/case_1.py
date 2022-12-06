import time
import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

login = "qa4@yandex.ru"
password = "123"

LOGIN_FIELD = "//input[@id='login_email']"
PASSWORD_FIELD = "//input[@id='password']"
SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.freeconferencecall.com/en/us/login")

time.sleep(3)
login_url = driver.current_url

driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(login)
driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
driver.find_element(By.XPATH, SUBMIT_BUTTON).click()
time.sleep(3)

assert driver.current_url != login_url, "Логин не получился"

time.sleep(1)
