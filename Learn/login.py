
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class login_pos:
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    # driver.implicitly_wait(10)
    def login_pos_app(self):
        self.driver.get("https://pos-app.macomal.com")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@name="phoneNo"]').send_keys(9854126358)
        self.driver.find_element(By.NAME,"password").send_keys("nirmesh")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[text()="PROCEED"]').click()
        time.sleep(2)


log = login_pos()
# log.login_pos_app()