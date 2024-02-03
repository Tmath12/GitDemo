from selenium import webdriver

# chrome driver intermediate drive used to invoke browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#print ("abcd")

# chrome browser
service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# locator ID,Xpath , CSSSelector , name , classname, linktext
# driver.find_element(By.NAME,"Main-form")
# driver.find_element(By.NAME, "name").send_keys("ABC")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123234")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath for any element //tagname[@attribute='value']
# cssSelector tag-name[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul shetty")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

#static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message


driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello again")
#driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()