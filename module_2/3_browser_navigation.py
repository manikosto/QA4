# Step 4 --- Import time
import time
# Step 1 --- Imports to start
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Step 2 --- Driver initialization Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 3 --- Get page
driver.get("https://ozon.ru")

# Step 4 --- Time sleep
time.sleep(10)

# Step 5 --- Go back
driver.back()

# Step 6 --- Go forward
driver.forward()

# Step 7 --- Refresh page
driver.refresh()

# Step 8 --- Close and Quit
driver.close()
driver.quit()


time.sleep(2)