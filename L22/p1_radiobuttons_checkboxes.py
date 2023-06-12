from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


path = r'/home/olytvynov/Projects/HL/drivers/chromedriver_linux64_111.0.5563.64'
driver = Chrome(service=Service(path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demo.guru99.com/test/radio.html')

radio_button_1 = driver.find_element(By.ID, 'vfb-7-1')
radio_button_2 = driver.find_element(By.ID, 'vfb-7-2')

print(radio_button_1.is_displayed())
print(radio_button_1.is_enabled())
print(radio_button_1.is_selected())

print()
radio_button_1.click()
time.sleep(1)
radio_button_2.click()

print(radio_button_1.is_displayed())
print(radio_button_1.is_enabled())
print(radio_button_1.is_selected())


check_box1 = driver.find_element(By.ID, 'vfb-6-0')
check_box3 = driver.find_element(By.ID, 'vfb-6-2')

print()
print(check_box1.is_displayed())
print(check_box1.is_enabled())
print(check_box1.is_selected())

check_box1.click()
check_box3.click()
print()
print(check_box1.is_selected())
print(check_box3.is_selected())



time.sleep(1)
driver.quit()
