import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Пакет для поиска локаторов
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

WIKI_SEARCH_INPUT = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
print(WIKI_SEARCH_INPUT)
time.sleep(3)

HEADER_TITLE = driver.find_element(By.CLASS_NAME, "title")
print(HEADER_TITLE.text)

ELEMENT_BY_TAG_NAME = driver.find_element(By.TAG_NAME, "h2")
print(ELEMENT_BY_TAG_NAME)

LINK_BY_TEXT = driver.find_element(By.LINK_TEXT, "Software Testing Tutorials")
print(LINK_BY_TEXT)