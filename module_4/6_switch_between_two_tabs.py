import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Part 1 --- Driver initialization
options = Options()  # Call options of browser
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)
driver.get("https://whatismyipaddress.com/")

# Step 2 --- Get first tab descriptor
first_tab = driver.current_window_handle
print("Дескриптор первой вкладки: ", first_tab)

# Step 3 --- Open new tab and get second tab descriptor
driver.switch_to.new_window("tab")  # Switch to new tab automatically
time.sleep(2)
second_tab = driver.current_window_handle
print("Дескриптор второй вкладки: ", second_tab)

# Step 4 --- Check tab is switched
assert driver.current_window_handle != first_tab, "Вкладка не переключилась"

# Step 5 --- Switch to first tab
driver.switch_to.window(first_tab)
time.sleep(2)
assert driver.current_window_handle == first_tab, "Вкладка не переключилась"