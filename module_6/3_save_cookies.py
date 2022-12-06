import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


login = "qa4@yandex.ru"
password = "123"

LOGIN_FIELD = "//input[@id='login_email']"
PASSWORD_FIELD = "//input[@id='password']"
SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

PROFILE_LINK = "//div[@class='__navigation__profile-menu__6c7ac    ']"
LOGOUT_BUTTON = "//a[@title='Log Out']"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(login)
driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(password)
driver.find_element(By.XPATH, SUBMIT_BUTTON).click()
time.sleep(3)
# Сохраняем куки
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

