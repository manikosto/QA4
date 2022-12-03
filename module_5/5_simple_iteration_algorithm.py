import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'normal'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/subscription")
time.sleep(3)
TRACKS = driver.find_elements(By.XPATH, "//a[contains(@class, 'btn-category rounded-pill')]")
print(TRACKS)
for TRACK in TRACKS:
    TRACK.click()
    time.sleep(2)

time.sleep(5)