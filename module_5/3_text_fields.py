import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/text-box")

# Записываем найденный элемент (text box) в переменную
email_field = driver.find_element(By.XPATH, "//input[@id='userName']")

# Чистим поле
email_field.clear()

# Записываем значение поля в переменную
element_value = email_field.get_attribute("value")
time.sleep(2)

# Проверяем, что в поле пусто
assert element_value == ""

time.sleep(2)
# Вводим логин в поле email
email_field.send_keys("example@yandex.ru")
time.sleep(2)

driver.find_element(By.XPATH, "//textarea").send_keys("example@yandex.ru")
time.sleep(2)

# Записываем значение поля в переменную
email_field_value = email_field.get_attribute("value")

# Проверяем, что в поле email содержится введенный логин
assert "example@yandex.ru" in email_field_value

time.sleep(2)