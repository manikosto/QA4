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

driver.get("https://demoqa.com/buttons")

CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")

CLICK_ME_BUTTON = driver.find_element(*CLICK_ME_BUTTON)

action.click(CLICK_ME_BUTTON).perform()

time.sleep(5)