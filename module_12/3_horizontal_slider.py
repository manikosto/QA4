import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)

def move_slider(current_point_attribute, end_point, slider):
    if end_point < int(slider.get_attribute(current_point_attribute)):
        while int(slider.get_attribute(current_point_attribute)) != end_point:
            slider.send_keys(Keys.ARROW_LEFT)
    else:
        while int(slider.get_attribute(current_point_attribute)) != end_point:
            slider.send_keys(Keys.ARROW_RIGHT)
# Ex: 1
# driver.get("https://demoqa.com/slider")
# SLIDER = ("xpath", "//input[@type='range']")
# SLIDER = driver.find_element(*SLIDER)
# move_slider("value", 75, SLIDER)

# Ex: 2
driver.get("http://seiyria.com/bootstrap-slider")

SLIDER_1 = ("xpath", "(//div[@class='slider-handle min-slider-handle round'])[2]")
SLIDER_2 = ("xpath", "(//div[@class='slider-handle max-slider-handle round'])[1]")

SLIDER_1 = driver.find_element(*SLIDER_1)
SLIDER_2 = driver.find_element(*SLIDER_2)

move_slider("aria-valuenow", 100, SLIDER_1)
move_slider("aria-valuenow", 685, SLIDER_2)

time.sleep(3)