import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
driver.get("https://demoqa.com/buttons")

DOUBLE_CLICK_BUTTON = driver.find_element(*DOUBLE_CLICK_BUTTON)

action.click_and_hold(DOUBLE_CLICK_BUTTON).perform()

time.sleep(5)