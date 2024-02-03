from selenium import webdriver

# chrome driver intermediate drive used to invoke browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/torga007/Desktop/Sele/gecko')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

browsersortedlist = []

#click on column header
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#driver.find_element(By.LINK_TEXT,"Top Deals").click()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#windowsopened = driver.window_handles
#driver.switch_to.window(windowsopened[0])
#collect veggie names - >veggielist (browser sort)
veggiewebelement = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggiewebelement:
    browsersortedlist.append(ele.text)

browserlist = browsersortedlist.copy()
#sort this veggielist => new sorted veglist

browsersortedlist.sort()

assert browsersortedlist == browserlist

#veggielist = new sorted veglist


driver.close()

