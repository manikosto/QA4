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

# Step 2 --- Open several tabs
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Step 3 --- Get list and count of opened tabs
windows = driver.window_handles  # Get list of descriptors
print("Список дескрипторов открытых вкладок: ", windows)
print("Количество открытых вкладок: ", len(windows))

# Step 4 --- Get current tab descriptor
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab))

# Step 5 --- Switch tab by index
driver.switch_to.window(windows[1])  # 0 = Tab 1, 1 = Tab 2 and so on
time.sleep(2)

# Step 6 --- Check the tab is switched
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"