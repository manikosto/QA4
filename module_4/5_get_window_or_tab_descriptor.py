import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Step 1 --- Call options
options = Options()

# Step 2 --- Driver initialization
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)

# Step 4 --- Start browser
driver.get("https://whatismyipaddress.com/")

# Step 5 --- Get window descriptor
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)

# Step 6 --- Get list of descriptors
driver.switch_to.new_window("tab")  # Open the second tab
time.sleep(2)
descriptor_list = driver.window_handles
print("Список всех открытых вкладок / Дескрипторы всех вкладок: ", descriptor_list)
