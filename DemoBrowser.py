from selenium import webdriver

#chrome driver intermediate drive used to invoke browser
from selenium.webdriver.chrome.service import Service
#chrome browser
#service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
#driver = webdriver.Chrome(service=service_obj) #driver is object
#driver.maximize_window()
#driver.get("https://zucitech.com/")
#print(driver.title)
#print(driver.current_url)
#driver.get('https://zucitech.com/careers/')
#driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.forward()
#driver.close()


#firefox browser

service_obj = Service('C:/Users/torga007/Downloads/gecko')
driver = webdriver.Firefox(service=service_obj) #driver is object
driver.maximize_window()
driver.get("https://zucitech.com/")
print(driver.title)
print(driver.current_url)
driver.get('https://zucitech.com/careers/')
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
