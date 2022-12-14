import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

''' Radio '''
driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")
IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

print(driver.find_element(*YES_RADIO_BUTTON).is_selected())
wait.until(EC.element_to_be_clickable(YES_RADIO_LABEL))
driver.find_element(*YES_RADIO_LABEL).click()
print(driver.find_element(*YES_RADIO_BUTTON).is_selected())

print(driver.find_element(*NO_RADIO_BUTTON).is_enabled())

time.sleep(2)



