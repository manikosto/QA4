import time
import os, sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

COPY = ("xpath", "//button[@data-clipboard-target='#bar']")

driver.get("https://clipboardjs.com/")

COPY = driver.find_element(*COPY)

time.sleep(2)
action.scroll_to_element(COPY).perform()

time.sleep(5)