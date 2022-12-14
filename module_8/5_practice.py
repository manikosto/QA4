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
driver.set_window_size(1920, 1080)
driver.get("https://demoqa.com/webtables")

ROWS = ("xpath", "//div[@role='rowgroup']")
CELLS = ("xpath", "//div[@role='gridcell']")

''' Работа средствами питона'''

def get_all_cells_in_row_value(row):
    for element in driver.find_elements("xpath", f"//div[@role='rowgroup'][{row}]//div[@role='gridcell']"):
        print(element.text)

def get_cell_value(row, cell):
    for element in driver.find_elements("xpath", f"//div[@role='rowgroup'][{row}]//div[@role='gridcell'][{cell}]"):
        print(element.text)

def delete_row(row):
    driver.find_element("xpath", f"//div[@role='rowgroup'][{row}]//span[@title='Delete']").click()

get_all_cells_in_row_value(3) # Получимс все ячейки из указанного ряда
get_cell_value(2, 3) # Получим значение 3-ей ячейки второго ряда
delete_row(3) # Удалим третий ряд
