import selenium
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH,"//input[@name='name']").send_keys("Anusha")
driver.find_element(By.CSS_SELECTOR," input[class='form-control']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//label[@class='form-check-label']").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

alertText = driver.find_element(By.CLASS_NAME,"alert").text


assert ("Success!" in alertText)

