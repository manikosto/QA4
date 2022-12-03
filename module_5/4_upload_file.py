import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/upload-download")

upload_file_field = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
download_file_field = driver.find_element(By.XPATH, "//a[@id='downloadButton']")

upload_file_field.send_keys(f"{os.getcwd()}/files/picture.jpg")
download_file_field.click()


time.sleep(5)