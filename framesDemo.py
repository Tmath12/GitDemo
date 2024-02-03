from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/torga007/Desktop/Sele/gecko')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")


driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hi hello")
driver.switch_to.default_content()


header = driver.find_element(By.CSS_SELECTOR, "h3").text
print(header)






