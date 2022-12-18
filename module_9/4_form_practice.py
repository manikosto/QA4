
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
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/automation-practice-form")

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

# Ввод имени
driver.find_element(*NAME_FIELD).clear() # Чистим поле
driver.find_element(*NAME_FIELD).send_keys("Aleksei") # Вводим текст
assert driver.find_element(*NAME_FIELD).get_attribute("value") == "Aleksei", "Имя не введено" # Проверяем, что текст введен

# Ввод фамилии
driver.find_element(*LAST_NAME_FIELD).clear() # Чистим поле
driver.find_element(*LAST_NAME_FIELD).send_keys("Pum") # Вводим текст
assert driver.find_element(*LAST_NAME_FIELD).get_attribute("value") == "Pum", "Фамилия не введена" # Проверяем, что текст введен

# Ввод email
driver.find_element(*EMAIL_FIELD).clear() # Чистим поле
driver.find_element(*EMAIL_FIELD).send_keys("akoledachkin@ya.ru") # Вводим текст
assert driver.find_element(*EMAIL_FIELD).get_attribute("value") == "akoledachkin@ya.ru", "Email не введен" # Проверяем, что текст введен

# Выбираем пол через радио (по приниципу 1 элемент для взаимодействия, 1 для статуса)
driver.find_element(*GENDER_LABEL).click() # Клик на элемент для взаимодействия
assert driver.find_element(*GENDER_STATUS).is_selected() is True, "Флага нет" # Проверка, что флаг выставился

# Ввод номера телефона
driver.find_element(*MOBILE_NUMBER_FIELD).clear() # Чистим поле
driver.find_element(*MOBILE_NUMBER_FIELD).send_keys("8999999999") # Вводим текст
assert driver.find_element(*MOBILE_NUMBER_FIELD).get_attribute("value") == "8999999999", "Номер не введен" # Проверяем, что текст введен

# Выбирали темы используя новый мультиселект

# Тема 1
driver.find_element(*SUBJECTS_FIELD).send_keys("en") # Вписываем часть слова в dropdown
wait.until(EC.text_to_be_present_in_element_value(SUBJECTS_FIELD, "en")) # Ждем пока в dropdown появится нужный текст
driver.find_element(*SUBJECTS_FIELD).send_keys(Keys.TAB) # Нажимаем TAB для полного заполнения

# Тема 2
driver.find_element(*SUBJECTS_FIELD).send_keys("com") # Вписываем часть слова в dropdown
wait.until(EC.text_to_be_present_in_element_value(SUBJECTS_FIELD, "com")) # Ждем пока в dropdown появится нужный текст
driver.find_element(*SUBJECTS_FIELD).send_keys(Keys.ARROW_DOWN, Keys.TAB) # Нажимаем TAB для полного заполнения

# Выбраем хобби через чек-бокс (по приниципу 1 элемент для взаимодействия, 1 для статуса)
driver.find_element(*HOBBIES_MUSIC_LABEL).click() # Клик на элемент для взаимодействия
assert driver.find_element(*HOBBIES_MUSIC_STATUS).is_selected() is True, "Чек-бокс не выбран" # Проверка, что флаг выставился

# Грузим файл
driver.find_element(*PICTURE_FIELD).send_keys(os.getcwd() + "/files/pic.jpg")

# Вводим адрес
driver.find_element(*CURRENT_ADDRESS).clear() # Чистим поле
driver.find_element(*CURRENT_ADDRESS).send_keys("Gieldowa 4c, Warsaw")
assert driver.find_element(*CURRENT_ADDRESS).get_attribute("value") == "Gieldowa 4c, Warsaw", "Адрес не введен" # Проверяем, что текст введен

# Выбор штата
driver.find_element(*STATE_SELECT).send_keys("Har") # Вписываем часть слова в dropdown
wait.until(EC.text_to_be_present_in_element_value(STATE_SELECT, "Har")) # Ждем пока в dropdown появится нужный текст
driver.find_element(*STATE_SELECT).send_keys(Keys.TAB) # Нажимаем TAB для полного заполнения

# Проверели, что dropdown city стал доступен
assert driver.find_element(*CITY_SELECT).is_enabled() is True, "Поле недоступно"

# Ввели город
driver.find_element(*CITY_SELECT).send_keys("Kar") # Вписываем часть слова в dropdown
wait.until(EC.text_to_be_present_in_element_value(CITY_SELECT, "Kar")) # Ждем пока в dropdown появится нужный текст
driver.find_element(*CITY_SELECT).send_keys(Keys.TAB) # Нажимаем TAB для полного заполнения

# Клик на submit button
wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)) # Ожидаем кликабельности кнопки
driver.find_element(*SUBMIT_BUTTON).click() # Кликаем

# Убедились, что форма отправлена
wait.until(EC.visibility_of_element_located(NOTIFICATION)) # Ожидаем появления нотификации
assert driver.find_element(*NOTIFICATION), "Элемент не найден" # Убеждаемся, что элемент найден
