from selenium import webdriver

# chrome driver intermediate drive used to invoke browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome browser
service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("Demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@123")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@123")
#driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
driver.find_element(By.XPATH, "//button[text()= 'Save New Password']").click()




