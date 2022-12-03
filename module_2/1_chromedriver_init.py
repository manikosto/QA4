# Step 1 --- Imports to start
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Step 2 --- Driver initialization Chrome
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(5)

