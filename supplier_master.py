import time
from selenium import  webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://pos-app.macomal.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@name="phoneNo"]').send_keys('9854126358')
driver.find_element(By.NAME,"password").send_keys("nirmesh")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']").click()
time.sleep(4)
driver.get("https://pos-app.macomal.com/supplier-master")
driver.find_element(By.XPATH,"//input[@id='supplierName']").send_keys('Samsung private limited')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='supplierPhoneNo']").send_keys('9971719590')
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='supplierEmail']").send_keys('sugar@gmail.com')
driver.find_element(By.XPATH,"//input[@id='supplierGSTNo']").send_keys('24AAACC1206D1ZM')
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='supplierCity']").send_keys('Delhi')
driver.find_element(By.XPATH,"//input[@id='supplierPincode']").send_keys('110053')
driver.find_element(By.XPATH,"//input[@id='supplierAddress']").send_keys('New delhi')
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
time.sleep(4)
## User reset ##
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]/div/div[1]').click()
driver.find_element(By.XPATH,"//button[normalize-space()='Reset']").click()
time.sleep(4)
## User update ##
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]/div/div[1]').click()
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
time.sleep(2)

## User delete ##
ele = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr[9]/td[1]/div/div[2]').click()
time.sleep(2)
actions.send_keys(Keys.ENTER).perform()
time.sleep(1)