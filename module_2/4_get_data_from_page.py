# Step 1 --- Imports to start
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Step 2 --- Driver initialization Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 3 --- Get page
driver.get("https://ozon.ru")

# Step 4 --- Get title
page_title = driver.title
print("Title страницы: ", page_title)

# Step 5 --- Get current URL
my_url = driver.current_url
print(my_url)

# Step 6 --- Get source code
page_code = driver.page_source
print(page_code)