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

# Ex: 1
# SOURCE = ("xpath", "//div[@id='draggable']")
# TARGET = ("xpath", "//div[@id='droppable']")
#
# driver.get("https://demoqa.com/droppable")
#
# SOURCE = driver.find_element(*SOURCE)
# TARGET = driver.find_element(*TARGET)
#
# wait.until(EC.element_to_be_clickable(SOURCE))
# action.drag_and_drop(SOURCE, TARGET).perform()
#
# time.sleep(5)

# Ex: 2
SOURCE = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

driver.get("https://demoqa.com/sortable")


def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source)
    TARGET = driver.find_element(*target)
    wait.until(EC.element_to_be_clickable(SOURCE))
    action.drag_and_drop(SOURCE, TARGET).perform()


drag_and_drop(SOURCE, TARGET)

time.sleep(5)

# Ex: 3
# GRID_TAB = ("xpath", "//a[@id='demo-tab-grid']")
#
# driver.get("https://demoqa.com/sortable")
#
#
# def choose_element(number):
#     return driver.find_element("xpath", f"//div[@class='create-grid']/div[{number}]")
#
#
# def drag_and_drop(source, target):
#     SOURCE = choose_element(source)
#     TARGET = choose_element(target)
#     wait.until(EC.element_to_be_clickable(SOURCE))
#     action.drag_and_drop(SOURCE, TARGET).perform()
#
#
# driver.find_element(*GRID_TAB).click()
#
# time.sleep(2)
# drag_and_drop(4, 6)
#
# time.sleep(5)
