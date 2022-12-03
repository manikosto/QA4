import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Part 1 --- Driver initialization
options = Options()  # Call options of browser
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1920, 1080)
driver.get("https://testautomationpractice.blogspot.com")


# iframe_volunteer = driver.find_elements(By.TAG_NAME, "iframe")[0]
iframe_volunteer = driver.find_element(By.XPATH, "//iframe")
print(driver.current_window_handle)
time.sleep(3)

driver.switch_to.frame(iframe_volunteer)
print(driver.current_window_handle)
time.sleep(3)

first_name_field = driver.find_element(By.XPATH, "//input[@name='RESULT_TextField-1']")
first_name_field.send_keys("Alexey")
time.sleep(3)

driver.switch_to.default_content()
first_name_field.send_keys("Alexey")
#
# time.sleep(5)