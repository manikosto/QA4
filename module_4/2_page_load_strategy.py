from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Part 1 --- Call options
options = Options()

# Part 2 --- Page load strategy
# --- Normal ---
options.page_load_strategy = 'normal'  # Used by default, waits for all resources to download | BY DEFAULT
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://whatismyipaddress.com/")

# --- Eager ---
options.page_load_strategy = 'eager'  # DOM access is ready, but other resources like images may still be loading
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://whatismyipaddress.com/")

# # # --- None ---
options.page_load_strategy = 'none'  # Does not block WebDriver at all
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://whatismyipaddress.com/")

