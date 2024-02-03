from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_elements(By.XPATH, "//input[@type='text']")
name = "Rahul"
driver.find_element(By.NAME,"enter-name").send_keys(name)
#driver.find_element(By.CSS_SELECTOR,"#name").send_keys("rahul")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
#alert.accept()
#alert.dismiss()


