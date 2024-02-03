from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#click on shop tab
driver.find_element(By.LINK_TEXT, "Shop").click()

#select the phone to checkout
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productname = product.find_element(By.XPATH,"//div/h4/a").text #gives product name
    if productname == "blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

#checkout
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
countries = driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()

#selecting the checkbox
driver.find_element(By.CSS_SELECTOR,".checkbox-primary").click()

#click on purchase
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
successtext = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in successtext
driver.close()