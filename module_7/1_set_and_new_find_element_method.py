
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get("http://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")

driver.find_element(*REMOVE_BUTTON).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))