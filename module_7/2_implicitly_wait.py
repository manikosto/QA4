import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(3)

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_5_BUTTON = ("xpath", "//button[@id='visibleAfter']")
ENABLE_AFTER_5_BUTTON = ("xpath", "//button[@id='enableAfter']")
driver.find_element(*ENABLE_AFTER_5_BUTTON).click()
