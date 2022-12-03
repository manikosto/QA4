import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Step 1 --- Driver initialization
options = Options()  # Call options of browser
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)
driver.get("https://whatismyipaddress.com/")

# Step 2 --- Open new tab
driver.switch_to.new_window("tab")  # Switch to new tab is automatically

# Step 3 --- Open new window
driver.switch_to.new_window("window")  # Switch to new window is automatically
