import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

def choose_drag_element(number):
    return driver.find_element("xpath", f"//div[@class='grid__item'][{number}]")

def choose_drop_area(number):
    return driver.find_element("xpath", f"//div[@class='drop-area__item'][{number}]")

def drag_and_drop(source, target):
    action.click_and_hold(source) \
        .pause(2) \
        .move_to_element(target) \
        .release() \
        .perform()

drag_and_drop(choose_drag_element(7), choose_drop_area(2))


time.sleep(5)