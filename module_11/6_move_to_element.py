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
driver.set_window_size(1920, 1080)

driver.get("https://demoqa.com/menu")

STEP_1 = ("xpath", "//a[text()='Main Item 2']")
STEP_2 = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3 = ("xpath", "//a[text()='Sub Sub Item 2']")

STEP_1 = driver.find_element(*STEP_1)
STEP_2 = driver.find_element(*STEP_2)
STEP_3 = driver.find_element(*STEP_3)

action.move_to_element(STEP_1) \
    .move_to_element(STEP_2) \
    .click(STEP_3) \
    .perform()

time.sleep(5)