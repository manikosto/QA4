from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Part 1 --- Call options
options = Options()

# Part 2 --- Driver initialization
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Part 3 --- Set window size
# driver.set_window_size(1920, 1080)
driver.maximize_window()

# Part 4 --- Start browser
driver.get("https://whatismyipaddress.com/")
