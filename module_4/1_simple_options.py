import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Part 1 --- Call options
options = Options()

# Part 2 --- Use headless mode
# options.add_argument("--headless")

# Part 3 --- Driver initialization
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://whatismyipaddress.com/")

driver.get("https://vk.com")
main_window = driver.current_window_handle
print("Первое окно", main_window)
time.sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://youtube.com")
time.sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://yandex.ru")
time.sleep(2)

driver.switch_to.new_window("window")
second_window = driver.current_window_handle
driver.get("https://github.com")
print("Второе окно", second_window)

time.sleep(2)
driver.switch_to.window(main_window)
driver.quit()
time.sleep(2)

driver.switch_to.window(second_window)

driver.switch_to.new_window("tab")
driver.get("https://yandex.ru")

time.sleep(2)




# list_of_tabs = driver.window_handles
# print(list_of_tabs)
# driver.switch_to.window(list_of_tabs[1])
