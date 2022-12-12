import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

''' Example 1 '''
# driver.get("https://demoqa.com/dynamic-properties")
#
# VISIBLE_AFTER_5_BUTTON = ("xpath", "//button[@id='visibleAfter']")
#
# wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_5_BUTTON))
# driver.find_element(*VISIBLE_AFTER_5_BUTTON).click()

''' Example 2 '''
# driver.get("http://the-internet.herokuapp.com/dynamic_controls")
#
# ADD_BUTTON = ("xpath", "//button[text()='Add']")
# REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
#
# wait.until(EC.element_to_be_clickable(REMOVE_BUTTON))
# driver.find_element(*REMOVE_BUTTON).click()
#
# wait.until(EC.element_to_be_clickable(ADD_BUTTON))
# driver.find_element(*ADD_BUTTON).click()

''' Example 3 '''
# driver.get("http://the-internet.herokuapp.com/dynamic_controls")
#
# INPUT = ("xpath", "(//input[@type='text'])[1]")
# ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
#
# DISABLED = driver.find_element(*INPUT).get_attribute("disabled")
#
# if DISABLED == "true":
#     driver.find_element(*ENABLE_BUTTON).click()
#
# while DISABLED == "true":
#     time.sleep(0.5)
#     DISABLED = driver.find_element(*INPUT).get_attribute("disabled")
# else:
#     driver.find_element(*INPUT).send_keys("Hello")

''' Example 4 '''
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

ADD_ELEMENT_BUTTON = ("xpath", "//button[@onclick='addElement()']")
DELETE_ELEMENT_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")

wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))
driver.find_element(*ADD_ELEMENT_BUTTON).click()

wait.until(EC.visibility_of_element_located(DELETE_ELEMENT_BUTTON))
driver.find_element(*DELETE_ELEMENT_BUTTON).click()

wait.until(EC.invisibility_of_element_located(DELETE_ELEMENT_BUTTON))



