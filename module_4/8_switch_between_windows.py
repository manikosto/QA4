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

# Step 2 --- Get first window descriptor
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Step 3 --- Open new window, switch and get his descriptor
driver.switch_to.new_window("window")  # Open and switch to new window works automatically
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Step 4 --- Check switch to a new window
assert new_window == driver.current_window_handle, "Окно не переключилось"

# Step 5 --- Working in the new window
time.sleep(2)
driver.get("https://vk.com")

# Step 5 --- Switch to old window
driver.switch_to.window(old_window)

# Step 6 --- Check switch from new to old window
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Step 7 --- Working in old window
time.sleep(2)
driver.get("https://ya.ru")

# Step 8 --- Switch to the new window again
driver.switch_to.window(new_window)

# Step 9 --- Check switch from old to new window
assert new_window == driver.current_window_handle, "Окно не переключилось"

# Step 10 --- Close new window
time.sleep(2)
driver.close()
time.sleep(2)
