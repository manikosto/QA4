
import time
import os
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
options.add_argument("--user-agent=Automation 1 QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://yandex.ru")

NAME_FIELD = ("xpath", "//input[@id='firstName']")
LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
GENDER_STATUS = ("xpath", "//input[@id='gender-radio-1']")
GENDER_LABEL = ("xpath", "//label[@for='gender-radio-1']")
MOBILE_NUMBER_FIELD = ("xpath", "//input[@id='userNumber']")
SUBJECTS_FIELD = ("xpath", "//input[@id='subjectsInput']")
HOBBIES_MUSIC_STATUS = ("xpath", "//input[@id='hobbies-checkbox-3']")
HOBBIES_MUSIC_LABEL = ("xpath", "//label[@for='hobbies-checkbox-3']")
PICTURE_FIELD = ("xpath", "//input[@id='uploadPicture']")
CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
STATE_SELECT = ("xpath", "//input[@id='react-select-3-input']")
CITY_SELECT = ("xpath", "//input[@id='react-select-4-input']")
SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
NOTIFICATION = ("xpath", "//div[text()='Thanks for submitting the form']")
CLOSE_BUTTON = ("xpath", "//button[@id='closeLargeModal']")

def enter_data(locator, data):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(data)
    assert driver.find_element(*locator).get_attribute("value") == data, "Текст не введен"

def click_radio_or_checkbox_button(locator_for_click, locator_for_status):
    driver.find_element(*locator_for_click).click()
    assert driver.find_element(*locator_for_status).is_selected() is True, "Флага нет"

def enter_data_in_select(locator, data):
    driver.find_element(*locator).send_keys(data) # Вписываем часть слова в dropdown
    wait.until(EC.text_to_be_present_in_element_value(locator, data)) # Ждем пока в dropdown появится нужный текст
    driver.find_element(*locator).send_keys(Keys.TAB) # Нажимаем TAB для полного заполнения

def upload_file(locator, file_name):
    driver.find_element(*locator).send_keys(os.getcwd() + f"/files/{file_name}")

def click_on(locator):
    wait.until(EC.element_to_be_clickable(locator))
    driver.find_element(*locator).click()

def wait_for_element_invisible(locator):
    wait.until(EC.visibility_of_element_located(locator))
    assert driver.find_element(*locator), "Элемент не найден"

enter_data(NAME_FIELD, "Алексей")
enter_data(LAST_NAME_FIELD, "Коледачкин")
enter_data(EMAIL_FIELD, "manikosto@outlook.com")
click_radio_or_checkbox_button(GENDER_LABEL, GENDER_STATUS)
enter_data(MOBILE_NUMBER_FIELD, "8999999999")
enter_data_in_select(SUBJECTS_FIELD, "en")
enter_data_in_select(SUBJECTS_FIELD, "com")
click_radio_or_checkbox_button(HOBBIES_MUSIC_LABEL, HOBBIES_MUSIC_STATUS)
upload_file(PICTURE_FIELD, "pic.jpg")
enter_data(CURRENT_ADDRESS, "Gieldowa 4c, Warsaw")
enter_data_in_select(STATE_SELECT, "Har")
enter_data_in_select(CITY_SELECT, "Kar")
click_on(SUBMIT_BUTTON)
wait_for_element_invisible(NOTIFICATION)
click_on(CLOSE_BUTTON)

time.sleep(3)

