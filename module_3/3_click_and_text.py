import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

# Click on element

WIKI_PAGE_BUTTON = driver.find_element(By.CLASS_NAME, "wikipedia-search-wiki-link")
WIKI_PAGE_BUTTON.click()

FIELD_2 = driver.find_element(By.ID, "field2")
FIELD_2.send_keys("Aleksei")

time.sleep(5)