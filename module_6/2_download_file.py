import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


FILES = "//a"

options = Options()
preferences = {
    "download.default_directory": os.getcwd() + "/downloads",
    "safebrowsing.enabled": "false"
}
options.add_experimental_option("prefs", preferences)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://the-internet.herokuapp.com/download")

links = driver.find_elements(By.XPATH, FILES)
links[1].click()

time.sleep(5)