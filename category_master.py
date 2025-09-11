import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://pos-app.macomal.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@name="phoneNo"]').send_keys('9854126358')
driver.find_element(By.NAME,"password").send_keys("nirmesh")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']").click()
time.sleep(2)
driver.get('https://pos-app.macomal.com/category-master')
driver.find_element(By.ID,'categoryName').send_keys(str('Test_category'))
time.sleep(1)
driver.find_element(By.XPATH,'(//*[@tabindex="0"])[1]').click()
time.sleep(1)
brand_name = 'vivo'
driver.find_element(By.XPATH,'//li[text()="'+str(brand_name)+'"]').click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
time.sleep(2)
## user category will be updated ##

driver.find_element(By.XPATH,"//tbody/tr[9]/td[1]/div[1]/div[1]//*[name()='svg']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
time.sleep(2)
## reset data ##
driver.find_element(By.XPATH,"//tbody/tr[9]/td[1]/div[1]/div[1]//*[name()='svg']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[normalize-space()='Reset']").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[3]/div/div/table/tbody/tr[9]/td[1]/div/div[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Yes, delete it!']").click()
time.sleep(2)

