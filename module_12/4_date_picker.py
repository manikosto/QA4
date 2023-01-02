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

driver.get("https://demoqa.com/date-picker")

DATE_PICKER = ("xpath", "//input[@id='dateAndTimePickerInput']")
MONTH = ("xpath", "//div[contains(@class, 'react-datepicker__month-dropdown')]")
YEAR = ("xpath", "//div[contains(@class, 'react-datepicker__year-read-view')]")

UP = ("xpath", "(//a[contains(@class, 'react-datepicker__navigation')])[1]")
DOWN = ("xpath", "(//a[contains(@class, 'react-datepicker__navigation')])[2]")


def choose_date(month, year, day):
    MONTHS_DROPDOWN = ("xpath", f"//div[@class='react-datepicker__month-option' and text()='{month}']")
    YEAR_DROPDOWN = ("xpath", f"//div[@class='react-datepicker__year-option' and text()='{year}']")
    DAY = ("xpath", f"//div[text()='{day}']")
    driver.find_element(*MONTH).click()
    driver.find_element(*MONTHS_DROPDOWN).click()
    driver.find_element(*YEAR).click()
    while True:
        try:
            driver.find_element(*YEAR_DROPDOWN).click()
            break
        except:
            driver.find_element(*UP).click()
    driver.find_element(*DAY).click()


driver.find_element(*DATE_PICKER).click()
choose_date("January", "2038", "20")

time.sleep(3)