import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.imgonline.com.ua/eng/combine-two-images-into-one.php')
upload_file = driver.find_element(By.XPATH, "//input[@name='uploadfile']")

import os
upload_file.send_keys(os.path.join(os.getcwd(), 'img.jpg'))


time.sleep(1)
driver.quit()