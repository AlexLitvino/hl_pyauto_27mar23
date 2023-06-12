import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

# Datepicker

driver.get('https://demo.guru99.com/test/')
date_picker = driver.find_element(By.XPATH, "//input[@name='bdaytime']")
date_picker.send_keys('11012023')
date_picker.send_keys(Keys.TAB)
date_picker.send_keys('0914PM')

# submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
# submit_button.click()

form = driver.find_element(By.XPATH, "//form[@name='bdate']")
form.submit()

time.sleep(1)
driver.quit()