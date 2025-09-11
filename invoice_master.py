import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://pos-app.macomal.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@name="phoneNo"]').send_keys('9854126358')
driver.find_element(By.NAME,"password").send_keys("nirmesh")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']").click()
time.sleep(4)
driver.get("https://pos-app.macomal.com/invoice-series")
driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div[1]/div[1]//*[name()='svg']").click()
driver.find_element(By.XPATH,"//input[@id='prefix']").send_keys('INV')
driver.find_element(By.XPATH,"//input[@id='prefix1']").send_keys('1')
driver.find_element(By.XPATH,"//input[@id='prefix2']").send_keys('2')
driver.find_element(By.XPATH,"//input[@id='suffix']").send_keys('2025')
driver.find_element(By.XPATH,"//input[@id='separator']").send_keys('/')
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Restore']").click()