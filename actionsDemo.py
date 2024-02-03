from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/torga007/Desktop/Sele/gecko')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

#action.click_and_hold(driver.find_element( ))
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
action.double_click(driver.find_element(By.ID, "checkBoxOption1")).perform()




