import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

H3 = ("xpath", "//h3")
FOOTER = ("xpath", "//div[@class='large-4 large-centered']")

driver.find_element(*H3)

driver.find_element(*FOOTER)

time.sleep(3)