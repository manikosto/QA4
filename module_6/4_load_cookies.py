import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/en/us/login")

# Добавление куков
driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://www.freeconferencecall.com/profile")
time.sleep(5)

''' Debug mode '''

# driver.get("https://www.freeconferencecall.com")
# print(driver.get_cookies())
# driver.delete_cookie("country_code")
# driver.delete_cookie("locale")
# driver.add_cookie({'domain': 'www.freeconferencecall.com', 'httpOnly': True, 'name': 'country_code', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'ae'})
# driver.add_cookie({'domain': 'www.freeconferencecall.com', 'httpOnly': False, 'name': 'locale', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'ar'})
# print(driver.get_cookies())
# driver.get("https://www.freeconferencecall.com")
# time.sleep(10)