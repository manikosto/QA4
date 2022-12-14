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

''' Простой пример '''
driver.get("http://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
assert driver.find_element(*CHECKBOX_1).get_attribute("checked"), "Чек-бокс не выбран"
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"

driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"

time.sleep(3)

''' Клик по компоненте '''
driver.get("https://demoqa.com/checkbox")

TOGGLE_BUTTON = ("xpath", "//button[@title='Toggle']")
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")
HOME_BUTTON = ("xpath", "//span[text()='Home']")
CHECKBOXES = ("xpath", "//input[@type='checkbox']")

print(driver.find_element(*HOME_CHECKBOX).is_selected())
driver.find_element(*HOME_BUTTON).click()
print(driver.find_element(*HOME_CHECKBOX).is_selected())

''' Проверка всех проставленных чек-боксов '''
driver.find_element(*TOGGLE_BUTTON).click()
driver.find_element(*HOME_BUTTON).click()
for checkbox in driver.find_elements(*CHECKBOXES):
    print(checkbox.is_selected())
    assert checkbox.is_selected(), "Чек-бокс не проставлен"
time.sleep(2)

''' Получения статуса через класс '''
driver.get("https://demoqa.com/selectable")
FIRST_CHECKBOX = ("xpath", "(//ul[@id='verticalListContainer']/li)[1]")
driver.find_element(*FIRST_CHECKBOX).get_attribute("class")
driver.find_element(*FIRST_CHECKBOX).click()
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"

time.sleep(2)