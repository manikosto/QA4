# Step 1 --- Imports to start
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Step 2 --- Driver initialization Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
# driver = webdriver.Firefox(GeckoDriverManager().install())