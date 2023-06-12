import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/test/delete_customer.php")

submit_button = driver.find_element(By.XPATH, '//input[@name="submit"]')
submit_button.click()
alert = driver.switch_to.alert
time.sleep(0.5)
print(alert.text)
#alert.dismiss()
alert.accept()

time.sleep(1)
driver.quit()
