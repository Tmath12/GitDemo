from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('/Users/torga007/Downloads/chromedriver-win64')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(10)

action = ActionChains(driver)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

Text = str(driver.find_element(By.CSS_SELECTOR, ".red").text)
print(Text)
name = Text[19:48]
print(name)

driver.close()
driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(name)
driver.find_element(By.NAME, "password").send_keys("student")
radios = driver.find_element(By.XPATH, "//input[@value = 'user']")
radios.is_selected()

dropdown = Select(driver.find_element(By.XPATH, "//select[@class = 'form-control']"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Consultant")

driver.find_element(By.NAME, "terms").click()

driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver,10)

assert wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
driver.close()