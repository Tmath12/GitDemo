from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Firefox options if needed
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

# Specify the path to the Firefox GeckoDriver executable
service = Service('/Users/torga007/Desktop/Sele/gecko')

# Create a Firefox WebDriver instance
driver = webdriver.Firefox(service=service, options=firefox_options)
driver.implicitly_wait(5)

# Your automation code
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,500);")
driver.execute_script("window.scrollBy(0,100);")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("e1.png")
