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

driver.get("https://clipboardjs.com/")

COPY = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE = ("xpath", "//textarea[@id='bar']")

COPY = driver.find_element(*COPY)
PASTE = driver.find_element(*PASTE)

# action.scroll_to_element(COPY).click(COPY).perform()
# time.sleep(2)
# PASTE.send_keys(Keys.COMMAND + "V")

cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

PASTE.send_keys(cmd_ctrl + "A")
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "X")
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "V")



time.sleep(5)