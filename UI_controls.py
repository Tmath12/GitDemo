from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

print ("-------------------------------------")
#radio button
#radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radios[1].click()
assert radios[1].is_selected()

#print(len(radios))
#for radio in radios:
 #   if radio.get_attribute("value") == "radio2":
  #      radio.click()
   #     break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()



