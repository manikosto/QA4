import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/key_presses")

KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")

time.sleep(3)

driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello world!")
time.sleep(1)
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.COMMAND + "A")
time.sleep(1)
driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACK_SPACE)
time.sleep(3)
