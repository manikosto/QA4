import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

''' Пример 1 '''
driver.get("http://the-internet.herokuapp.com/dynamic_controls")

TEXT_FIELD = ("xpath", "//input[@type='text']")
ENABLE_BUTTON = ("xpath", "//button[@onclick='swapInput()']")

print(driver.find_element(*TEXT_FIELD).is_enabled())

driver.find_element(*ENABLE_BUTTON).click()
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))

print(driver.find_element(*TEXT_FIELD).is_enabled())

''' Пример 2'''
driver.get("https://demoqa.com/dynamic-properties")

ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

print(driver.find_element(*ENABLE_BUTTON).is_enabled())
print(driver.find_element(*ENABLE_BUTTON).is_displayed())
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))

