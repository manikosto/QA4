import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(3)
ADD_BUTTON = driver.find_element(By.XPATH, "//button[text()='Add Element']")
# 2 варианта записи локатороВ, так как он будет пробовать найти сразу
time.sleep(3)

# ADD_BUTTON.click()
time.sleep(3)
DELETE_BUTTON = ""
assert driver.find_element(By.XPATH, "//button[text()='Delete']"), "Не найдена"

time.sleep(3)