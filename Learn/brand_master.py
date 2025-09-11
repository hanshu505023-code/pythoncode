import time

from login import login_pos,By

class brand_mas(login_pos):

    def link_master(self):
        self.driver.get('https://pos-app.macomal.com/brand-master')

    def create_brand(self):
        self.driver.find_element(By.ID,"brandName").send_keys("notebook")
        self.driver.find_element(By.ID,'brandSymbol').send_keys("colour flower")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/button[2]').click()
        time.sleep(5)

    def update_product(self):
        ele = self.driver.find_element(By.XPATH,'//tr[td[text()="notebook"]]/td[1]/div/div[1]')
        time.sleep(1)
        self.action.move_to_element(ele).click().perform()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/button[2]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//tr[td[text()="notebook"]]/td[1]/div/div[2]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//button[text()="Yes, delete it!"]').click()
        time.sleep(4)


bm = brand_mas()
# bm.login_pos_app()
# bm.link_master()
# bm.create_brand()
# bm.update_product()
