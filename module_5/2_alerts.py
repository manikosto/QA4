import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/alerts")

time.sleep(3)

first_alert_button = driver.find_element(By.XPATH, "(//button[text()='Click me'])[1]")
second_alert_button = driver.find_element(By.XPATH, "(//button[text()='Click me'])[2]")
confirm_and_cancel_alert_button = driver.find_element(By.XPATH, "(//button[text()='Click me'])[3]")
prompt_alert_button = driver.find_element(By.XPATH, "(//button[text()='Click me'])[4]")

prompt_alert_button.click()
time.sleep(3)

alert = driver.switch_to.alert
# alert.text  # Получение текста алерта
# alert.accept()  # Принять Alert
# alert.dismiss()  # Отклонить Alert
alert.send_keys("Hello")  # Ввод данных в Alert
alert.accept()
time.sleep(3)


